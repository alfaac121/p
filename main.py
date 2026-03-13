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
        <p class="mensaje" id="mensaje">Haz clic en el botón para abrir todas las URLs. Si el navegador las bloquea, usa los enlaces de abajo.</p>
        <button onclick="openUrls()">Abrir URLs</button>
        <div id="enlaces" style="display:none; margin-top:24px; text-align:left; max-width:400px; margin-left:auto; margin-right:auto;"></div>
        <script>
            function openUrls() {
                var mensaje = document.getElementById('mensaje');
                var divEnlaces = document.getElementById('enlaces');
                mensaje.textContent = 'Abriendo...';
                divEnlaces.style.display = 'none';
                divEnlaces.innerHTML = '';
                fetch('/api/urls')
                    .then(r => r.json())
                    .then(urls => {
                        var bloqueado = false;
                        urls.forEach(function(url) {
                            var w = window.open(url, '_blank');
                            if (!w) bloqueado = true;
                        });
                        mensaje.textContent = bloqueado
                            ? 'El navegador bloqueó algunas. Permite pop-ups (icono en la barra de direcciones) o haz clic en cada enlace de abajo:'
                            : 'Listo.';
                        urls.forEach(function(url, i) {
                            var a = document.createElement('a');
                            a.href = url;
                            a.target = '_blank';
                            a.rel = 'noopener';
                            a.textContent = (i + 1) + '. ' + url.replace(/^https?:\\/\\//, '');
                            a.style.display = 'block';
                            a.style.marginTop = '8px';
                            a.style.color = '#1a73e8';
                            divEnlaces.appendChild(a);
                        });
                        divEnlaces.style.display = 'block';
                    })
                    .catch(function() {
                        mensaje.textContent = 'Error al cargar las URLs.';
                    });
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
