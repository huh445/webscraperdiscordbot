import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.url = "https://news.com.au"
    
    def web_scraper(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.get_text()
    
if __name__ == "__main__":
    print(WebScraper().web_scraper())