import random
def dice():
    min_value=1
    max_value=6
    dice=random.randint(min_value,max_value)
    return dice

while True:
    players=(input("enter the number of player (2-4) : "))
    if players.isdigit():
        players=int(players)
        if 2<= players<=4:
            break    
        else:
            print("enter a value between 2-4")
    else:
        print("invaild input")        
    
    
max_score= 30
players_score=[0 for i in range(players)]
total_score=0
while max(players_score)< max_score:
    for play_index in range(players):
        print("\n","player no:", play_index +1,"\n")

        while True:
            play= input("would you like to play? :")
            if play!="yes":
                break

            result=dice()
            if result==1:
                print("you rolled a one, you know what is means!!!!!")
                total_score=0
                break
            else:

                print("you rolled a :", result)
                total_score+=result
            print("you currently have a score of : ", total_score)
    players_score[play_index]+=total_score
    print("You have a total score of : ", players_score[play_index])
max_score=max(players_score) 
winner= players_score.index(max_score) 
print(max_score)          

            
