#Print three different strings
print("Hello everyone")
print("My name is Seth")
print("Nice to meet you!")


#Write a program that prints a message if a variable is less than 10, and a different message is the variable is
#greater than or equal to 10
if x < 10:
  print("x is less than 10")
else:
  print("x is greater than or equal to 10")


#Write a program that prints a message if a variable is less than or equal to 10, another message is the variable
#is greater than 10 but less than or equal to 25, and another message if the variable is greater than 25
if x <= 10:
  print("x is less than or equal to 10")
elif x > 10 and x <= 25:
  print("x is greater than 10 but less than or equal to 25")
else:
  print("x is greater than 25")


#Create a program that divides to variables and prints the remainder
print(x % y)


#Create a program that takes two variables, divides them, and prints the quotient
print(x / y)


#Write a program with a variable "age" assigned to an integer that prints different strings depending on what integer
#age is
if age < 21:
  print("No drinking for you!")
elif age == 21:
  print("Have a drink!")
else:
  print("You've been able to drink, go ahead!")