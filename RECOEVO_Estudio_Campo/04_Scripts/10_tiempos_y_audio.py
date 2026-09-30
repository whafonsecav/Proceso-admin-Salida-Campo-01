"""(1) Ubica cada frase en el audio: alinea sus palabras con los segmentos de Whisper y guarda el segundo de inicio.
(2) Exporta los audios a mp3 mono 48 kbps para reproducir la cita exacta desde la presentación.
Salida: 03_Base_de_Datos/tiempos.json · 05_Presentacion/media/audio/AudioN.mp3"""
import json, re, unicodedata, difflib, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]; BASE = ROOT / "RECOEVO_Estudio_Campo"
U = json.loads((BASE / "03_Base_de_Datos" / "unidades_codificadas.json").read_text(encoding="utf-8"))
def norm(t):
    t = unicodedata.normalize("NFD", t.lower()); t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.findall(r"[a-zñ0-9]+", t)
W = {}
for n in range(1, 11):
    segs = json.loads((BASE / "01_Validacion_Transcripciones" / "whisper" / f"Audio{n}.json").read_text(encoding="utf-8"))["segments"]
    words, starts = [], []
    for s in segs:
        ws = norm(s["text"]); dur = max(s["end"] - s["start"], .1)
        for k, w in enumerate(ws):
            words.append(w); starts.append(s["start"] + dur * k / max(len(ws), 1))
    W[f"Audio{n}"] = (words, starts)
res, last = {}, {}
for u in U:
    words, starts = W[u["audio"]]; q = norm(u["texto"])[:14]
    if len(q) < 2 or not words: continue
    best, bi = 0, None; lo = last.get(u["audio"], 0)
    for i in range(0, max(1, len(words) - len(q) + 1)):
        r = difflib.SequenceMatcher(None, q, words[i:i + len(q)], autojunk=False).ratio() - (0.08 if i < lo - 40 else 0)
        if r > best: best, bi = r, i
    if bi is not None and best >= 0.45:
        res[u["id"]] = {"t": round(max(starts[bi] - 1.0, 0), 1), "conf": round(best, 2)}; last[u["audio"]] = bi
(BASE / "03_Base_de_Datos" / "tiempos.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print("frases ubicadas:", len(res), "de", len(U), "· confianza media", round(sum(v["conf"] for v in res.values()) / len(res), 2))
A = BASE / "05_Presentacion" / "media" / "audio"; A.mkdir(parents=True, exist_ok=True)
for f in sorted((ROOT / "Entrevistas").glob("Audio*.*")):
    if f.suffix == ".txt": continue
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(f), "-vn", "-ac", "1", "-b:a", "48k", str(A / f"{f.stem}.mp3")], check=True)
print("audios exportados:", len(list(A.glob("*.mp3"))), "·", round(sum(p.stat().st_size for p in A.glob("*.mp3")) / 1e6, 1), "MB")
