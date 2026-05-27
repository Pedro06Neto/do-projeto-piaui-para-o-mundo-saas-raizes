import http.server
import json
import os
import urllib.request


def load_dotenv(path):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"\'"')
            if key and key not in os.environ:
                os.environ[key] = value

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

GROQ_KEY = os.getenv('GROQ_KEY')
GROQ_URL = 'https://api.groq.com/openai/v1/chat/completions'
PORT = int(os.getenv('PORT', 3000))

MIME = {
    '.html': 'text/html; charset=utf-8',
    '.js':   'application/javascript',
    '.css':  'text/css',
    '.png':  'image/png',
    '.ico':  'image/x-icon',
    '.wasm': 'application/wasm',
    '.pck':  'application/octet-stream',
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"  {args[0]} {args[1]}")

    def do_POST(self):
        if self.path != '/api/openai':
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length))
        if 'model' not in body:
            body['model'] = 'llama-3.3-70b-versatile'

        payload = json.dumps(body).encode('utf-8')
        req = urllib.request.Request(
            GROQ_URL,
            data=payload,
            headers={
                'Authorization': f'Bearer {GROQ_KEY}',
                'Content-Type': 'application/json',
                'User-Agent': 'groq-python/0.11.0',
            },
            method='POST',
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                response_bytes = resp.read()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(response_bytes)
        except urllib.error.HTTPError as e:
            body_err = e.read().decode('utf-8', errors='replace')
            try:
                msg = json.loads(body_err).get('error', {}).get('message', body_err[:300])
            except json.JSONDecodeError:
                msg = body_err[:300]
            self._json_error(e.code, msg)
        except urllib.error.URLError as e:
            self._json_error(502, f'Erro ao conectar com a API: {e.reason}')
        except TimeoutError:
            self._json_error(504, 'Tempo limite excedido. Tente novamente.')

    def _json_error(self, code, msg):
        body = json.dumps({'error': {'message': msg}}).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url_path = self.path.split('?')[0]
        if url_path == '/':
            url_path = '/raizes_do_piaui_piaui_world_roteiro_ia (1).html'

        # Impede path traversal (ex: /../../../etc/passwd)
        file_path = os.path.realpath(os.path.join(BASE_DIR, url_path.lstrip('/')))
        if not file_path.startswith(BASE_DIR):
            self.send_response(403)
            self.end_headers()
            return

        ext = os.path.splitext(file_path)[1]
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            self.send_response(200)
            self.send_header('Content-Type', MIME.get(ext, 'application/octet-stream'))
            self.end_headers()
            self.wfile.write(data)
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    if not GROQ_KEY:
        print('ERRO: variável GROQ_KEY não encontrada no .env')
        raise SystemExit(1)
    print(f'Servidor rodando em http://localhost:{PORT}')
    print('Pressione Ctrl+C para parar.\n')
    http.server.HTTPServer(('', PORT), Handler).serve_forever()
