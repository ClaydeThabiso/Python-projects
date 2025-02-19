import random
import time
Operators=[" +", "-","*"]
Start= 1
end=10
problems=5
def maths():
    LHS= random.randint(Start,end)
    RHS= random.randint(Start,end)
    choose_Operators=random.choice(Operators)
    expression= str(LHS)+ " "+ choose_Operators + " "+ str(RHS)
    answer=eval(expression)
    return expression, answer

Start_time= time.time()
print("TIme is starting NOW !!!")
correct= 0
wrong=0
for i in range(problems):
     expression , answer=maths() 
     while True:
        user_input=input("Problem #"+str(i+1 )+":"+" "+  expression +" = ")
        if user_input == str(answer):
           correct+=1
        else:
            wrong+=1   
        break
         
             
   
        
          
           

end_time=time.time()
total_time =round(end_time-Start_time,2)
print("you finshed in ", total_time,"seconds")
print ("you got ", correct,"correct " ,"And ", wrong," wrong")       
