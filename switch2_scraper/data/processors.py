import pandas as pd 
from typing import List
from scraper.games import Game
from scraper.reviews import Review

def games_to_df(games: List[Game]) -> pd.DataFrame:
    return pd.DataFrame([{
        'name': g.name,
        'url': g.url
    } for g in games])
    
def reviews_to_df(reviews: List[Review]) -> pd.DataFrame:
    return pd.DataFrame([{
        'game_name': r.game_name,
        'review_text': r.text,
        'score': r.score
    } for r in reviews])
    
def save_reviews(df: pd.DataFrame, filename: str = 'switch2_reviews.csv'):
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} reviews to {filename}")