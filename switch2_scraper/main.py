""" Main script to scrape Switch 2 games and reviews from Nintendo Life """

from scraper.games import GameListScraper
from scraper.reviews import ReviewScraper
from scraper.client import NintendoLifeClient
from data.processors import games_to_df, reviews_to_df, save_reviews

def main():
    # Initliaze components
    client = NintendoLifeClient(delay = 1.0)
    game_scraper = GameListScraper(client)
    review_scraper = ReviewScraper(client)
    
    # Get games
    print('Scraping game lists...')
    all_games = []
    for page in range(1, 7): #6 pages of games at the moment of making it
        games = game_scraper.scrape_browse_page(page)
        all_games.extend(games)
        print(f'Page {page}: {len(games)} games')
        
    games_df = games_to_df(all_games)
    print(f'Total: {len(all_games)} games')
    
    # Get reviews
    print('\nScraping reviews...')
    all_reviews = []
    for game in all_games[:5]:
        reviews = review_scraper.scrape_game_reviews(game.url, game.name)
        all_reviews.extend(reviews)
        print(f'{game.name}: {len(reviews)} reviews')
        
    reviews_df = reviews_to_df(all_reviews)
    save_reviews(reviews_df)
    
    print(f"\nFinal dataset: {len(reviews_df)} reviews from {len(games)} games")

if __name__ == '__main__':
    main()