import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL dari halaman yang ingin di-scrape
url = "https://books.toscrape.com/"

# Membuat request ke website
response = requests.get(url)

# Parsing konten website dengan Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Mencari semua elemen yang mengandung data buku
books = soup.find_all('article', class_='product_pod')

# List untuk menyimpan data
data = []

# Meng-ekstrak data buku
for book in books:
    title = book.find('h3').find('a')['title']
    price = book.find('p', class_='price_color').text
    stock = book.find('p', class_='instock availability').text.strip()
    data.append({
        'title': title,
        'price': price,
        'stock': stock
    })

# Membuat DataFrame dengan data yang di-scrape
df = pd.DataFrame(data)

# Menyimpan data ke dalam file CSV
df.to_csv('/home/dzikri/Desktop/DE/scrapping/books.csv', index=False)

print("Data telah disimpan ke file books.csv")

