#!/usr/bin/python
def fizzbuzz():
    for num in range (1, 101):
      if num % 15 is 0:
         print("fizzbuzz", end=" ")
      elif num % 3 is 0:
         print("fizz", end=" ")
      elif num % 5 is 0:
         print("Buzz", end=" ")
      else:
         print(num, end=" ")
