# write a function that takes a number as an input and returns that number squared

def square(x):
    """
    Returns x * x.
    :param x: int.
    """
    return x*x

# create a function that accepts a string as a parameter and prints it

def printString(str):
    """
    Prints a string.
    :param: str.
    """
    print (str)

# write a function that takes three required parameters and two optional parameters

def add_three(x, y, z, a = 10, b = 5, c = 2):
    """
    Adds three numbers together and
    prints the sum. Values 10, 
    5, and 2 are substituted if no 
    values are passed.
    :param x: int.
    :param y: int.
    :param z: int.
    """
    print (x + y + z)

# write a program with two functions. The first function should take an integer as a parameter and return the result of the integer
# divided by 2. The second function should take an integer as a parameter and return the result of the integer multiplied by 4. 
# Call the first function, save the result as a variable, and pass it as a parameter to the second function.


def divide_by_two(x):
    """
    Takes a value and 
    divides it by two.
    :param x: int.
    """
    return x / 2

def divide_by_four(y):
    """
    Takes a value and 
    divides it by four.
    :param x: int.
    """
    return y / 4

new_num = divide_by_two(16)

divide_by_four(new_num)

# write a function that converts a string to a float and returns the result. Use exception handling to catch the exception that
# would occur

try:
    """
    Takes two inputs and converts 
    them to floats. The two floats
    are then muliplied by each
    other. If a number is not 
    entered as a value, a 
    ValueError is printed.
    """
    a = input("Enter a number:")
    b = input("Please enter another number:")
    a = float(a)
    b = float(b)
    print(a * b)
except (ValueError):
    print("Not a valid input! Try again.")