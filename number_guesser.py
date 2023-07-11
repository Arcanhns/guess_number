import random
game_on = True

while game_on is True:

    secret_number = random.randint(1,10)
    attempts = 0
    guessing = True

    while guessing is True:
        player = int(input("Guess the secret number between 1 - 10: "))
        if player == secret_number:
            attempts = attempts + 1
            print("You guessed correctly in",attempts,"attemps, the number was", secret_number)
            guessing = False
        elif player > secret_number:
            attempts = attempts + 1
            print("too high! try again.")
        else:
            attempts = attempts + 1
            print("too low! try again.")
        
    player = input("Do you want to play again? y/n ").lower()
    if player == "y":
        guessing = True
    else:
        game_on = False
