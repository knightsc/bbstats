import urllib2

from bbstats.game import Game

class WNBAGame(Game):
    def __init__(self, game_id, gamecode):
        self.game_id = game_id
        self.gamecode = gamecode
        
        self.__boxscore_xml_url = 'http://www.wnba.com/games/game_component/dynamic/%s/boxscore.xml' % (gamecode)        
        self.__boxscore_json_url = 'http://stats.nba.com/stats/boxscore?GameID=%s&RangeType=0&StartPeriod=0&EndPeriod=0&StartRange=0&EndRange=0' % (game_id)
        self.__playbyplay_xml_url = 'http://www.wnba.com/games/game_component/dynamic/%s/pbp_all.xml' % (gamecode)
        self.__playbyplay_json_url = 'http://stats.nba.com/stats/playbyplay?GameID=%s&StartPeriod=0&EndPeriod=0' % (game_id)
        self.__shotchart_xml_url = 'http://www.wnba.com/games/game_component/dynamic/%s/shotchart_all.xml' % (gamecode)        
        
    def __download(self, url):    
        response = urllib2.urlopen(url)
    	text = response.read()
    	    
    	if 'Page Not Found' in text:
	    text = ""
	    
	return text
	        
    
    @property
    def boxscore_xml(self):
        if not hasattr(self, '__boxscore_xml'):
            self.__boxscore_xml = self.__download(self.__boxscore_xml_url)
        
        return self.__boxscore_xml
        
    @property
    def boxscore_json(self):
        if not hasattr(self, '__boxscore_json'):
            self.__boxscore_json = self.__download(self.__boxscore_json_url)
            
        return self.__boxscore_json
        
    @property
    def playbyplay_xml(self):
        if not hasattr(self, '__playbyplay_xml'):
            self.__playbyplay_xml = self.__download(self.__playbyplay_xml_url)
            
        return self.__playbyplay_xml
        
    @property
    def playbyplay_json(self):
        if not hasattr(self, '__playbyplay_json'):
            self.__playbyplay_json = self.__download(self.__playbyplay_json_url)
                        
        return self.__playbyplay_json
        
    @property
    def shotchart_xml(self):
        if not hasattr(self, '__shotchart_xml'):
            self.__shotchart_xml = self.__download(self.__shotchart_xml_url)
            
        return self.__shotchart_xml