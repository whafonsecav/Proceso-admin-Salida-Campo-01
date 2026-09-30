"""Servidor local de la presentación, con soporte de rangos HTTP (necesario para saltar al minuto exacto de cada audio).
Uso: python servidor.py  →  abre http://localhost:8765"""
import http.server, os, re, sys, webbrowser, threading

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def log_message(self, *a): pass
    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes"); self.send_header("Cache-Control", "no-cache"); super().end_headers()
    def send_head(self):
        self._remaining = None  # la conexión se reutiliza (HTTP/1.1): no arrastrar el rango de la solicitud anterior
        rng = self.headers.get("Range")
        path = self.translate_path(self.path)
        if not rng or os.path.isdir(path) or not os.path.exists(path):
            return super().send_head()
        m = re.match(r"bytes=(\d*)-(\d*)", rng); size = os.path.getsize(path)
        start = int(m.group(1) or 0); end = int(m.group(2)) if m.group(2) else size - 1
        end = min(end, size - 1)
        f = open(path, "rb"); f.seek(start)
        self.send_response(206); self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}"); self.send_header("Content-Length", str(end - start + 1))
        self.end_headers(); self._remaining = end - start + 1
        return f
    def copyfile(self, src, dst):
        rem = getattr(self, "_remaining", None)
        if rem is None: return super().copyfile(src, dst)
        while rem > 0:
            b = src.read(min(65536, rem))
            if not b: break
            dst.write(b); rem -= len(b)

if __name__ == "__main__":
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}/"
    print(f"Presentación RECOEVO en {url}  (Ctrl+C para cerrar)")
    if "--no-browser" not in sys.argv: threading.Timer(1, lambda: webbrowser.open(url)).start()
    srv.serve_forever()
