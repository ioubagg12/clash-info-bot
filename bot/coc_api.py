"""Clash of Clans API wrapper"""

import requests
from bot.config import COC_API_KEY, COC_API_BASE_URL


class CoCAPI:
    """Handles requests to Clash of Clans API"""

    def __init__(self):
        self.base_url = COC_API_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {COC_API_KEY}",
            "Content-Type": "application/json"
        }

    def get_player_info(self, player_tag: str) -> dict:
        """
        Fetch player information from Clash of Clans API
        
        Args:
            player_tag (str): Player tag (e.g., "#ABC123")
        
        Returns:
            dict: Player information or error message
        """
        try:
            if not player_tag.startswith("#"):
                player_tag = "#" + player_tag
            
            encoded_tag = player_tag.replace("#", "%23")
            
            url = f"{self.base_url}/players/{encoded_tag}"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "data": response.json()
                }
            elif response.status_code == 404:
                return {
                    "success": False,
                    "error": "Player not found. Check your player tag."
                }        
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Request timed out. Try again."
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error: {str(e)}"
            }

    def get_clan_info(self, clan_tag: str) -> dict:
        """
        Fetch clan information from Clash of Clans API
        
        Args:
            clan_tag (str): Clan tag (e.g., "#ABC123")
        
        Returns:
            dict: Clan information or error message
        """
        try:
            if not clan_tag.startswith("#"):
                clan_tag = "#" + clan_tag
            
            encoded_tag = clan_tag.replace("#", "%23")
            
            url = f"{self.base_url}/clans/{encoded_tag}"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "data": response.json()
                }
            elif response.status_code == 404:
                return {
                    "success": False,
                    "error": "Clan not found. Check your clan tag."
                }        
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "Request timed out. Try again."
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error: {str(e)}"
            }

