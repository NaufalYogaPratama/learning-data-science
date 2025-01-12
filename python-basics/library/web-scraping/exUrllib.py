import urllib.request
import urllib.error
import json
from urllib.parse import urlparse, parse_qs

# Fungsi untuk mengunduh halaman web
def download_page(url):
    try:
        response = urllib.request.urlopen(url)
        page_content = response.read()
        return page_content
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

# Fungsi untuk menganalisis query parameters dari URL
def analyze_url(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params

# Mengunduh halaman web dan menganalisis URL
url = "https://grafana.com/"
page_content = download_page(url)

if page_content:
    print("Halaman web berhasil diunduh.")

# Menganalisis query params dari URL
query_params = analyze_url(url)
print(f"Query parameters: {json.dumps(query_params, indent=2)}")
