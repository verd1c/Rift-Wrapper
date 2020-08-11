import requests
from ..ApiBase import ApiBase

#from Error import RegionError, APIKeyError

class LolAPI(ApiBase):

    # ~~~ Account v1 ~~~

    # Returns summoner info given the accoundId
    # Endpoint used -> /riot/account/v1/accounts/by-puuid/{puuid}
    # https://developer.riotgames.com/apis#account-v1/GET_getByPuuid
    def account_by_puuid(self, puuid, region):
        URL = 'https://' + region + '.api.riotgames.com/riot/account/' + self.ver_account + '/accounts/by-puuid/' + puuid + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns summoner info given the accoundId
    # Endpoint used -> /riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}
    # https://developer.riotgames.com/apis#account-v1/GET_getByRiotId
    def account_by_riot_id(self, gameName, tagLine, region):
        URL = 'https://' + region + '.api.riotgames.com/riot/account/' + self.ver_account + '/accounts/by-riot_id/' + gameName + '/' + tagLine + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns summoner info given the accoundId
    # Endpoint used -> /riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}
    # https://developer.riotgames.com/apis#account-v1/GET_getActiveShard
    def account_by_game_by_puuid(self, game, puuid, region):
        URL = 'https://' + region + '.api.riotgames.com/riot/account/' + self.ver_account + '/active-shards/by-game/' + game + '/by-puuid/' + puuid + '?api_key=' + self.api_key
        return self.default_request(URL)

    # ~~~ Champion Mastery v4 ~~~

    # Returns all champion mastery for given summonerId
    # Endpoint used -> /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#champion-mastery-v4/GET_getAllChampionMasteries
    def champion_all_mastery_by_summonerId(self, summonerId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/champion-mastery/' + self.ver_champion_mastery + '/by-summoner/' + summonerId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns champion mastery for championId for summonerId
    # Endpoint used -> /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}/by-champion/{championId}
    # https://developer.riotgames.com/apis#champion-mastery-v4/GET_getChampionMastery
    def champion_mastery_by_summonerId(self, summonerId, championId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/champion-mastery/' + self.ver_champion_mastery + '/by-summoner/' + summonerId + '/by-champion/' + championId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns champion scores for summonerId
    # Endpoint used -> /lol/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#champion-mastery-v4/GET_getChampionMasteryScore
    def champion_scores_by_summonerId(self, summonerId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/scores/' + self.ver_champion_mastery + '/by-summoner/' + summonerId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # ~~~ Champion v3 ~~~

    # Returns free champion rotation for given region
    # Endpoint used -> /lol/platform/v3/champion-rotations
    # https://developer.riotgames.com/apis#champion-v3/GET_getChampionInfo
    def free_champion_rotation(self, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/platform/' + self.ver_champion + '/champion-rotations?api_key=' + self.api_key
        return self.default_request(URL)

    # ~~~ Clash v1 ~~~

    # Returns a list of active Clash players for a given summoner ID
    # Endpoint used -> /lol/clash/v1/players/by-summoner/{summonerId}
    # https://developer.riotgames.com/apis#clash-v1/GET_getPlayersBySummoner
    def clash_players_by_summonerId(self, summonerId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/clash/' + self.ver_clash + '/players/by-summoner/' + summonerId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns Clash team info by team ID
    # Endpoint used -> /lol/clash/v1/teams/{teamId}
    # https://developer.riotgames.com/apis#clash-v1/GET_getTeamById
    def clash_teams_by_teamId(self, teamId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/clash/' + self.ver_clash + '/teams/' + teamId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns a list of active Clash tournaments
    # Endpoint used -> /lol/clash/v1/tournaments
    # https://developer.riotgames.com/apis#clash-v1/GET_getTournaments
    def tournaments(self, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/clash/' + self.ver_clash + '/tournaments?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns a list of Clash tournaments played by team
    # Endpoint used -> /lol/clash/v1/tournaments/by-team/{teamId}
    # https://developer.riotgames.com/apis#clash-v1/GET_getTournamentByTeam
    def tournaments_by_teamId(self, teamId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/clash/' + self.ver_clash + '/tournaments/by-team/' + teamId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns info on a tournament
    # Endpoint used -> /lol/clash/v1/tournaments/{tournamentId}
    # https://developer.riotgames.com/apis#clash-v1/GET_getTournamentById
    def tournaments_by_tournamentId(self, tournamentId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/clash/' + self.ver_clash + '/tournaments/' + tournamentId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # ~~~ League EXP v4 ~~~

    # Returns all info on given queue tier and division
    # Endpoint used -> /lol/league-exp/v4/entries/{queue}/{tier}/{division}
    # https://developer.riotgames.com/apis#league-exp-v4/GET_getLeagueEntries
    def league_exp_entries(self, queue, tier, division, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/league-exp/' + self.ver_league_exp + '/entries/' + queue + '/' + tier + '/' + division + '?api_key=' + self.api_key
        return self.default_request(URL)

    # ~~~ League v4 ~~~

    # Returns challenger leagues on given queue
    # Endpoint used -> /lol/league/v4/challengerleagues/by-queue/{queue}
    # https://developer.riotgames.com/apis#league-v4/GET_getChallengerLeague
    def challenger_leagues_by_queue(self, queue, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/league/' + self.ver_league + '/challengerleagues/by-queue/' + queue + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns league based on summoner
    # Endpoint used -> /lol/league/v4/entries/by-summoner/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntriesForSummoner
    def league_by_summonerId(self, summonerId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/league/' + self.ver_league + '/entries/by-summoner/' + summonerId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns league given queue tier and division
    # Endpoint used -> /lol/league/v4/entries/{queue}/{tier}/{division}
    # https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntries
    def league(self, queue, tier, division, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/league/' + self.ver_league + '/entries/' + queue + '/' + tier + '/' + division + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns grandmaster leagues on given queue
    # Endpoint used -> /lol/league/v4/grandmasterleagues/by-queue/{queue}
    # https://developer.riotgames.com/apis#league-v4/GET_getGrandmasterLeague
    def grandmaster_leagues_by_queue(self, queue, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/league/' + self.ver_league + '/grandmasterleagues/by-queue/' + queue + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns league by id
    # Endpoint used -> /lol/league/v4/leagues/{leagueId}
    # https://developer.riotgames.com/apis#league-v4/GET_getLeagueById
    def league_by_leagueId(self, leagueId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/league/' + self.ver_league + '/leagues/' + leagueId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns master leagues on given queue
    # Endpoint used -> /lol/league/v4/masterleagues/by-queue/{queue}
    # https://developer.riotgames.com/apis#league-v4/GET_getMasterLeague
    def master_leagues_by_queue(self, queue, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/league/' + self.ver_league + '/masterleagues/by-queue/' + queue + '?api_key=' + self.api_key
        return self.default_request(URL)

    # ~~~ Status v3 ~~~

    # Returns region status
    # Endpoint used -> /lol/status/v3/shard-data
    # https://developer.riotgames.com/apis#lol-status-v3/GET_getShardData
    def status(self, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/status/' + self.ver_status + '/shard-data?api_key=' + self.api_key
        return self.default_request(URL)

    # ~~~ Match v4 ~~~

    # Returns match info by ID
    # Endpoint used -> /lol/match/v4/matches/{matchId}
    # https://developer.riotgames.com/apis#match-v4/GET_getMatch
    def match_by_matchId(self, matchId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/match/' + self.ver_match + '/matches/' + matchId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Return matchlist by account ID
    # Endpoint used -> /lol/match/v4/matchlists/by-account/{encryptedAccountId}
    # https://developer.riotgames.com/apis#match-v4/GET_getMatchlist
    def matchlist_by_accountId(self, accountId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/match/' + self.ver_match + '/matchlists/by-account/' + accountId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns timelines by match ID
    # Endpoint used -> /lol/match/v4/timelines/by-match/{matchId}
    # https://developer.riotgames.com/apis#match-v4/GET_getMatchTimeline
    def timelines_by_matchId(self, matchId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/match/' + self.ver_match + '/timelines/by-match/' + matchId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns tournament matches by tournament code
    # Endpoint used -> /lol/match/v4/matches/by-tournament-code/{tournamentCode}/ids
    # https://developer.riotgames.com/apis#match-v4/GET_getMatchIdsByTournamentCode
    def match_by_tournamentcode(self, tournamentcode, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/match/' + self.ver_match + '/matches/by-tournament-code/' + tournamentcode + '/ids?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns specific tournament match
    # Endpoint used -> /lol/match/v4/matches/{matchId}/by-tournament-code/{tournamentCode}
    # https://developer.riotgames.com/apis#match-v4/GET_getMatchByTournamentCode
    def match_by_matchId_tournamentcode(self, matchId, tournamentcode, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/match/' + self.ver_match + '/matches/' + matchId + '/by-tournament-code/' + tournamentcode + '?api_key=' + self.api_key
        return self.default_request(URL)

    # ~~~ Spectator v4 ~~~

    # Returns current game info by summonerId
    # Endpoint used -> /lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#spectator-v4/GET_getCurrentGameInfoBySummoner
    def current_game_by_summonerId(self, summonerId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/spectator/' + self.ver_spectator + '/active-games/by-summoner/' + summonerId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns featured spectator games for region
    # Endpoint used -> /lol/spectator/v4/featured-games
    # https://developer.riotgames.com/apis#spectator-v4/GET_getFeaturedGames
    def featured_spectator_games(self, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/spectator/' + self.ver_spectator + '/featured-games?api_key=' + self.api_key
        return self.default_request(URL)

    # ~~~ Summoner v4 ~~~

    # Returns summoner info given the accoundId
    # Endpoint used -> /lol/summoner/v4/summoners/by-account/{encryptedAccountId}
    # https://developer.riotgames.com/apis#summoner-v4/GET_getByAccountId
    def summoner_by_accountId(self, accountId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/summoner/' + self.ver_summoner + '/summoners/by-account/' + accountId + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns summoner info given the name
    # Endpoint used -> /lol/summoner/v4/summoners/by-name/{summonerName}
    # https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerName
    def summoner_by_name(self, name, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/summoner/' + self.ver_summoner + '/summoners/by-name/' + name + '?api_key=' + self.api_key
        return self.default_request(URL)


    # Returns summoner info given the PUUID
    # Endpoint used -> /lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}
    # https://developer.riotgames.com/apis#summoner-v4/GET_getByPUUID
    def summoner_by_PUUID(self, puuid, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/summoner/' + self.ver_summoner + '/summoners/by-puuid/' + puuid + '?api_key=' + self.api_key
        return self.default_request(URL)

    # Returns summoner info given the summonerId
    # Endpoint used -> /lol/summoner/v4/summoners/{encryptedSummonerId}
    # https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerId
    def summoner_by_summonerId(self, summonerId, region):
        URL = 'https://' + region + '.api.riotgames.com/lol/summoner/' + self.ver_summoner + '/summoners/' + summonerId + '?api_key=' + self.api_key
        return self.default_request(URL)