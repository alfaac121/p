# main.py
from flask import Flask, jsonify, redirect

app = Flask(__name__)

# Lista de URLs (se abren todas a la vez en el navegador del usuario)
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.youtube.com",
    "https://www.wikipedia.org",
    "https://www.reddit.com",
    "https://www.twitter.com",
    "https://www.linkedin.com",
    "https://www.amazon.com",
    "https://www.netflix.com",
    "https://www.instagram.com",
    "https://www.medium.com",
    "https://www.spotify.com",
    "https://www.notion.so",
    "https://www.discord.com",
    "https://www.twitch.tv",
    "https://www.ebay.com",
    "https://www.zoom.us",
]

@app.route('/api/urls')
def get_urls():
    """Devuelve la lista de URLs para que el frontend las abra."""
    return jsonify(urls)

@app.route('/redirect/<path:url>')
def redirect_to(url):
    """Proxy de navegación: redirige a la URL final (a veces evita bloqueos)."""
    return redirect(url, code=302)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Auto Open</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 40px; }
            h1 { color: #333; }
            .mensaje { color: #666; margin-top: 16px; }
            button {
                font-size: 18px;
                padding: 12px 24px;
                cursor: pointer;
                background: #1a73e8;
                color: white;
                border: none;
                border-radius: 8px;
            }
            button:hover { background: #1557b0; }
        </style>
    </head>
    <body>
        <h1>Auto Open</h1>
        <p class="mensaje" id="mensaje">Haz clic en el botón para abrir todas las URLs en nuevas pestañas.</p>
        <button onclick="openUrls()">Abrir URLs</button>
        <script>
            function openUrls() {
                document.getElementById('mensaje').textContent = 'Abriendo...';
                fetch('/api/urls')
                    .then(r => r.json())
                    .then(urls => {
                        let bloqueado = false;
                        urls.forEach(url => {
                            const newWindow = window.open('/redirect/' + encodeURIComponent(url), '_blank');
                            if (!newWindow) {
                                bloqueado = true;
                            }
                        });
                        document.getElementById('mensaje').textContent = bloqueado
                            ? 'Algunas ventanas se bloquearon. Por favor, permite pop-ups para este sitio y vuelve a pulsar el botón.'
                            : 'Listo.';
                        if (bloqueado) {
                            alert('Por favor, habilita las ventanas emergentes para este sitio y vuelve a pulsar "Abrir URLs".');
                        }
                    })
                    .catch(() => {
                        document.getElementById('mensaje').textContent = 'Error al cargar las URLs.';
                    });
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
