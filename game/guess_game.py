import random

fst_num = int(input("Enter start number: "))
lst_num = int(input("Enter lasr number: "))

secret = random.randint(fst_num,lst_num)

print(" now , you guess a number between fast_number and last_number")

while True:
    guess = int(input("Enter your guess number: "))
    if guess < secret :
        print("low num ! , try again ")
    elif guess > secret:
        print("too high ! , try again")
    else:
        print("Wow, You guessed the number.")
        break