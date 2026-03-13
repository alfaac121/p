# main.py
from flask import Flask, jsonify

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
            .mensaje { color: #666; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Abriendo URLs...</h1>
        <p class="mensaje" id="mensaje">Cargando...</p>
        <script>
            fetch('/api/urls')
                .then(r => r.json())
                .then(urls => {
                    urls.forEach(url => window.open(url, '_blank'));
                    document.getElementById('mensaje').textContent = 'Listo. Si el navegador bloqueó ventanas, permite pop-ups para este sitio y recarga.';
                })
                .catch(() => {
                    document.getElementById('mensaje').textContent = 'Error al cargar las URLs.';
                });
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
