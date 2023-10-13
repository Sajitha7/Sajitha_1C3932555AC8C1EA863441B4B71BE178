class Player:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is playing cricket.")

class Batsman(Player):
    def play(self):
        print(f"The batsman {self.name} is batting.")

class Bowler(Player):
    def play(self):
        print(f"The bowler {self.name} is bowling.")

# Get player's name from the user
player_name = input("Enter the player's name: ")

# Create objects of the Batsman and Bowler classes with the player's name
batsman = Batsman(player_name)
bowler = Bowler(player_name)

# Call the play() method for each object
batsman.play()
bowler.play()