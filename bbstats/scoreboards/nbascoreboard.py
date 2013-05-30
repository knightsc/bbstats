import datetime
import json
import urllib2

from bbstats.game import Game

class NBAScoreboard(object):
    """In general NBA has the best support
    
    Attributes:
        scoreboard_date: The date of the games
        games: A list of games
    """

    URL = 'http://stats.nba.com/stats/scoreboard?LeagueID=00&gameDate=%s&DayOffset=0'
    
    def __init__(self, scoreboard_date):
        self.scoreboard_date = scoreboard_date
        self.games = []
        self.__scoreboard = None
        self.__load_scoreboard()
    
    def __iter__(self):
        return iter(self.games)
        
    def __load_scoreboard(self):
        scoreboard_url = self.URL % (self.scoreboard_date.strftime('%m/%d/%Y'))            
        response = urllib2.urlopen(scoreboard_url)
        self.__scoreboard = json.load(response)
        
        # loop through games
        for result in self.__scoreboard['resultSets']:
            if result['name'] == 'GameHeader':
                for row in result['rowSet']:
                    g = Game(row[2], row[5])
                    self.games.append(g)
                    
                break
            