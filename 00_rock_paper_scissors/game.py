import random

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
    
    def get_choice(self, index) -> str:
        """Take index as an argument and return rock, paper, or scissors"""
        return self.choices[index]
        
    def __str__(self):
        """Returns string representation of Player objects"""
        return f"Player Name: {self.name} | Score: {self.score}"

class Computer(Player):
    """Represents computer player object

    Attributes:
        Player (Player): Inherit properties from the Player class
    """
    def __init__(self):
        """Initializes Computer object by creating a Player Object
        with the name computer
        """
        super().__init__("computer")
        
    def get_choice(self) -> str:
        """Return a random choice from rock, paper, or scissors"""
        index = random.randint(0, 2)
        return super().get_choice(index)
        
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
        
player1 = Player('john')
player2 = Computer()

# game = Game(player1, player2)
# print(game)