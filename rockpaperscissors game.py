
import random
user_wins=0
count=0
computer_wins=0
game=["rock", "paper", "scissors"]
while True:
    print(" ")
    user_input= input("Type in Rock , Paper , scissors: ").lower()
    count+=1
    if user_input not in game:
        continue

    random_number = random.randint(0,2)
    computer_pick=game[random_number]
    print("computer picked" , computer_pick)
    if user_input == "paper" and computer_pick =="rock":
        print("Results : you won!!")
        user_wins+=1
    elif user_input =="scissors" and computer_pick =="paper":
        print("Results : you won!!")
        user_wins+=1
    elif  user_input =="rock" and computer_pick =="scissors":
        print("Results : you won!!")
        user_wins+=1 
    elif  user_input =="rock" and computer_pick =="rock":
        print("Results : draw") 
    elif user_input =="paper" and computer_pick =="paper":
        print("Results : draw")  
    elif user_input =="scissors" and computer_pick =="scissors":
        print("Results : draw")    
        
    else:
        
        print("Results : you lost")
        computer_wins+=1   

    if count >= 3:
        print(" ")
        print("Total Score")
        
        print("you won", user_wins)
        print("the computer won", computer_wins)
        break
