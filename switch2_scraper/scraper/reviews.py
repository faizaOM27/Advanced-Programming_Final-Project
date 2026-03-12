from typing import List
from .client import NintendoLifeClient
from dataclasses import dataclass

@dataclass
class Review:
    game_name: str 
    review_url: str
    score: str 
    review_text: str 

class Game:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
    
class ReviewScraper:
    def __init__(self, client: NintendoLifeClient, max_per_game: int = 10):
        self.client = client
        self.max_per_game = max_per_game
    
    def scrape_review_links(self, game: Game) -> List[Review]:
        soup = self.client.get_page(game.url)
        
        review_links = soup.select('section#reviews .body .ui-listing-body ul.items.style-list li.item-review .item-wrap .info .info-wrap p.heading a')
        
        reviews = []
        for link in review_links[:self.max_per_game]:
            review = Review(
                game_name = game.name,
                review_url = link['href'],
                score = 'N/A',
                review_text = ''
            )
            reviews.append(review)
        
        return reviews
    
    def scrape_full_review(self, review: Review) -> Review:
        soup = self.client.get_page(review.review_url)
        
        score_selectors = [
            'article.review .body.body-text.article-text section.text aside.scoring.rating p.score span.value.accent', 'article.review .body.body-text.article-text aside.scoring.rating p.score span.value.accent', 'article.review aside.scoring.rating p.score span.value.accent'
        ]
        
        review.score = 'N/A'
        for selector in score_selectors:
            score_elem = soup.select_one(selector)
            if score_elem:
                review.score = score_elem.get_text(strip=True)
                break
            
        article = soup.select_one('article.review .body.body-text.article-text')
        if article:
            all_paragraphs = article.select('section.text p')
            
            review_texts = []
            for p in all_paragraphs:
                text = p.get_text(strip=True)
                if len(text) > 20: #skip short/empty text most of the time ads
                    review_texts.append(text)
                    
            full_text = ' '.join(review_texts)
            bad_phrases = [
                'subscribe to', 'youtube', 'youtub', 'nintendo life', '844k', 'follow us', 'advertisement', 'sponsored', 'comment'
            ]
            
            if not any(phrase.lower() in full_text.lower() for phrase in bad_phrases):
                review.review_text = full_text
            else:
                clean_paragraphs = []
                for text in review_texts:
                    if not any(phrase.lower() in text.lower() for phrase in bad_phrases):
                        clean_paragraphs.append(text)
                        
                review.review_text = ' '.join(clean_paragraphs) if clean_paragraphs else 'N/A'
            
        else:
            review.review_text = 'N/A'
    
        return review