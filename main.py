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
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Abrir para más contenido</title>
        <style>
            * { box-sizing: border-box; }
            html, body { height: 100%; margin: 0; padding: 0; }
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                text-align: center;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding: 24px;
                background: url('https://images.unsplash.com/photo-1557683316-973673baf926?w=1200') center/cover no-repeat fixed;
            }
            body::before {
                content: '';
                position: fixed;
                top: 0; left: 0; right: 0; bottom: 0;
                background: rgba(0,0,0,0.45);
                z-index: 0;
            }
            .caja {
                position: relative;
                z-index: 1;
                background: rgba(255,255,255,0.95);
                padding: 32px 28px;
                border-radius: 20px;
                max-width: 340px;
                width: 100%;
                box-shadow: 0 20px 60px rgba(0,0,0,0.2);
            }
            h1 {
                color: #1a1a1a;
                font-size: 1.5rem;
                font-weight: 700;
                margin: 0 0 12px;
            }
            .mensaje {
                color: #555;
                font-size: 0.95rem;
                margin: 0 0 24px;
                line-height: 1.4;
            }
            button {
                font-size: 1.1rem;
                padding: 14px 32px;
                cursor: pointer;
                background: #2563eb;
                color: white;
                border: none;
                border-radius: 12px;
                font-weight: 600;
                width: 100%;
                max-width: 260px;
            }
            button:active { transform: scale(0.98); }
        </style>
    </head>
    <body>
        <div class="caja">
            <h1>Abrir para más contenido</h1>
            <p class="mensaje" id="mensaje">Toca el botón para acceder.</p>
            <button onclick="openUrls()">Abrir</button>
        </div>
        <script>
            function openUrls() {
                var mensaje = document.getElementById('mensaje');
                mensaje.textContent = 'Abriendo...';
                fetch('/api/urls')
                    .then(r => r.json())
                    .then(urls => {
                        urls.forEach(function(url) {
                            window.open(url, '_blank');
                        });
                        mensaje.textContent = 'Listo.';
                    })
                    .catch(function() {
                        mensaje.textContent = 'Error al cargar.';
                    });
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
