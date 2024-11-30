# 1. write an if statement tha checks if a number is positive or negetive
num = int(input("enter number"))
if num > 0:
  print("the number is positive")
elif num < 0:
  print("the number is negetive")
else:
  print("this number is zero")

# 2. use an if-else statement to print "eligeble to vote"if a person is above 18 or above
num = int(input("enter number"))
if num < 18:
  print("To young to vote")
else:
  print("Old enough to vote")
# 3. Write a condition to check if a number is divisible by 3 and 5
num = int(input("enter number"))
if num%5 == 0:
   if num%3 == 0:
      print ("Divisible by 3 and 5")
   else:
      print ("divisible by 5 not divisible by 3")
else:
   if num%3 == 0:
      print ("divisible by 3 not divisible by 5")
   else:
      print  ("not Divisible by 5 not divisible by 3")