# 1. Write a loop that prints every number from 1 to 10
x = range(1, 11)
for n in x:
  print(n)
  
   
# 2. Creat a while loop that keeps running until the user enters stop
i = 1
while i < 11:
  print(i)
  if i == 10:
    i += 1
while True:
  line = input('Word: ')
  if line == 'done':
    break
  print(line)
print()
  
  
  
# 3. How can you iterate over a list and print each element using a loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elements in numbers :
  print(elements)