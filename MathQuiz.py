import random

choice = 0
total_correct = 0
total_questions = 0

print("Welcome to the Math Quiz!")

while choice != 3:
  print("\nWhat would you like to pracice?")
  print(" 1) Addition")
  print(" 2) Subtraction")
  print(" 3) Quit")
  choice = int(input("Input choice: "))
  
  if choice == 3:
    break
  
  questions = int(input("How many questions would you like to do? "))
  total_questions += questions
  
  if choice == 1:
    print("\nLet's add!")
    correct = 0
    for x in range (questions):
      num1 = random.randint(1, 10)
      num2 = random.randint(1, 10)
      guess = int(input(str(num1) + " + " + str(num2) + " = "))
      if guess == (num1 + num2):
        print("Correct! Great job!")
        correct += 1
        total_correct += 1
      else:
        print("Incorrect. Better luck next time!")
        
    print("You got " + str(correct) + "/" + str(questions) + " correct!")
  elif choice == 2:
    print("\nLet's subtract!")
    correct = 0
    for x in range (questions):
      num1 = random.randint(1, 10)
      num2 = random.randint(1, 10)
      guess = int(input(str(num1) + " - " + str(num2) + " = "))
      if guess == (num1 - num2):
        print("Correct! Great job!")
        correct += 1
        total_correct += 1
      else:
        print("Incorrect. Better luck next time!")
        
    print("You got " + str(correct) + "/" + str(questions) + " correct!")

print("\nYou got " + str(total_correct) + "/" + str(total_questions) + " correct!")
print("That's a score of %.2f" % ((total_correct/total_questions) * 100))
print("\nThanks for practicing some math!")