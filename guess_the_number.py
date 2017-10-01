import random

num = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
for guesses in range (1,6):
  print ('Take a guess.')
  guess = int(input())
  if guess > num:
    print("Your guess is too high.")
  elif guess < num:
    print("Your guess is too low.")
  else:
      break
if guess == num:
    print('Good job! You guessed my number in ' + str(guesses) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(num))
