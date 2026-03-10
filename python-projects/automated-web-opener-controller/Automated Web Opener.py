import webbrowser
import sys


URLS = {
    "works":["www.google.com"],
    "personal":["www.youtube.com","www.spotify.com","www.github.com"]
}

def open_webpages(urls):
    for url in urls:
        webbrowser.open_new_tab(url)

open_webpages(URLS["personal"])

if __name__ == "___main__":
    set_name = sys.argv[1]
    urls = URLS[set_name]
    open_webpages(urls)