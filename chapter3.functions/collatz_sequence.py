
def collatz(number):
  if number % 2 == 0:
    result1 = number//2
    print(result1)
    return result1
  elif number % 2 == 1:
    result2 = 3*number + 1
    print(result2)
    return result2

try:
  num = input("Please enter a number: ")
  while num != 1:
    num = collatz(int(num))
except ValueError:
  print("Please enter an integer")
