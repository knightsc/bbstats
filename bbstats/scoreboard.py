import abc

class Scoreboard(object):
    """Basic scoreboard. Give it a single date and you can get a list
    of games from that day.
    
    Attributes:
        scoreboard_date: The date of the games
        games: A list of games
        
    Methods:
        refresh(): update the games for the passed in date. Unless
                   you're scoreboard is for today there's no reason
                   to refresh the games are finished.
    """
    
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, scoreboard_date):
        self.scoreboard_date = scoreboard_date
        self.games = []        
        self.refresh()
    
    def __iter__(self):
        """Return an iterator over the list of games for this scoreboard."""    
        return iter(self.games)        
            
    @abc.abstractmethod
    def refresh(self):
        """Get the latest games for the scoreboard dates."""
    