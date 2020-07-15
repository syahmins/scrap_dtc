import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', TITLE='Scrap detik.com')

@app.route("/detikpopuler")
def detikpopuler():
    # tautan yang akan diambil datanya
    html_doc = requests.get('https://www.detik.com/terpopuler')

    # tampilkan isi halaman dalam format html
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    # ambil judul dan gambar berita saja, outputnya masih dalam kode html
    judul_berita = soup.find_all(class_='media__title')
    gambar_berita = soup.find_all(class_='media__image')

    return render_template('index.html', gambar_berita=gambar_berita)


if __name__ == '__main__':
    app.run(debug=True)
