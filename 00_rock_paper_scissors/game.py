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
        self.choices = ['rock', 'paper', 'scissors']
    
    
    def add_score(self):
        """Adds one single point to the score"""
        self.score += 1
        
    def reset_score(self):
        """Resets the score back to 0"""
        self.score = 0
    
    def get_choice(self, index):
        return self.choices[index]
        
    def __str__(self):
        return f"Player Name: {self.name} | Score: {self.score}"
        
class Game:
    """Represents a game for the user against the computer
    
    Attributes:
        player1 (Player): player object
        player2 (Player): computer object
    """
    def __init__(self, player: Player, computer):
        """Initialize the game object with two player objects

        Args:
            player (Player): player object
            computer (Player): computer object
        """
        self.player = player
        self.computer = computer
        self.score = {
            player1.name: player1.score,
            player2.name: player2.score,
        }
        
player1 = Player('John')
player2 = Player('computer')

game = Game(player1, player2)
print(game)