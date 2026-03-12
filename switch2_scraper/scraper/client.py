import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class NintendoLifeClient:
    BASE_URL = "https://www.nintendolife.com"
    
    def __init__(self, delay: float = 1.0):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0"
        })
        self.delay = delay
        
    def get_page(self, path: str) -> BeautifulSoup: #Type hint
        url = urljoin(self.BASE_URL, path)
        resp = self.session.get(url)
        resp.raise_for_status()
        time.sleep(self.delay) #delays in requests to avoid being timed out by the website
        return BeautifulSoup(resp.text, 'lxml')