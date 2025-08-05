import random 
print("")
secret_number = random.randint(1,10)
guess= int(input("enter a number between 1 and 10: "))
while guess != secret_number : 
  if guess < secret_number:
    guess = int(input("too low ! try again: "))

  else: 
    guess = int(input("too high ! try again: "))

print("congrats! you guessed it .")