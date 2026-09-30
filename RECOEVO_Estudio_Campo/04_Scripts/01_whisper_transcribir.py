"""Re-transcribe los 10 audios con Whisper large-v3 (GPU) para validar las transcripciones existentes.
Salida: 01_Validacion_Transcripciones/whisper/AudioN.json (segmentos con tiempos) y AudioN.txt
"""
import json, os, sys, time, glob, subprocess
import numpy as np
from pathlib import Path

# DLLs de CUDA instaladas vía pip (nvidia-cublas-cu12 / nvidia-cudnn-cu12)
import site
for sp in site.getsitepackages() + [site.getusersitepackages()]:
    for sub in ("nvidia/cublas/bin", "nvidia/cudnn/bin"):
        p = Path(sp) / sub
        if p.exists():
            os.add_dll_directory(str(p))
            os.environ["PATH"] = str(p) + os.pathsep + os.environ["PATH"]

from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "Entrevistas"
OUT = ROOT / "RECOEVO_Estudio_Campo" / "01_Validacion_Transcripciones" / "whisper"
OUT.mkdir(parents=True, exist_ok=True)

PROMPT = ("Entrevista en Usme, Bogotá, barrio Villa Rosita, sobre residuos orgánicos, basuras, "
          "el shut, reciclaje, compost, abono, perros, ratas, junta de acción comunal, fruver.")

model = WhisperModel("large-v3", device="cuda", compute_type="float16")
files = sorted(SRC.glob("Audio*.*"), key=lambda p: int(p.stem.replace("Audio", "")))
for f in files:
    if f.suffix == ".txt":
        continue
    t0 = time.time()
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0
    segs, info = model.transcribe(audio, language="es", beam_size=5, vad_filter=True,
                                  condition_on_previous_text=False, word_timestamps=False,
                                  compression_ratio_threshold=2.2, no_speech_threshold=0.5)
    segs = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(),
             "avg_logprob": round(s.avg_logprob, 3), "no_speech_prob": round(s.no_speech_prob, 3)} for s in segs]
    (OUT / f"{f.stem}.json").write_text(json.dumps({"file": f.name, "duration": info.duration, "segments": segs},
                                                   ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / f"{f.stem}.txt").write_text("\n".join(f"[{s['start']:07.2f}] {s['text']}" for s in segs), encoding="utf-8")
    print(f"{f.name}: {info.duration:.0f}s audio, {len(segs)} segmentos, {time.time()-t0:.0f}s", flush=True)
