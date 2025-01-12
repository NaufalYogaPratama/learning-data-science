import requests
from bs4 import BeautifulSoup

# Fungsi untuk mengunduh halaman web dan memparsing HTML
def parse_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Fungsi untuk mengekstrak informasi dari halaman web
def extract_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        links.append(a_tag['href'])
    return links

# Fungsi untuk mengekstrak informasi artikel
def extract_article(soup):
    title = soup.find('h1')
    content = soup.find('div', class_='article-content')
    if title and content:
        return title.get_text(), content.get_text()
    else:
        return None, None

# URL untuk menguji
url = "https://grafana.com/"

# Mem-parsing halaman
soup = parse_page(url)

# Mengekstrak semua link
links = extract_links(soup)
print(f"All Links: {links}")

# Mengekstrak artikel (jika ada)
title, content = extract_article(soup)
if title and content:
    print(f"Title: {title}")
    print(f"Content: {content[:300]}...")  # Tampilkan potongan pertama dari artikel
else:
    print("Artikel tidak ditemukan.")
