import random
import time

# Initialize game parameters
players = list(range(1, 457))
moved = []
eliminated = []
rounds_moved = {player: 0 for player in players}  # Tracks rounds in which players moved

moving_player_Perc = 0.8
eliminated_player_Perc = 0.05

for round_num in range(3):  # 3 rounds
    
    # Green light
    print(' ')
    print("Green light")
    time.sleep(5)  
    if len(players) > 0:
        moved_players = random.sample(players, int(len(players) * moving_player_Perc))
        moved.extend(moved_players)
        for player in moved_players:
            rounds_moved[player] += 1
        stationary_players = [player for player in players if player not in moved_players]
    else:
        print("No players left.")
        break
    
    print("Moved:", moved_players)
    print("Stationary:", stationary_players)
    
    print(' ')
    # Red light
    print("Red light")
    time.sleep(2)
    if len(players) > 0:
        eliminated_players = random.sample(players, int(len(players) * eliminated_player_Perc))
        eliminated.extend(eliminated_players)
        players = [player for player in players if player not in eliminated_players]  # Remove eliminated players
    else:
        print("No players left.")
        break
    
    print("Eliminated:", eliminated_players)

# Check for winners 
winners = [player for player, count in rounds_moved.items() if count >= 2 and player not in eliminated]

if winners:
    print("Winning players:", winners)
    print(len(winners)," players won the game")
else:
    print("No one won the game.")
