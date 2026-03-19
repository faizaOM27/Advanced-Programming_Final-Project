from typing import List 
from .client import NintendoLifeClient
from dataclasses import dataclass 

# Represents a single game entry scraped from NintendoLife
@dataclass
class Game:
    name: str 
    url: str 
    
# Scrapes lists of Nintendo Switch 2 games from NintendoLife browse pages
class GameListScraper:
    def __init__(self, client: NintendoLifeClient):
        self.client = client
        
    def scrape_browse_page(self, page: int = 1) -> List[Game]:
        # Constructing the browse page path
        path = f"nintendo-switch-2/games/browse" + (f"?page={page}" if page > 1 else "")
        soup = self.client.get_page(path)
        
        game_links = soup.find_all('a', href=lambda x: x and '/games/' in x)
        
        games = []
        for link in game_links:
            name = link.get_text(strip=True)
            
            # Filtering to ensure the name mentions Switch 2
            if name and len(name) > 5 and any(x in name.lower() for x in ['switch 2', 'switch-2']):
                games.append(Game(name=name, url=link['href']))
        
        return games