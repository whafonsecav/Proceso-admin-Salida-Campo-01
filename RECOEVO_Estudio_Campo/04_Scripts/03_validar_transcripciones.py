"""Valida cada transcripción existente contra la re-transcripción Whisper large-v3.
Métricas por audio: WER aproximado (alineación de palabras normalizadas), cobertura (qué % del audio
quedó en la transcripción) y lista de bloques omitidos/añadidos de más de 6 palabras para revisión humana.
Salida: 01_Validacion_Transcripciones/validacion.json y reporte_validacion.md
"""
import json, re, unicodedata, difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "RECOEVO_Estudio_Campo" / "01_Validacion_Transcripciones"
W = BASE / "whisper"

def norm(t, labels=True):
    if labels: t = re.sub(r"^(Speaker \d|Entrevistador|Entrevistad[oa]|Don Álvaro|Don Pérez|Juan Sebastián|Valentina|Isaac|Participantes|Entrevista sobre)[^:\n]*:?", "", t, flags=re.M)
    t = re.sub(r"\d\d:\d\d", " ", t).replace("****", " ")
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(ch for ch in t if unicodedata.category(ch) != "Mn")
    return re.findall(r"[a-zñ0-9]+", t)

def wer(ref, hyp):  # ref = audio (Whisper), hyp = transcripción entregada
    sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
    S = D = I = 0; blocks = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "replace": S += max(i2 - i1, j2 - j1)
        elif op == "delete": D += i2 - i1
        elif op == "insert": I += j2 - j1
        if op != "equal" and max(i2 - i1, j2 - j1) >= 7:
            blocks.append({"tipo": op, "en_audio_whisper": " ".join(ref[i1:i2]), "en_transcripcion": " ".join(hyp[j1:j2])})
    return (S + D + I) / max(len(ref), 1), sm.ratio(), blocks

res = []
for n in range(1, 11):
    wj = json.loads((W / f"Audio{n}.json").read_text(encoding="utf-8"))
    hyp = norm(" ".join(s["text"] for s in wj["segments"]), labels=False)
    ref = norm((ROOT / "Entrevistas" / f"Audio{n}.txt").read_text(encoding="utf-8"))
    w, ratio, blocks = wer(hyp, ref)  # referencia = audio (Whisper); hipótesis = transcripción entregada
    res.append({"audio": f"Audio{n}", "duracion_s": round(wj["duration"]), "palabras_audio": len(hyp),
                "palabras_transcripcion": len(ref), "cobertura": round(len(ref) / max(len(hyp), 1), 3),
                "wer_aprox": round(w, 3), "similitud": round(ratio, 3),
                "bloques_divergentes": blocks})
(BASE / "validacion.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
for r in res:
    print(f"{r['audio']}: {r['duracion_s']}s | audio {r['palabras_audio']} pal · transc {r['palabras_transcripcion']} pal | "
          f"cobertura {r['cobertura']:.0%} | WER≈{r['wer_aprox']:.0%} | similitud {r['similitud']:.0%} | bloques {len(r['bloques_divergentes'])}")
