import random 

def random_number(start, end):
  return random.randint(start, end)
number = random_number(1, 100)
print("Tú número asignado es", number)