import datetime
import json
import urllib2

from bbstats.scoreboard import Scoreboard
from bbstats.nba.nbagame import NBAGame

class NBAScoreboard(Scoreboard):

    _URL = 'http://stats.nba.com/stats/scoreboard?LeagueID=00&gameDate=%s&DayOffset=0'   
        
    def refresh(self):
        scoreboard_url = self._URL % (self.scoreboard_date.strftime('%m/%d/%Y'))            
        response = urllib2.urlopen(scoreboard_url)
        self.__scoreboard = json.load(response)
        
        # loop through games
        for result in self.__scoreboard['resultSets']:
            if result['name'] == 'GameHeader':
                for row in result['rowSet']:
                    g = NBAGame(row[2], row[5])
                    self.games.append(g)
                    
                break
            