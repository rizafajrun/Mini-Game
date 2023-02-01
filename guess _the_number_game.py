chance = 0
secret_number = 7
limit = 3

while chance < limit:
    guess_number = input("Select number (1-9) : ")
    guess_number = int(guess_number)

    if guess_number == secret_number:
        print("Congrats, you found the secret number!")
        break
    elif guess_number != secret_number:
        print("Not that, try again!")

    chance += 1
