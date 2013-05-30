import datetime
import json
import os
import urllib2

from bbstats.scoreboards.nbascoreboard import NBAScoreboard

STATS_PATH = 'output'

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

def main():    
    #for single_date in daterange(start_date, end_date):
    startdt = datetime.date(2013, 05, 27)
    
    scoreboard = NBAScoreboard(startdt)
    for game in scoreboard:
        ensure_dir(STATS_PATH + '/' + game.gamecode + '/')
        
        localFile = open(STATS_PATH + '/' + game.gamecode + '/boxscore.xml', 'wb')
	localFile.write(game.boxscore_xml)
        localFile.close()
        
        localFile = open(STATS_PATH + '/' + game.gamecode + '/boxscore.json', 'wb')
        localFile.write(game.boxscore_json)
        localFile.close() 
                        
        localFile = open(STATS_PATH + '/' + game.gamecode + '/pbp_all.xml', 'wb')
        localFile.write(game.playbyplay_xml)
        localFile.close()        
                        
        localFile = open(STATS_PATH + '/' + game.gamecode + '/playbyplay.json', 'wb')
        localFile.write(game.playbyplay_json)
        localFile.close()  
                        
        localFile = open(STATS_PATH + '/' + game.gamecode + '/shotchart_all.xml', 'wb')
        localFile.write(game.shotchart_xml)
        localFile.close()                           
          

if __name__ == '__main__':
    main()