# 1. Create a list of 5 cities and print the third city 
thislist = ["Ibadan", "Victoria Island", "Ikeja", "Agege", "Alakija"]
print(thislist[2])

# 2. Write a program that adds a new city to a list and then prints the entire list. 
thislist = ["Ibadan", "Victoria Island", "Ikeja", "Agege", "Alakija"]
print (thislist[4])

new_city = (input(""))
thislist.append(new_city)
print(thislist)

# 3. How would you loop through a list and print only the even numbers 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in a:
  
    if val % 2 == 0:
        print(val, end = " ")
        