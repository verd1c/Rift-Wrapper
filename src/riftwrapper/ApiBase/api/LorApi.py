import requests
from ..ApiBase import ApiBase

class LorAPI(ApiBase):

    # ~ Ranked v1

    # Returns the ranked leaderboards for Legends of Runetera
    # Endpoint used -> /lor/ranked/v1/leaderboards
    # https://developer.riotgames.com/apis#lor-ranked-v1
    def ranked_leaderboards(self, region):

        URL = 'https://' + region + '.api.riotgames.com/lor/ranked/' + self.ver_lor_ranked + 'leaderboards?api_key=' + self.api_key
        return self.default_request(URL)