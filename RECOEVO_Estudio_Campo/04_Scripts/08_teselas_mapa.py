"""Descarga las teselas satelitales (Esri World Imagery) de la ruta de vuelo del mapa de la presentación,
para que funcione sin internet cuando se sirve con servidor local. Salida: 05_Presentacion/media/tiles/{z}/{y}/{x}.jpg"""
import math, urllib.request, concurrent.futures as cf
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "05_Presentacion" / "media" / "tiles"
LAT, LON = 4.500941, -74.085905
URL = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"

def tile(z):
    n = 2 ** z
    return (LON + 180) / 360 * n, (1 - math.asinh(math.tan(math.radians(LAT))) / math.pi) / 2 * n

jobs = []
for z in range(0, 20):
    n = 2 ** z; fx, fy = tile(z)
    rx = n if z <= 3 else (6 if z <= 9 else (9 if z <= 16 else 14))   # z0-3: mundo completo (globo)
    ry = n if z <= 3 else (5 if z <= 9 else (8 if z <= 16 else 12))
    xs = range(n) if z <= 3 else range(int(fx) - rx, int(fx) + rx + 1)
    ys = range(n) if z <= 3 else range(max(0, int(fy) - ry), min(n, int(fy) + ry + 1))
    for x in xs:
        for y in ys:
            jobs.append((z, x % n, y))

def get(j):
    z, x, y = j
    p = OUT / str(z) / str(y) / f"{x}.jpg"
    if p.exists(): return 0
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        d = urllib.request.urlopen(urllib.request.Request(URL.format(z=z, x=x, y=y), headers={"User-Agent": "RECOEVO-edu/1.0"}), timeout=30).read()
        p.write_bytes(d); return len(d)
    except Exception:
        return -1

with cf.ThreadPoolExecutor(8) as ex:
    r = list(ex.map(get, jobs))
print(f"teselas: {len(jobs)} · fallidas: {sum(1 for v in r if v < 0)} · MB nuevos: {sum(v for v in r if v > 0) / 1e6:.1f}")

# inventario para la precarga de la presentación
import json, os
lst = sorted(str(p.relative_to(OUT)).replace(os.sep, "/")[:-4] for p in OUT.glob("*/*/*.jpg"))
(OUT / "manifest.json").write_text(json.dumps(lst, separators=(",", ":")), encoding="utf-8")
print("manifest:", len(lst))

# paquete único (una sola descarga en la precarga): pack.bin + pack.json {clave: [offset, largo]}
idx, off = {}, 0
with open(OUT / "pack.bin", "wb") as fo:
    for k in lst:
        b = (OUT / f"{k}.jpg").read_bytes(); fo.write(b); idx[k] = [off, len(b)]; off += len(b)
(OUT / "pack.json").write_text(json.dumps(idx, separators=(",", ":")), encoding="utf-8")
print("pack:", round(off / 1e6, 1), "MB")
