from user import user_name, user_guess
from computer import computer_guess
from helpers import random_number

def main():
    number = random_number(1, 100)  
    name = user_name()  
    print("¡Comencemos el juego!")
    
    game_over = False
    turn ='user'

    while not game_over:
      if turn == 'user':
        print(f"Es tu turno {name}")
        if user_guess(number, name):  
          print("¡Ganaste el juego!")
          game_over = True
        else: 
          turn = 'computer'
          
      elif turn == 'computer': 
        print("<<<Es el turno de la computadora.>>>")
        if computer_guess(number): 
          print("La compu ganó el juego.")
          game_over = True
        else: 
          turn = 'user'

if __name__ == "__main__":
    main()







      
