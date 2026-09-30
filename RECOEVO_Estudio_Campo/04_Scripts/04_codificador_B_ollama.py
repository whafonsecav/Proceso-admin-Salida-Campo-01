"""Codificador B independiente: modelo local (Ollama, qwen2.5:14b) aplica el mismo libro de códigos
a cada unidad de significado, sin ver la codificación del codificador A.
Sirve para medir acuerdo intercodificador (kappa de Cohen) y revisar desacuerdos.
Salida: 03_Base_de_Datos/codificacion_B_ollama.json
"""
import json, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "RECOEVO_Estudio_Campo"
CB = json.loads((BASE / "02_Metodologia" / "codebook.json").read_text(encoding="utf-8"))
UNITS = json.loads((BASE / "03_Base_de_Datos" / "unidades.json").read_text(encoding="utf-8"))
OUT = BASE / "03_Base_de_Datos" / "codificacion_B_ollama.json"
MODEL = sys.argv[1] if len(sys.argv) > 1 else "qwen2.5:14b"

codes_txt = "\n".join(f"- {c['id']}: {c['nombre']}. {c['definicion']} Incluye: {c['incluye']}. {('Excluye: ' + c['excluye']) if c['excluye'] else ''}"
                      for c in CB["codigos"])
sat = CB["escalas"]["satisfaccion"]; dis = CB["escalas"]["disposicion"]
SYSTEM = f"""Eres un investigador cualitativo experto que codifica entrevistas semiestructuradas sobre residuos orgánicos en Usme (Bogotá).
Aplica ESTRICTAMENTE este libro de códigos. Asigna de 0 a 3 códigos a la unidad (solo los que estén claramente presentes).
CÓDIGOS:
{codes_txt}

ESCALA satisfaccion (1-5) — {sat['nombre']}: {json.dumps(sat['anclas'], ensure_ascii=False)}. Usa null si {sat['na']}.
ESCALA disposicion (1-5) — {dis['nombre']}: {json.dumps(dis['anclas'], ensure_ascii=False)}. Usa null si {dis['na']}.

Responde SOLO JSON: {{"codigos": ["ID", ...], "satisfaccion": n|null, "disposicion": n|null}}"""

def ask(unit):
    user = f"Pregunta previa del entrevistador: {unit.get('pregunta') or '(ninguna)'}\nRespuesta del participante (unidad a codificar): {unit['texto']}"
    body = json.dumps({"model": MODEL, "stream": False, "format": "json",
                       "options": {"temperature": 0, "num_ctx": 8192},
                       "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]}).encode()
    req = urllib.request.Request("http://localhost:11434/api/chat", body, {"Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=300).read())
    try:
        j = json.loads(r["message"]["content"])
    except Exception:
        j = {"codigos": [], "satisfaccion": None, "disposicion": None, "error": r["message"]["content"][:200]}
    valid = {c["id"] for c in CB["codigos"]}
    j["codigos"] = [c for c in j.get("codigos", []) if c in valid][:3]
    return j

res = {}
if OUT.exists():
    res = json.loads(OUT.read_text(encoding="utf-8"))
for i, u in enumerate(UNITS, 1):
    if u["id"] in res:
        continue
    res[u["id"]] = ask(u)
    if i % 10 == 0:
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{i}/{len(UNITS)}", flush=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print("listo", len(res))
