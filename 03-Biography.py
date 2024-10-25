#03:_Biography

info={}

info['name']=input("Enter your full name: ")     #get user input and store it on the name key on info dictionary
info['hometown']=input("Enter your hometown: ")

while True: 
    age_inp=input('Enter your age: ')
    if age_inp.isdigit():    #true if the user input a digit
        info['age']=int(age_inp)      #put the str digit into an integer value
        print(info)
        break
    else:           #if ever the user input a string not an integer
        print("Please enter a valid age number (number).")

"""
Adv Req: first i make a dictionary named info, then I create a list 
to store multiple key-value pairs and I can get user response 
by using input. 

for the age, I use while loop to to repeat the input from the user 
incase the user type a string instead of an integer. If the user already
type an integer, the condition is met so the code will end
"""



       
