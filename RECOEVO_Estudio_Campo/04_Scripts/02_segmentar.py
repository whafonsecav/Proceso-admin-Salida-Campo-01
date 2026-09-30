"""Segmenta las transcripciones en turnos (entrevistador / participante) y unidades de significado.
Audio7 y Audio10 no tienen etiquetas de hablante: se segmentan a partir de la versión Whisper revisada
(01_Validacion_Transcripciones/revisadas/AudioN_revisada.txt) si existe; si no, se omiten.
Salida: 03_Base_de_Datos/turnos.json
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "Entrevistas"
BASE = ROOT / "RECOEVO_Estudio_Campo"
REV = BASE / "01_Validacion_Transcripciones" / "revisadas"
OUT = BASE / "03_Base_de_Datos"
OUT.mkdir(parents=True, exist_ok=True)

INTERVIEWER = re.compile(r"^(Speaker 1|Entrevistador)\s*(\([^)]*\))?\s*:", re.I)
PARTICIPANT = re.compile(r"^(Speaker 2|Don Álvaro|Don Pérez|Juan Sebastián|Entrevistada|Entrevistado|Valentina|Isaac|P)\s*:", re.I)

def parse(text):
    turns, cur = [], None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        m_i, m_p = INTERVIEWER.match(line), PARTICIPANT.match(line)
        if m_i:
            cur = {"rol": "entrevistador", "texto": line[m_i.end():].strip()}
            turns.append(cur)
        elif m_p:
            cur = {"rol": "participante", "texto": line[m_p.end():].strip()}
            turns.append(cur)
        elif line.startswith("****") and cur:
            cur["texto"] += " " + line.lstrip("* ").strip()
        # cabeceras / metadatos se ignoran
    return turns

rows = []
for n in range(1, 11):
    rev = REV / f"Audio{n}_revisada.txt"
    src = rev if rev.exists() else SRC / f"Audio{n}.txt"
    turns = parse(src.read_text(encoding="utf-8"))
    for k, t in enumerate(turns, 1):
        rows.append({"audio": f"Audio{n}", "turno": k, **t, "fuente": src.name})
(OUT / "turnos.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
c = Counter((r["audio"], r["rol"]) for r in rows)
for n in range(1, 11):
    print(f"Audio{n}: entrevistador={c[(f'Audio{n}','entrevistador')]} participante={c[(f'Audio{n}','participante')]}")

# ---------- Unidades de significado (solo participante) ----------
PART = {"Audio1": "E01", "Audio2": "E02", "Audio3": "E02", "Audio4": "E03", "Audio5": "E04",
        "Audio6": "E05", "Audio10": "E05", "Audio7": "E06", "Audio8": "E07", "Audio9": "E08"}
MAXW = 55
def split_units(text):
    sents = re.split(r"(?<=[.!?…])\s+", text)
    chunks, cur = [], []
    for s in sents:
        if cur and len(" ".join(cur + [s]).split()) > MAXW:
            chunks.append(" ".join(cur)); cur = []
        cur.append(s)
    if cur: chunks.append(" ".join(cur))
    return chunks

units, last_q = [], {}
for r in rows:
    if r["rol"] == "entrevistador":
        last_q[r["audio"]] = r["texto"]; continue
    for k, ch in enumerate(split_units(r["texto"]), 1):
        units.append({"id": f"{r['audio'].replace('Audio','A')}-T{r['turno']:02d}-{k}", "audio": r["audio"],
                      "participante": PART[r["audio"]], "turno": r["turno"],
                      "pregunta": last_q.get(r["audio"], ""), "texto": ch, "palabras": len(ch.split())})
(OUT / "unidades.json").write_text(json.dumps(units, ensure_ascii=False, indent=1), encoding="utf-8")
print("unidades:", len(units), "| >=4 palabras:", sum(u["palabras"] >= 4 for u in units))
