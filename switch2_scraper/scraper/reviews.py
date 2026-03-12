from typing import List
from .client import NintendoLifeClient
from dataclasses import dataclass

@dataclass
class Review:
    game_name: str 
    text: str 
    score: str
    
class ReviewScraper:
    def __init__(self, client: NintendoLifeClient, max_per_game: int = 10):
        self.client = client
        self.max_per_game = max_per_game
        
    def scrape_game_reviews(self, game_url: str, game_name: str) -> List[Review]: #Type Hint
        soup = self.client.get_page(game_url)
        
        # UPDATE THESE SELECTORS after inspecting game pages
        review_divs = soup.find_all('div', class_='review-item')
        reviews = []
        
        for div in review_divs[:self.max_per_game]:
            text_el = div.find('p', class_='review-text')
            score_el = div.find('span', class_='score')
            if text_el and score_el:
                reviews.append(Review(
                    game_name=game_name,
                    text=text_el.get_text(strip=True)[:500],
                    score=score_el.get_text(strip=True)
                ))
        return reviews