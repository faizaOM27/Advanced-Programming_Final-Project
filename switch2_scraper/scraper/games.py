from typing import List 
from .client import NintendoLifeClient
from dataclasses import dataclass 

@dataclass
class Game:
    name: str 
    url: str 
    
class GameListScraper:
    def __init__(self, client: NintendoLifeClient):
        self.client = client
        
    def scrape_browse_page(self, page: int = 1) -> List[Game]:
        path = f"nintendo-switch-2/games/browse" + (f"?page={page}" if page > 1 else "")
        soup = self.client.get_page(path)
        
        game_links = soup.find_all('a', href=lambda x: x and '/games/' in x)
        
        games = []
        for link in game_links:
            name = link.get_text(strip=True)
            if name and len(name) > 5 and any(x in name.lower() for x in ['switch 2', 'switch-2']):
                games.append(Game(name=name, url=link['href']))
        
        return games