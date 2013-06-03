import json
import urllib2

LEAGUES = ['00','10','20']
league_id = {'00':1,'10':2,'20':3}
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
                            #print league, row2[0], min_year, max_year, row2[2], row2[3], row2[4], row2[5], row2[6], row2[7]
                            sql = 'insert into team (league_id, system_id, team_code, min_year, max_year, city, name, abbr, conference, division) values ('
                            sql += str(league_id[league]) + ",'" + str(row2[0]) + "','" + str(row2[7]) + "'," + str(min_year) + "," + str(max_year) + ",'" + str(row2[2]) + "','" + str(row2[3]) + "','" + str(row2[4]) + "','" + str(row2[5]) + "','" + str(row2[6]) + "'"
                            sql += ');'
                            print sql
                        break
            break
