#!/usr/bin/python

from pytrends.request import TrendReq
from time import time, sleep
from random import random, randint
from json import dumps, loads

# name of the file containing our MMO names
namefile = 'names.txt'

# name of the file to write the output. More popular MMOs will be
# located before less popular MMOs.
rankfile = 'rankings.txt'

# Get the trends API
pytrends = TrendReq(hl='en-US', tz=360)

# Google Trends category for MMOs
# See: https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories
#mmocat = 935
mmocat = 105

# Time in seconds to wait before asking Google Trends for something.
# Otherwise, we run out of quota.
spacingDuration = 5
requestSpacing = 5
lastCallTime = 0

# timeframe -- last three months
timeframe = 'today 3-m'

# MMOs to compare written to mmolist
with open(namefile, 'r') as f:
    mmolist = f.read().split('\n')

# Information to improve the search, keyed by game name, with information from suggestions API.
mmokwds = {}

def gaugeInterest(gamedata):
    """
    Return the average interest, as reported by Google Trends, for the game date
    given. This can range from 0 to 100.
    """
    numrows = len(gamedata)
    sum = 0
    for i in range(numrows):
        sum = sum + gamedata[i]
    return sum

def gimme_some_chunks(list):
    'generator to yield four entry chunks from a list'
    for y in range(0, len(list), 4):
        yield list[y:(y+4)]

def compare_games_by_trends(pivot, list):
    'Breaks the game list into four game chunks and sorts them'
    lt = []
    ge = []
    for chunk in gimme_some_chunks(list):
        (nlt, nge) = compare_chunks_by_trends(pivot, chunk)
        lt = lt + nlt
        ge = ge + nge
    return (lt, ge)

def compare_chunks_by_trends(pivot, list):
    """
    calls Trend API with up to four games, and the pivot. Returns list of games
    that are ranked lower and higher.
    """
    global lastCallTime, requestSpacing, spacingDuration
    payload = [pivot] + list
    try:
        now = time()
        waittime = now - lastCallTime
        lastCallTime = now
        if waittime < requestSpacing:
            interval = requestSpacing - waittime + 1
            print ('Sleeping for {} seconds'.format(interval))
            sleep(interval)

        pytrends.build_payload(payload, cat=mmocat, timeframe=timeframe, geo='', gprop='')

        # Manipulate pytrends internal variables to add more parameters to our
        # search terms, based on suggestions.
        reqdict = loads(pytrends.token_payload['req'])
        for compitem in reqdict['comparisonItem']:
            if compitem['keyword'] in mmokwds:
                kwd = mmokwds[compitem['keyword']]
                compitem['keyword'] = kwd['keyword']
                compitem['title'] = kwd['title']
                compitem['name'] = kwd['title']
                compitem['type'] = kwd['type']
        
        pytrends.token_payload['req'] = dumps(reqdict)

        data = pytrends.interest_over_time()

        # build a dictionary keyed by game name with value the average interest
        # over the past 90 days.
        game_trend_table = {}

        for g in payload:
            game_trend_table[g] = gaugeInterest(data[g]) if g in data else 0

        print (game_trend_table)

        lt = []
        ge = []

        # make the LT and GE lists and return them.
        for g in list:
            lt.append(g) if game_trend_table[g] > game_trend_table[pivot] else ge.append(g)

        return (lt, ge)
    except Exception as err:
        print ('Error was {}'.format(err))
        requestSpacing = spacingDuration
        print ('Died with error. Games are {}, {}. Spacing set to {}'.format(pivot, list, requestSpacing))
        sleep(requestSpacing)
        return compare_chunks_by_trends(pivot, list)
     
def qsort(list):
    'implementation of the qsort algorithm'
    if len(list) <= 1: return list
    pivot = list[0]
    (lt, ge) = compare_games_by_trends(pivot, list[1:])
    return qsort(lt) + [pivot] + qsort(ge)

def sortGames():
    'Sort the game list by relative interest'
    return qsort(mmolist)

def rankAndWrite():
    'call sortGames to sort the games, then write the results to a file'
    # This could take awhile...
    l = sortGames()
    with open(rankfile, 'w') as f:
        for game in l:
            print('{}. {}'.format(l.index(game)+1, game), file=f)

def build_kwds():
    'Uses the Suggestions API to try and regularize the game names'
    newmmolist = []
    for g in mmolist:
        sleep(0.5)
        sugs = pytrends.suggestions(g)
        mmokwds[g] = { 'keyword': g, 'title': g, 'type': 'Search term' }
        for sug in sugs:
            # 2010 video game seems to be a category for just FFXIV
            if (sug['title'] not in newmmolist) and \
                    (sug['type'] == '2010 video game' or sug['type'] == 'Online game' or sug['type'] == 'Video game'):
                mmokwds[g]['keyword'] = sug['mid']
                mmokwds[g]['type'] = sug['type']
                mmokwds[g]['title'] = sug['title']
                newmmolist.append(sug['title'])
                print(mmokwds[g])
                break
    return newmmolist

# if calling as main, immediately call rankAndWrite to do the ranking.
if __name__ == "__main__":
    mmolist = build_kwds()
    rankAndWrite()
