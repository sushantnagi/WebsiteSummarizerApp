import requests
from bs4 import BeautifulSoup

class Website:
    def __init__(self, url):
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        self.url = url
        self.title = None
        self.text = None
        self.error = None

        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.error = f"❌ Failed to fetch URL: {str(e)}"
            return

        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            self.title = soup.title.string if soup.title else "No title found"

            # Remove noise
            for tag in soup(["script", "style", "img", "input", "footer", "header", "aside"]):
                tag.decompose()

            body = soup.body
            self.text = body.get_text(separator="\n", strip=True) if body else ""
            self.text = ' '.join(self.text.split())  # remove excessive spaces


        except Exception as e:
            self.error = f"❌ Failed to parse HTML: {str(e)}"
