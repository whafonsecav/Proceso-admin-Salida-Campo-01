"""Genera 05_Presentacion/data.js: todas las frases (literal + editada + minuto del audio) y los agregados.
Las cifras de la presentación se calculan en el navegador a partir de estas mismas frases, de modo que
lo que se ve al hacer clic en un número es exactamente lo que produce ese número."""
import json, re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]; DB = BASE / "03_Base_de_Datos"
R = json.loads((DB / "resultados.json").read_text(encoding="utf-8"))
V = json.loads((BASE / "01_Validacion_Transcripciones" / "validacion.json").read_text(encoding="utf-8"))
CB = json.loads((BASE / "02_Metodologia" / "codebook.json").read_text(encoding="utf-8"))
U = json.loads((DB / "unidades_codificadas.json").read_text(encoding="utf-8"))
ED = json.loads((DB / "edicion_aceptada.json").read_text(encoding="utf-8"))   # ediciones del modelo local que pasaron el filtro
REV = json.loads((DB / "revision_edicion.json").read_text(encoding="utf-8"))  # edición manual de las rechazadas
T = json.loads((DB / "tiempos.json").read_text(encoding="utf-8"))
SHUT = re.compile(r"\b(chux|chuck|chute|chut|chuc)\b", re.I)
# Anonimización (la autorización exige citas sin nombre): nombres de participantes → su código
ANON = [(r"\b(Don|Señor|señor)\s+José\b", "[E01]"), (r"\bJosé\b", "[E01]"),
        (r"\b(Don|Señor|señor)\s+[ÁA]lvaro(\s*\[P[ée]rez\])?", "[E02]"), (r"\b[ÁA]lvaro\b", "[E02]"),
        (r"\b(Don|Señor|señor)\s+P[ée]rez\b", "[E03]"), (r"\bP[ée]rez\b", "[E03]"),
        (r"Juan Sebasti[áa]n( Torres Garc[íi]a)?", "[E04]"), (r"Valentina( Rodr[íi]guez)?", "[E07]"), (r"Isaac( Pardo)?", "[E08]")]
def anon(t):
    for a, b in ANON: t = re.sub(a, b, t or "")
    return t
units = []
for u in U:
    if not (u["codigos"] or u["satisfaccion"] or u["disposicion"]): continue
    ed = anon(SHUT.sub("shut", REV.get(u["id"]) or ED.get(u["id"]) or u["texto"]))
    units.append({"id": u["id"], "p": u["participante"], "a": u["audio"], "t": T.get(u["id"], {}).get("t"),
                  "q": anon(u["pregunta"]), "o": anon(u["texto"]), "e": ed, "c": u["codigos"], "s": u["satisfaccion"],
                  "d": u["disposicion"], "k": u["condiciones"], "n": u["nota"]})
data = {
    "codigos": [{"id": c["id"], "nombre": c["nombre"], "dim": c["dim"], "def": c["definicion"]} for c in CB["codigos"]],
    "dimensiones": CB["dimensiones"], "escalas": CB["escalas"],
    "participantes": {k: {"rol": v["rol"], "detalle": v["detalle"], "audios": v["audios"]} for k, v in R["participantes"].items()},
    "saturacion": R["saturacion_permutada"], "acuerdo": {k: v for k, v in R["acuerdo"].items() if k != "por_codigo"},
    "validacion": [{"audio": v["audio"], "similitud": v["similitud"], "duracion": v["duracion_s"]} for v in V],
    "units": units,
}
(BASE / "05_Presentacion" / "data.js").write_text("window.RECOEVO = " + json.dumps(data, ensure_ascii=False) + ";", encoding="utf-8")
(DB / "frases_finales.json").write_text(json.dumps(units, ensure_ascii=False, indent=1), encoding="utf-8")
print("data.js ok · frases:", len(units), "· con minuto:", sum(1 for u in units if u["t"] is not None),
      "· editadas:", sum(1 for u in units if u["e"] != u["o"]), "· 'chux' restantes:", sum(1 for u in units if re.search("chux|chuck", u["e"], re.I)))
