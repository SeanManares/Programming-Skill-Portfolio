#10-Is_it_even?
def main():
    print("Check whether the number is odd or even")
    num = int(input("Enter the number: "))    # ask user the number
    if (num%2) == 0:                        #I use modulus operator to  find the remainder, if remainder is = 0, it is true
        print(f"The number {num}  is even")    #I put f before the string to replace the num its value
    else:
        print(f"The number {num} is odd")
        
main()          #call the function