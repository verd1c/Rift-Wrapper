import requests

from .ApiBase.api import (
    APIKeyError,
    RegionError,
    LolAPI,
    LorAPI
)


class LolWrapper:

    # Default region is EUW
    region = 'euw1'

    # Cache
    last_checked_name = None

    # Initializes object with API key
    def __init__(self, api_key=None):
        if api_key is None:
            return

        self.api_key = api_key

        self._league = LolAPI(api_key)
        self._lor = LorAPI(api_key)

        # Future update
        #self._valo = ValoAPI(api_key)
        #self._tft = TFTAPI(api_key)

    account_regions = ['americas', 'asia', 'europe']
    lor_account_regions = ['americas', 'asia', 'europe', 'sea']
    val_regions = ['ap', 'br', 'eu', 'kr', 'latam', 'na']
    game_regions = ['euw1', 'br1', 'eun1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'tr1', 'ru']
    locale = ['ar-AE', 'de-DE', 'en-GB', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'ru-RU', 'th-TH', 'tr-TR', 'vi-VN', 'zh-CN', 'zh-TW']

    def set_region(self, region=None):
        if region is None:
            return

        # Check if region is correct
        if region.lower() in [  'br1',
                                'jp1',
                                'kr',
                                'la1',
                                'la2',
                                'americas', 'na', 'na1',
                                'oc1',
                                'tr1',
                                'ru',
                                'asia',
                                'europe', 'euw1', 'eun1', 'eu'
                                'sea',
                                'ap', 
                                'br', 
                                'kr', 
                                'latam']:
            self.region = region.lower()
        else:
            raise Exception("Region Error")

    #######################
    #- Account Interface -#
    #######################

    # ~ Account v1

    # Returns summoner info given the accoundId
    # Endpoint used -> /riot/account/v1/accounts/by-puuid/{puuid}
    # https://developer.riotgames.com/apis#account-v1/GET_getByPuuid
    def get_account_by_puuid(self, puuid=None):

        if puuid is None or self.region not in self.account_regions:
            return

        return self._league.account_by_puuid(puuid, self.region)

    # Returns summoner info given the accoundId
    # Endpoint used -> /riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}
    # https://developer.riotgames.com/apis#account-v1/GET_getByRiotId
    def get_account_by_riot_id(self, gameName=None, tagLine=None):

        if gameName is None or tagLine is None or self.region not in self.account_regions:
            return

        return self._league.account_by_riot_id(gameName, tagLine, self.region)

    # Returns summoner info given the accoundId
    # Endpoint used -> /riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}
    # https://developer.riotgames.com/apis#account-v1/GET_getActiveShard
    def get_account_by_game_by_puuid(self, game=None, puuid=None):
        if puuid is None or self.region not in self.account_regions:
            return

        if game is None:
            # Default to valorant
            return self._league.account_by_game_by_puuid('val', puuid, self.region)

        return self._league.account_by_game_by_puuid(game, puuid, self.region)

    #################################
    #- League of Legends Interface -#
    #################################

    # ~ Champion Mastery v4

    # Returns all champion mastery for given summonerId
    # Endpoint used -> /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#champion-mastery-v4/GET_getAllChampionMasteries
    def get_all_champion_mastery_by_summonerId(self, summonerId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if summonerId is None:
            return

        return self._league.champion_all_mastery_by_summonerId(summonerId, self.region)

    # Returns champion mastery for championId for summonerId
    # Endpoint used -> /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}
    # https://developer.riotgames.com/apis#champion-mastery-v4/GET_getChampionMastery
    def get_champion_mastery_by_summonerId(self, summonerId=None, championId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if summonerId is None or championId is None:
            return

        return self._league.champion_mastery_by_summonerId(summonerId, championId, self.region)

    # Returns champion scores for summonerId
    # Endpoint used -> /lol/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#champion-mastery-v4/GET_getChampionMasteryScore
    def get_champion_scores_by_summonerId(self, summonerId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if summonerId is None:
            return

        return self._league.champion_scores_by_summonerId(summonerId, self.region)

    # ~ Champion v3

    # Returns free champion rotation for given region
    # Endpoint used -> /lol/platform/v3/champion-rotations
    # https://developer.riotgames.com/apis#champion-v3/GET_getChampionInfo
    def get_free_champion_rotation(self):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        return self._league.free_champion_rotation(self.region)

    # ~ Clash v1

    # Returns a list of active Clash players for a given summoner ID
    # Endpoint used -> /lol/clash/v1/players/by-summoner/{summonerId}
    # https://developer.riotgames.com/apis#clash-v1/GET_getPlayersBySummoner
    def get_clash_players_by_summonerId(self, summonerId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if summonerId is None:
            return

        return self._league.clash_players_by_summonerId(summonerId, self.region)

    # Returns Clash team info by team ID
    # Endpoint used -> /lol/clash/v1/teams/{teamId}
    # https://developer.riotgames.com/apis#clash-v1/GET_getTeamById
    def get_clash_teams_by_teamId(self, teamId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if teamId is None:
            return

        return self._league.clash_players_by_teamIdId(teamId, self.region)

    # Returns a list of active Clash tournaments
    # Endpoint used -> /lol/clash/v1/tournaments
    # https://developer.riotgames.com/apis#clash-v1/GET_getTournaments
    def get_tournaments(self):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        return self._league.tournaments(self.region)

    # Returns a list of Clash tournaments played by team
    # Endpoint used -> /lol/clash/v1/tournaments/by-team/{teamId}
    # https://developer.riotgames.com/apis#clash-v1/GET_getTournamentByTeam
    def get_tournaments_by_teamId(self, teamId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if teamId is None:
            return

        return self._league.tournaments_by_teamId(teamId, self.region)

    # Returns info on a tournament
    # Endpoint used -> /lol/clash/v1/tournaments/{tournamentId}
    # https://developer.riotgames.com/apis#clash-v1/GET_getTournamentById
    def get_tournaments_by_tournamentId(self, tournamentId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if tournamentId is None:
            return

        return self._league.tournaments_by_tournamentId(tournamentId, self.region)

    # ~~~ League EXP v4 ~~~

    # Returns all info on given queue tier and division
    # Endpoint used -> /lol/league-exp/v4/entries/{queue}/{tier}/{division}
    # https://developer.riotgames.com/apis#league-exp-v4/GET_getLeagueEntries
    def get_league_exp_entries(self, queue=None, tier=None, division=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if queue is None or tier is None or division is None:
            return

        return self._league.league_exp_entries(queue, tier, division, self.region)

    # ~~~ League v4 ~~~

    # Returns challenger leagues on given queue
    # Endpoint used -> /lol/league/v4/challengerleagues/by-queue/{queue}
    # https://developer.riotgames.com/apis#league-v4/GET_getChallengerLeague
    def get_challenger_leagues_by_queue(self, queue=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if queue is None:
            return

        return self._league.challenger_leagues_by_queue(queue, self.region)

    # Returns league based on summoner
    # Endpoint used -> /lol/league/v4/entries/by-summoner/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntriesForSummoner
    def get_league_by_summonerId(self, summonerId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if summonerId is None:
            return

        return self._league.league_by_summonerId(summonerId, self.region)

    # Returns league given queue tier and division
    # Endpoint used -> /lol/league/v4/entries/{queue}/{tier}/{division}
    # https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntries
    def get_league(self, queue=None, tier=None, division=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if queue is None or tier is None or division is None:
            return

        return self._league.league(queue, tier, division, self.region)

    # Returns grandmaster leagues on given queue
    # Endpoint used -> /lol/league/v4/grandmasterleagues/by-queue/{queue}
    # https://developer.riotgames.com/apis#league-v4/GET_getGrandmasterLeague
    def get_grandmaster_leagues_by_queue(self, queue=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if queue is None:
            return

        return self._league.grandmaster_leagues_by_queue(queue, self.region)

    # Returns league by id
    # Endpoint used -> /lol/league/v4/leagues/{leagueId}
    # https://developer.riotgames.com/apis#league-v4/GET_getLeagueById
    def get_league_by_leagueId(self, leagueId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if leagueId is None:
            return

        return self._league.league_by_leagueId(leagueId, self.region)

    # Returns master leagues on given queue
    # Endpoint used -> /lol/league/v4/masterleagues/by-queue/{queue}
    # https://developer.riotgames.com/apis#league-v4/GET_getMasterLeague
    def get_master_leagues_by_queue(self, queue=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if queue is None:
            return

        return self._league.master_leagues_by_queue(queue, self.region)

    # ~~~ Status v3 ~~~

    # Returns region status
    # Endpoint used -> /lol/status/v3/shard-data
    # https://developer.riotgames.com/apis#lol-status-v3/GET_getShardData
    def get_status(self):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        return self._league.status(self.region)

    # ~~~ Match v4 ~~~

    # Returns match info by ID
    # Endpoint used -> /lol/match/v4/matches/{matchId}
    # https://developer.riotgames.com/apis#match-v4/GET_getMatch
    def get_match_by_matchId(self, matchId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if matchId is None:
            return

    # Return matchlist by account ID
    # Endpoint used -> /lol/match/v4/matchlists/by-account/{encryptedAccountId}
    # https://developer.riotgames.com/apis#match-v4/GET_getMatchlist
    def get_matchlist_by_accountId(self, accountId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if accountId is None:
            return

    # Returns timelines by match ID
    # Endpoint used -> /lol/match/v4/timelines/by-match/{matchId}
    # https://developer.riotgames.com/apis#match-v4/GET_getMatchTimeline
    def get_timelines_by_matchId(self, matchId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if matchId is None:
            return

    # Returns tournament matches by tournament code
    # Endpoint used -> /lol/match/v4/matches/by-tournament-code/{tournamentCode}/ids
    # https://developer.riotgames.com/apis#match-v4/GET_getMatchIdsByTournamentCode
    def get_match_by_tournamentcode(self, tournamentCode=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if tournamentCode is None:
            return

    # Returns specific tournament match
    # Endpoint used -> /lol/match/v4/matches/{matchId}/by-tournament-code/{tournamentCode}
    # https://developer.riotgames.com/apis#match-v4/GET_getMatchByTournamentCode
    def get_match_by_matchId_tournamentcode(self, matchId=None, tournamentcode=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if matchId is None or tournamentcode is None:
            return

    # ~~~ Spectator v4 ~~~

    # Returns current game info by summonerId
    # Endpoint used -> /lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#spectator-v4/GET_getCurrentGameInfoBySummoner
    def get_current_game_by_summonerId(self, summonerId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if summonerId is None:
            return

        return self._league.current_game_by_summonerId(summonerId, self.region)

    # Returns featured spectator games for region
    # Endpoint used -> /lol/spectator/v4/featured-games
    # https://developer.riotgames.com/apis#spectator-v4/GET_getFeaturedGames
    def get_featured_spectator_games(self):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        return self._league.featured_spectator_games(self.region)

    # ~~~ Summoner v4 ~~~

    # Returns summoner info given the accoundId
    # Endpoint used -> /lol/summoner/v4/summoners/by-account/{encryptedAccountId}
    # https://developer.riotgames.com/apis#summoner-v4/GET_getByAccountId
    def get_summoner_by_accountId(self, accountId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        # Try to get cached last name if no accountId is given
        if accountId is None:
            if self.last_checked_name is not None:
                accountId = self.get_summoner_by_name(self.last_checked_name)['accountId']
            else:
                return
        
        return self._league.summoner_by_accountId(accountId, self.region)

    # Returns summoner info given the name
    # Endpoint used -> /lol/summoner/v4/summoners/by-name/{summonerName}
    # https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerName
    def get_summoner_by_name(self, name=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if name is None:
            return

        # Cache name
        self.last_checked_name = name

        return self._league.summoner_by_name(name, self.region)
        
    # Returns summoner info given the PUUID
    # Endpoint used -> /lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}
    # https://developer.riotgames.com/apis#summoner-v4/GET_getByPUUID
    def get_summoner_by_PUUID(self, puuid=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if puuid is None:
            return

        return self._league.summoner_by_PUUID(puuid, self.region)

    # Returns summoner info given the summonerId
    # Endpoint used -> /lol/summoner/v4/summoners/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerId
    def get_summoner_by_summonerId(self, summonerId=None):
        # Check for bad region
        if self.region not in self.game_regions:
            raise RegionError

        if summonerId is None:
            return

        return self._league.summoner_by_summonerId(summonerId, self.region)

    ###################################
    #- Legends of Runetera Interface -#
    ###################################

    # Returns the ranked leaderboards for Legends of Runetera
    # Endpoint used -> /lor/ranked/v1/leaderboards
    # https://developer.riotgames.com/apis#lor-ranked-v1
    def get_lor_ranked_leaderboards(self, region=None):
        if region not in self.lor_account_regions:
            return

        return self._lor.ranked_leaderboards(region)