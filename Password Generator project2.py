import tkinter as tk
import random
root=tk.Tk()
root.geometry("500x700")
root.title("Password generator JBS")

def password():
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ':', ';', '<', '=', '>', '?', '@']

    num_passwords = int(NumPass.get())
    #password_length = int(PassLength.get())

    number = 0
 
    num_lowercase = 0
    num_uppercase = 0
    num_numbers = 0
    num_symbols = 0
    
    if True:
     
            num_lowercase = int(NumLower.get())
            number += num_lowercase
        
        
            num_uppercase = int(NumUpper.get())
            number += num_uppercase
       
       
            num_numbers = int(NumDigits.get())
            number += num_numbers
        
      
            num_symbols = int(NumSymbol.get())
            number += num_symbols
        
                

    for char in range(1,num_passwords + 1):
        password_list = []
    
        for char in range(1,num_lowercase + 1):
            password_list.append(random.choice(lower_case))
    
        for char in range(1,num_uppercase + 1):
            password_list += random.choice(upper_case)
    
        for char in range(1,num_numbers + 1):
            password_list += random.choice(numbers) 

        for char in range(1,num_symbols + 1):
            password_list += random.choice(symbols)

        random.shuffle(password_list)
        password= ""
        for char in password_list :
            password += char
       
        display.insert(tk.END, password +"\n")
    

def clear():
    display.delete(1.0,tk.END)
    
label=tk.Label(root,text="Password Generator",font=('Arial', 18))
label.pack(padx=20,pady=20)
    

label2=tk.Label(root,text="Type number of passwords", font=('Arial',10))
label2.place(x=20 , y =50)

#label3=tk.Label(root,text="Type length of passwords", font=('Arial',10))
#label3.place(x=20 , y =70)

NumPass=tk.Entry(root)
NumPass.place(x=180 , y=50)



label3=tk.Label(root,text="How many number of lower cases",font=('Arial',10))
label3.place(x=20 , y =90)

NumLower=tk.Entry(root)
NumLower.place(x=250 , y=90)

label4=tk.Label(root,text="How many number of Upper cases",font=('Arial',10))
label4.place(x=20 , y =110)

NumUpper=tk.Entry(root)
NumUpper.place(x=250 , y=110)

label5=tk.Label(root,text="How many number of Symbols cases",font=('Arial',10))
label5.place(x=20 , y =130)

NumSymbol=tk.Entry(root)
NumSymbol.place(x=250  , y=130)

label6=tk.Label(root,text="How many number of digits cases",font=('Arial',10))
label6.place(x=20 , y =150)

NumDigits=tk.Entry(root)
NumDigits.place(x=250  , y=150)

btnGenerate=tk.Button(root,text="Generate",font=('Arial',10),command=password)
btnGenerate.place(x=170,y=170)

btnClear=tk.Button(root,text="Clear",font=('Arial',10),command=clear)
btnClear.place(x=250,y=170)

display=tk.Text(root, height=25 ,width=35)
display.place(x=90,y=200)


root.mainloop( )
