import requests
from bs4 import BeautifulSoup

# tautan yang akan diambil datanya
html_doc = requests.get('https://www.detik.com/terpopuler')

# tampilkan isi halaman dalam format html
soup = BeautifulSoup(html_doc.text, 'html.parser')

# ambil judul dan gambar berita saja, outputnya masih dalam kode html
judul_berita = soup.find_all(class_='media__title')
gambar_berita = soup.find_all(class_='media__image')

# ambil hanya teks judul berita saja
for judul in judul_berita:
    print(judul.text)

for gambar in gambar_berita:
    print(gambar.find('img').get('title'))

# print(judul_berita)
