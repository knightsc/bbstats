import json
import urllib2

LEAGUES = ['00','10','20']
ALL_TEAMS = 'http://stats.nba.com/stats/commonteamyears?LeagueID=%s'
TEAM_INFO = 'http://stats.nba.com/stats/teaminfocommon?Season=%s&SeasonType=Regular+Season&LeagueID=%s&TeamID=%s'

for league in LEAGUES:
    response = urllib2.urlopen(ALL_TEAMS % (league))
    commonteamyears = json.load(response)

    for result in commonteamyears['resultSets']:
        if result['name'] == 'TeamYears':
            for row in result['rowSet']:
                team_id = row[1]
                min_year = row[2]
                max_year = row[3]
                season = max_year + "-" + max_year[-2:]                
                
                response = urllib2.urlopen(TEAM_INFO % (season, league, team_id))
                teaminfocommon = json.load(response)

                for result2 in teaminfocommon['resultSets']:
                    if result2['name'] == 'TeamInfoCommon':
                        for row2 in result2['rowSet']:
                            print league, row2[0], min_year, max_year, row2[2], row2[3], row2[4], row2[5], row2[6], row2[7]
                        break
            break
