class Player:
    """Represents a player in the game
    
    Attributes:
        name (str): The name of the player
        score (int): Player score set to 0 at start
    """
    def __init__(self, name: str):
        """Initializes the Player object.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.score = 0
    
    def add_score(self):
        """Adds one single point to the score"""
        self.score += 1
        
    def reset_score(self):
        """Resets the score back to 0"""
        self.score = 0