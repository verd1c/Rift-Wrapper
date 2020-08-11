import requests
from .. import ApiVer as vers


class ApiBase:

    # Base url for all api calls
    base_url = 'api.riotgames.com/'

    api_key: str

    def __init__(self, api_key):
        self.api_key = api_key

    def default_request(self, URL):
        res = requests.get(URL)

        # Check for bad API key
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 403:
            raise Exception("API Key Error")
        else:
            raise Exception("Unknown Error")

    # Import versions \\ignore
    ver_account = vers.lol['account']
    ver_champion_mastery = vers.lol['champion_mastery']
    ver_champion = vers.lol['champion']
    ver_clash = vers.lol['clash']
    ver_league_exp = vers.lol['league_exp']
    ver_league = vers.lol['league']
    ver_status = vers.lol['lol_status']
    ver_match = vers.lol['match']
    ver_spectator = vers.lol['spectator']
    ver_summoner = vers.lol['summoner']

    ver_lor_ranked = vers.lor['ranked']

