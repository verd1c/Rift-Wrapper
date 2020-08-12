# RiftWrapper v1.2

RiftWrapper is a simple wrapper for the [Riot Games API](https://developer.riotgames.com/docs/portal) written in python. You can check the currently supported APIs [here](https://github.com/verd1c/Rift-Wrapper#supported-api-versions).

## Installation

To install using pip do:

```sh
pip install riftwrapper
```

## Usage

In order to use RiftWrapper, you are going to need your personal API Key from Riot, which you can get from [here](https://developer.riotgames.com/).

After importing LolWrapper, you can use it as such with your own API Key:
```sh
from riftwrapper import LolWrapper

rw = LolWrapper('<your-api-key>')
```

Your API Key will be binded to rw, but you can always change your desired region as such:

```sh
rw.set_region('eun1')
```

Keep in mind that the default region is 'euw1'.

Now that we've set the region as eune, we can grab the info for a player in eune and print it:

```sh
my_summoner = rw.get_summoner_by_name('qwop')
print(my_summoner)
```

All return values are in json dictionary format, so we can grab and print the summoner's level, for example, like this:

```sh
print(my_summoner['summonerLevel'])
```

Or you can also get a list of the current free champion rotation:

```sh
free_champion_rotation = rw.get_free_champion_rotation()
print(free_champion_rotation)
```

## Supported API Versions

| API |
| ------ |
| [Account v1](https://developer.riotgames.com/apis#account-v1) |
| [Champion Mastery v4](https://developer.riotgames.com/apis#champion-mastery-v4) |
| [Champion v3](https://developer.riotgames.com/apis#champion-v3) |
| [Clash v1](https://developer.riotgames.com/apis#clash-v1) |
| [League Exp v4](https://developer.riotgames.com/apis#league-exp-v4) |
| [League v4](https://developer.riotgames.com/apis#league-v4) |
| [LoL Status v3](https://developer.riotgames.com/apis#lol-status-v3) |
| [Match v4](https://developer.riotgames.com/apis#match-v4) |
| [Spectator v4](https://developer.riotgames.com/apis#spectator-v4) |
| [Summoner v4](https://developer.riotgames.com/apis#summoner-v4) |
| [LoR Ranked v1](https://developer.riotgames.com/apis#lor-ranked-v1) |

## Future Work

Version 1.3 is to include support for the TFT and Valorant API.

## Changelog

  - v1.2 Added support for PyPi
  - v1.1 Removed useless GET URL prints
  - v1.0 Initial release
