"""Integra unidades + codificación A (investigador) + codificación B (modelo local) y calcula:
frecuencias por código/dimensión, matriz participante×código, co-ocurrencias, curva de saturación,
índices de satisfacción/disposición, y acuerdo intercodificador (kappa de Cohen / kappa ponderado).
Salida: 03_Base_de_Datos/resultados.json (alimenta la presentación)
"""
import json, itertools, math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "RECOEVO_Estudio_Campo"
DB = BASE / "03_Base_de_Datos"
CB = json.loads((BASE / "02_Metodologia" / "codebook.json").read_text(encoding="utf-8"))
UNITS = json.loads((DB / "unidades.json").read_text(encoding="utf-8"))
B = json.loads((DB / "codificacion_B_ollama.json").read_text(encoding="utf-8")) if (DB / "codificacion_B_ollama.json").exists() else {}
CODES = [c["id"] for c in CB["codigos"]]
DIM = {c["id"]: c["dim"] for c in CB["codigos"]}

PERFIL = {
    "E01": {"rol": "Hogar", "detalle": "Residente de la parte alta, saca la basura de su casa", "audios": ["Audio1"], "genero": "H"},
    "E02": {"rol": "Comercio · líder", "detalle": "Comerciante fundador, líder comunal (36 años en el sector)", "audios": ["Audio2", "Audio3"], "genero": "H"},
    "E03": {"rol": "Hogar · líder", "detalle": "Líder comunitario (50 años en el barrio)", "audios": ["Audio4"], "genero": "H"},
    "E04": {"rol": "Comercio de alimentos", "detalle": "Trabajador de fruver", "audios": ["Audio5"], "genero": "H"},
    "E05": {"rol": "Comercio + hogar", "detalle": "Comerciante arrendataria, 36 años en la zona, hogar de 4", "audios": ["Audio6", "Audio10"], "genero": "M"},
    "E06": {"rol": "Hogar", "detalle": "Residente adulto mayor, vive con su hija", "audios": ["Audio7"], "genero": "H"},
    "E07": {"rol": "Hogar + comercio", "detalle": "Residente joven (4 años), atiende un comercio", "audios": ["Audio8"], "genero": "M"},
    "E08": {"rol": "Comercio", "detalle": "Comerciante (5 años), vive en otra zona residencial", "audios": ["Audio9"], "genero": "H"},
}

# ---- codificación A ----
A = {}
for line in (DB / "codificacion_A.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip() or line.startswith("#"): continue
    p = [x.strip() for x in line.split("|")]
    codes = [c for c in p[1].split(",") if c]
    A[p[0]] = {"codigos": codes, "satisfaccion": None if p[2] == "-" else int(p[2]),
               "disposicion": None if p[3] == "-" else int(p[3]),
               "condiciones": [c for c in p[4].split(",") if c] if len(p) > 4 else [], "nota": p[5] if len(p) > 5 else ""}
units = [u for u in UNITS if "X" not in A[u["id"]]["codigos"]]
for u in units:
    u.update({k: A[u["id"]][k] for k in ("codigos", "satisfaccion", "disposicion", "condiciones", "nota")})
    b = B.get(u["id"], {})
    u["codigos_B"] = b.get("codigos", []); u["satisfaccion_B"] = b.get("satisfaccion"); u["disposicion_B"] = b.get("disposicion")
    u["dimensiones"] = sorted({DIM[c] for c in u["codigos"]})
sust = [u for u in units if u["codigos"]]
parts = sorted(PERFIL)

# ---- frecuencias ----
freq = {}
for c in CODES:
    us = [u for u in sust if c in u["codigos"]]
    ps = sorted({u["participante"] for u in us})
    freq[c] = {"unidades": len(us), "participantes": ps, "n_part": len(ps), "pct_part": round(len(ps) / len(parts) * 100)}
dimfreq = {}
for d in CB["dimensiones"]:
    us = [u for u in sust if d["id"] in u["dimensiones"]]
    dimfreq[d["id"]] = {"unidades": len(us), "n_part": len({u["participante"] for u in us}),
                        "pct_unidades": round(len(us) / len(sust) * 100)}
matriz = {p: {c: sum(1 for u in sust if u["participante"] == p and c in u["codigos"]) for c in CODES} for p in parts}

# ---- co-ocurrencias (en la misma unidad) ----
co = Counter()
for u in sust:
    for a, b in itertools.combinations(sorted(u["codigos"]), 2): co[(a, b)] += 1
coocs = [{"a": a, "b": b, "n": n} for (a, b), n in co.most_common(15)]

# ---- saturación: códigos nuevos por entrevista (orden de campo) ----
seen, sat_curve = set(), []
for p in parts:
    new = {c for u in sust if u["participante"] == p for c in u["codigos"]} - seen
    seen |= new
    sat_curve.append({"participante": p, "nuevos": len(new), "acumulado": len(seen), "codigos_nuevos": sorted(new)})

# saturación robusta: promedio sobre 1000 órdenes aleatorios (evita depender del orden de campo)
import random
random.seed(7)
codes_by_p = {p: {c for u in sust if u["participante"] == p for c in u["codigos"]} for p in parts}
acc = [0.0] * len(parts)
for _ in range(1000):
    order = parts[:]; random.shuffle(order); s = set()
    for i, p in enumerate(order):
        s |= codes_by_p[p]; acc[i] += len(s)
sat_perm = [round(a / 1000, 2) for a in acc]
n80 = next(i + 1 for i, v in enumerate(sat_perm) if v >= 0.8 * len(CODES))

# ---- escalas ----
def dist(key, us):
    v = [u[key] for u in us if u[key] is not None]
    d = Counter(v)
    return {"n": len(v), "media": round(sum(v) / len(v), 2) if v else None,
            "dist": {str(k): d.get(k, 0) for k in range(1, 6)}}
escalas = {"satisfaccion": dist("satisfaccion", units), "disposicion": dist("disposicion", units),
           "por_participante": {p: {"satisfaccion": dist("satisfaccion", [u for u in units if u["participante"] == p])["media"],
                                    "disposicion": dist("disposicion", [u for u in units if u["participante"] == p])["media"]} for p in parts},
           "satisfaccion_por_codigo": {c: dist("satisfaccion", [u for u in units if c in u["codigos"]])["media"] for c in CODES}}

# ---- acuerdo intercodificador ----
def kappa(x, y):
    n = len(x); po = sum(a == b for a, b in zip(x, y)) / n
    px = sum(x) / n; py = sum(y) / n
    pe = px * py + (1 - px) * (1 - py)
    return round((po - pe) / (1 - pe), 3) if pe < 1 else 1.0, round(po, 3)
def wkappa(pairs):  # kappa ponderado cuadrático 1-5
    if not pairs: return None
    k = 5; n = len(pairs)
    O = [[0] * k for _ in range(k)]
    for a, b in pairs: O[a - 1][b - 1] += 1
    ra = [sum(r) for r in O]; cb = [sum(O[i][j] for i in range(k)) for j in range(k)]
    num = sum(((i - j) ** 2) * O[i][j] for i in range(k) for j in range(k))
    den = sum(((i - j) ** 2) * ra[i] * cb[j] / n for i in range(k) for j in range(k))
    return round(1 - num / den, 3) if den else None
acuerdo = None
coded_B = [u for u in units if u["id"] in B]
if coded_B:
    per = {}
    for c in CODES:
        x = [int(c in u["codigos"]) for u in coded_B]; y = [int(c in u["codigos_B"]) for u in coded_B]
        if sum(x) + sum(y) == 0: continue
        per[c] = dict(zip(("kappa", "acuerdo"), kappa(x, y)))
    allx = [int(c in u["codigos"]) for u in coded_B for c in CODES]; ally = [int(c in u["codigos_B"]) for u in coded_B for c in CODES]
    k_all, po_all = kappa(allx, ally)
    ks = [v["kappa"] for v in per.values()]
    acuerdo = {"n_unidades": len(coded_B), "kappa_global": k_all, "acuerdo_global": po_all,
               "kappa_medio_por_codigo": round(sum(ks) / len(ks), 3), "por_codigo": per,
               "kappa_pond_satisfaccion": wkappa([(u["satisfaccion"], u["satisfaccion_B"]) for u in coded_B if u["satisfaccion"] and isinstance(u["satisfaccion_B"], int) and 1 <= u["satisfaccion_B"] <= 5]),
               "kappa_pond_disposicion": wkappa([(u["disposicion"], u["disposicion_B"]) for u in coded_B if u["disposicion"] and isinstance(u["disposicion_B"], int) and 1 <= u["disposicion_B"] <= 5])}

# ---- nivel persona (lo que se reporta en la presentación) ----
def pmean(key, p):
    v = [u[key] for u in units if u["participante"] == p and u[key] is not None]
    return round(sum(v) / len(v), 2) if v else None
personas = {p: {"satisfaccion": pmean("satisfaccion", p), "disposicion": pmean("disposicion", p),
                "n_sat": sum(1 for u in units if u["participante"] == p and u["satisfaccion"] is not None),
                "n_dis": sum(1 for u in units if u["participante"] == p and u["disposicion"] is not None)} for p in parts}
condiciones = {}
for u in units:
    for c in u["condiciones"]:
        condiciones.setdefault(c, set()).add(u["participante"])
condiciones = {k: sorted(v) for k, v in condiciones.items()}
out = {"n_unidades": len(units), "n_sustantivas": len(sust), "participantes": PERFIL,
       "frecuencias": freq, "dimensiones": dimfreq, "matriz": matriz, "coocurrencias": coocs,
       "saturacion": sat_curve, "saturacion_permutada": sat_perm, "entrevistas_para_80pct": n80, "escalas": escalas, "acuerdo": acuerdo, "personas": personas, "condiciones": condiciones}
(DB / "resultados.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
(DB / "unidades_codificadas.json").write_text(json.dumps(units, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"unidades {len(units)} · sustantivas {len(sust)}")
for c in sorted(CODES, key=lambda c: -freq[c]["n_part"]):
    print(f"  {c} {freq[c]['n_part']}/8 part · {freq[c]['unidades']} u · sat {escalas['satisfaccion_por_codigo'][c]}")
print("dim", dimfreq); print("saturación", [(s['participante'], s['nuevos']) for s in sat_curve])
print("sat_perm", sat_perm, "n80", n80); print("sat", escalas["satisfaccion"]); print("dis", escalas["disposicion"])
print("por participante", escalas["por_participante"])
print("personas", personas); print("condiciones", condiciones); print("co", coocs[:8]); print("acuerdo", json.dumps(acuerdo, ensure_ascii=False)[:600] if acuerdo else None)
