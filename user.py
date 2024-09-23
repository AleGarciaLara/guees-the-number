def user_name():
    name = input("¡Hola! ¿Cómo te llamas?")
    print(f"Bienvenida a Guess the number {name}. Intenta adivinar el número secreto entre el 1 y el 100")
    return name

def user_guess(number, name):    
    while True:
        guess = int(input(">>>Escribe tu intento:"))
        if guess > number:
            print("<<<¡Número alto! Intenta de nuevo.>>>")
            return False
        elif guess < number:
            print("<<<¡Número bajo! Intenta de nuevo.>>>")
            return False
        else:
            print(f"¡Felicidades {name}! ¡Adivinaste el número!")
            return True
            