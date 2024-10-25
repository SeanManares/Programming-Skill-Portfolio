#06-Brute_Force_Attack
def login():     #define login
    password = 12345          
    attempts = 5          #maximum attempt
    print("Password Entry System")
    print("The password has 5 digits")      #basic req
    
    
    while attempts > 0:      #I use while loop to continiously ask the password from user
        pass_inp = (input("Enter password: "))    
        if int(pass_inp) == password:       #I use int to convert str to integer
            print("Login successful")
            break            #to stop the code if the user inp correct pass
        else:
            attempts -= 1      #Adv Requirement: every failed attempt is subtracted to the maximum attempt
            print(f"Incorrect password. Attempts remaining: {attempts}")
            
        if attempts == 0:   
            print("Login block. Please try again later.")
            
login()       #call login function