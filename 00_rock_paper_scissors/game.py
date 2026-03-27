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
    def __init__(self, player: Player, computer: Computer):
        """Initialize the game object with two player objects

        Args:
            player (Player): player object
            computer (Player): computer object
        """
        self.player = player
        self.computer = computer
        self.tie = 0
        
    def start_match(self, index: int):
        """Starts match by getting player and computer choices"""
        player_choice = self.player.get_choice(index)
        computer_choice = self.computer.get_choice()
        winner = self.get_winner(player_choice, computer_choice)
        self.update_score(winner)
        print(player_choice, computer_choice, winner)
        print(self.get_score())
        
    def get_score(self):
        """Return Player and Computer scores in strings"""
        return (f"Player: {self.player.score} "
                f"Computer: {self.computer.score} "
                f"Tie: {self.tie}")
    
    def get_winner(self, player_choice, computer_choice) -> str:
        """Compares player and computer choices and return winner as str"""
        winner = "computer"
        
        if ((player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")):
            winner = "player"
        elif player_choice == computer_choice:
            winner = "tie"
            
        return winner

    def update_ties(self):
        """Keep track of ties separately since it's not a player"""
        self.tie += 1
    
    def update_score(self, winner: str):
        """Update score based on winner"""
        if winner == "player":
            self.player.add_score()
        elif winner == "computer":
            self.computer.add_score()
        else:
            self.update_ties()

player = Player('john')
computer = Computer()

game = Game(player, computer)

for i in range(0, 100):
    game.start_match(i % 3)