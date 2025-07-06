def get_guess():
    guess = int(input("Enter guess num: "))
    return guess

def main():
    guess = get_guess()            #the both guess are different scope 
    if guess == 50:
        print("correct")
    else:
        print("incorrect")

main()