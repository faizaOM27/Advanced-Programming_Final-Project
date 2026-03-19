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
    for page in range(1, 8): #7 pages of games at the moment of making it
        games = game_scraper.scrape_browse_page(page)
        all_games.extend(games)
        print(f'Page {page}: {len(games)} games')
    
    # Convert games to DataFrame for analysis/ export   
    games_df = games_to_df(all_games)
    print(f'Total: {len(all_games)} games')
    
    # Get reviews
    print('\nScraping reviews...')
    all_reviews = []
    for game in all_games:
        print(f'Processing {game.name}...')
        review_links = review_scraper.scrape_review_links(game)
        
        for review_link in review_links:
            full_review = review_scraper.scrape_full_review(review_link)
            all_reviews.append(full_review)
    
    # Convert reviews to structured DataFrame and save   
    reviews_df = reviews_to_df(all_reviews)
    save_reviews(reviews_df)
    
    # Final summary
    print(f"\nFinal dataset: {len(reviews_df)} reviews from {len(games)} games")

if __name__ == '__main__':
    main()