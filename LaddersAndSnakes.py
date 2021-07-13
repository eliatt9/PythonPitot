# Import modules
import random

# Global variables
NUMBER_OF_LADDERS = 6  # Number of Ladders
NUMBER_OF_SNAKES = 6  # Number of Snakes
SIZE_OF_TABLE = 100  # Number of the squares in the board

# Pre-game text
print("Welcome to Davidalk THE ONE AND ONLY Game board.\n"
      "Today we gonna play ladders & Snakes\n"
      "Good luck for everyone!")

# Define players
num_of_players = int(input("Choose number of players: "))
players = []
for i in range(num_of_players):
    player = {"name": "Player" + str(i+1),
              "position": 0}
    players.append(player)

# Define ladders
ladders_starts = []
ladders_ends = []
for i in range(NUMBER_OF_LADDERS):
    num1 = random.randint(1, 99)
    while num1 in ladders_starts:
        num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    while (num2 in ladders_ends) or (num1 >= num2):
        num2 = random.randint(1, 99)
    ladders_starts.append(num1)
    ladders_ends.append(num2)

# Define snakes
snakes_starts = []
snakes_ends = []
for i in range(NUMBER_OF_SNAKES):
    num1 = random.randint(1, 99)
    while num1 in snakes_starts:
        num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    while (num2 in snakes_ends) or (num1 >= num2):
        num2 = random.randint(1, 99)
    snakes_starts.append(num1)
    snakes_ends.append(num2)

# Define game variables
winner = ""
isChanged = False

print(ladders_starts, ladders_ends)
print(snakes_ends, snakes_starts)

# Loop for the whole game as long as we don't have winner we keep going
while not winner:
    for player in players:  # Each Player turn every round
        null = input("Enter to roll the dice")
        roll = random.randint(1, 6)  # Roll the dice
        new_position = player["position"] + roll
        if new_position - 100 > 0:  # Check if the player passed the 100 mark
            new_position = new_position - (new_position - 100)
        for i in range(NUMBER_OF_LADDERS):  # Check if there is Ladder
            if new_position == ladders_starts[i]:
                new_position = ladders_ends[i]
                isChanged = True
                continue
        if not isChanged:  # Don't look for snake if he got ladder this turn
            for i in range(NUMBER_OF_SNAKES):  # Check if there is Snake
                if new_position == snakes_ends[i]:
                    new_position = snakes_starts[i]
                    continue
        # Update the player's position
        player["position"] = new_position
        if player["position"] == 100:  # Check if there is Winner
            winner = player["name"]
            continue
        for play in players:  # Current players state
            print(play["name"], " is on square ", play["position"])

# Post-game text
print("Congratulations %s is the winner this time!"
      "Good Game! Well Played!" % winner)
