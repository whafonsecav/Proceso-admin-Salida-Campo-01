"""Edición gramatical conservadora de cada frase con contenido (modelo local Ollama).
No cambia el sentido: corrige puntuación/ortografía y retira muletillas o repeticiones tartamudeadas.
El texto original siempre se conserva junto al editado. Salida: 03_Base_de_Datos/texto_editado.json"""
import json, sys, urllib.request, difflib
from pathlib import Path

DB = Path(__file__).resolve().parents[1] / "03_Base_de_Datos"
U = json.loads((DB / "unidades_codificadas.json").read_text(encoding="utf-8"))
OUT = DB / "texto_editado.json"
MODEL = sys.argv[1] if len(sys.argv) > 1 else "qwen2.5:14b"
SYS = ("Eres editor de transcripciones de entrevistas en español de Colombia. Recibirás una frase dicha oralmente. "
       "Devuélvela corregida con estas reglas ESTRICTAS: (1) corrige ortografía, tildes y puntuación; "
       "(2) elimina repeticiones tartamudeadas y muletillas vacías ('o sea', 'digamos', 'si me entiende', 'pues', 'por ejemplo') SOLO si no aportan significado; "
       "(3) NO cambies palabras con significado, NO agregues ideas, NO resumas, NO cambies la persona gramatical, conserva modismos colombianos "
       "(su merced, chévere, berraquera, shut/chut, fruver); (4) mantén el mismo orden de ideas. Responde SOLO con la frase corregida, sin comillas.")
res = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
todo = [u for u in U if (u["codigos"] or u["satisfaccion"] or u["disposicion"]) and u["id"] not in res]
for i, u in enumerate(todo, 1):
    body = json.dumps({"model": MODEL, "stream": False, "options": {"temperature": 0, "num_ctx": 4096},
                       "messages": [{"role": "system", "content": SYS}, {"role": "user", "content": u["texto"]}]}).encode()
    r = json.loads(urllib.request.urlopen(urllib.request.Request("http://localhost:11434/api/chat", body, {"Content-Type": "application/json"}), timeout=300).read())
    t = r["message"]["content"].strip().strip('"“”')
    res[u["id"]] = {"editado": t, "ratio": round(difflib.SequenceMatcher(None, u["texto"].lower(), t.lower()).ratio(), 3)}
    if i % 10 == 0:
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8"); print(f"{i}/{len(todo)}", flush=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print("listo", len(res), "· a revisar (ratio<0.6):", sum(1 for v in res.values() if v["ratio"] < 0.6))
