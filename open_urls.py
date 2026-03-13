import webbrowser
import threading

# Lista de URLs a abrir
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    # Añade más URLs aquí
]

# Función para abrir una URL en una nueva pestaña
def open_url(url):
    webbrowser.open_new_tab(url)

# Abrir todas las URLs en paralelo
def open_all_urls():
    threads = []
    for url in urls:
        thread = threading.Thread(target=open_url, args=(url,))
        threads.append(thread)
        thread.start()
    
    # Esperar a que todas las pestañas se abran
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    open_all_urls()
