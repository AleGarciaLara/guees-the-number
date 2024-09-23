import random

def computer_guess(number):
    low = 1
    high = 100

    while True:
        guess = random.randint(low, high)
        print(f"La computadora adivina: {guess}")

        if guess > number:
            print("¡Número alto! La computadora intenta de nuevo.")
            return False
        elif guess < number:
            print("¡Número bajo! La computadora intenta de nuevo.")
            return False
        else:
            print("La computadora ganó!")
            return True  




