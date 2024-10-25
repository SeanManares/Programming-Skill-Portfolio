#08-Simple_Search
names = ["Jake","Zac","Ian","Ron","Sam","Dave"]  #I created a list

user_search = input("Enter the name (1st letter is capital): ") #Optional Req.- Ask the user 
if user_search in names:       #I use the if-else statement to check whether the names are on the list         
    print("The name is on the list")       #I use in keyword to check if the user input is true or false based on the list
else:
    print("The name is NOT on the list")

    

