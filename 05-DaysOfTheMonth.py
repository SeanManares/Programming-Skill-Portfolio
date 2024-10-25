#05:_Days_of_the_Month
months={1:"31 days", 2:"28 days", 3:"31 days", 4:"30 days", 5:"31 days",6:"30 days", 7:"31 days", 8:"31 days", 9:"30 days", 10:"31 days", 11:"30 days", 12:"31 days"}
monthnum = int(input("What is the month number? ")) #I put int so that when they put the number, it will be read by my conditional statements
if monthnum == 1:      #1-12 stands for January to December
    print(months[1])    
elif monthnum == 2:   #Adv requirement
    leap=input("Is the year a leap year? [1]Yes or [0]No: ")
    if leap == str(1):    #I put str so that it will read the number 1 (loop)
        print('29 days')
    elif leap == str(0):  
        print(months[2])  #2 is the normal year for february in the dictionary
    else:
        print("Invalid Number")       
elif monthnum == 3:
    print(months[3]) 
elif monthnum == 4:
    print(months[4]) 
elif monthnum == 5:
    print(months[5]) 
elif monthnum == 6:
    print(months[6]) 
elif monthnum == 7:
    print(months[7]) 
elif monthnum == 8:
    print(months[8]) 
elif monthnum == 9:
    print(months[9]) 
elif monthnum == 10:
    print(months[10]) 
elif monthnum == 11:
    print(months[11]) 
elif monthnum == 12:
    print(months[12])      
else:                                #Incase the user input >12 or <1
    print("Invalid month number (1-12)")               