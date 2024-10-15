#DP1C8
#A) Definite and Indefinite Loop
#Comparing: Both repeat a block of code multiple times
#Contast: DP: Reiles on knowing the how many times they would like it to run
#IL: You don't know how many times it will run it could run forever or stop as soon as you start

#B) For vs. While Loop
#Comparing: Both are used to repeat code.
#Contast: FL: Runs a set number of times like setting it to repeat something 5 times
#WL: Runs until a condition is no longer true like saying keep doing this until the code stop working

#C) Interactive vs. Sentinel Loop
#Comparing: Both loops keep running until you tell them to stop like a commaned 
#Contast: IL: The user decides when to stop like asking "Do you want to continue?" and you say yes or no

#D) Sentinel vs. End-of-File (EOF) Loop
#Comparing: Both stop running when a certain condition is met
#Contast: SL: Stops when a special value like -1 is entered and like a secret code to stop the loop
#EOFL: Stops when you reach the end of a file.

#DP2C8
# A)  not (P and Q): True if at least one of P or Q is false.
# B) (not P) and Q: True only when P is false and Q is true.
# C) (not P) or (not Q): True if at least one of P or Q is false.
# D) (P and Q) or R: True if both P and Q are true or if R is true.
# E) (P or R) and (Q or R): True if at least one of P or R is true and at least one of Q or R is true.
# CONFUSED on this one because didnt know if you wanted the chart or not but have the chart written on paper if you want to see it.
#DP3C8
#A)
n = int(input("Enter a positive integer n: "))  # Ask the user to enter a number
sum_of_numbers = 0  
counter = 1  

# While loop to calculate the sum of the first n counting numbers
while counter <= n:  # Keep going as long as counter is less than or equal to n
    sum_of_numbers += counter  # Add the current counter to the total sum
    counter += 1  

print("The sum of the first", n, "counting numbers is:", sum_of_numbers)  # Show the answer
print()

#C) This will ask user for numbers and then it will add up everthing in the end after you type 999 to stop the program
sum_of_numbers = 0  
number = 0  

# While loop to calculate the sum of numbers until 999 is entered
while number != 999:  # Keep going until the user enters 999
    number = int(input("Enter a number (enter 999 to stop): "))  
    if number != 999:  # Check if the entered number is not 999
        sum_of_numbers += number  # Add the number to the total sum

print("The sum of the entered numbers is:", sum_of_numbers)  # Show the total
print()
#PE1C8
# a program to compute the of Fibonacci number
def fibonacci(n):
    # Check for invalid repsones
    if n <= 0:
        return "Invalid input, n must be a positive integer."
    elif n == 1 or n == 2:
        return 1  # The first two Fibonacci numbers are 1

    # Start with the first two Fibonacci numbers
    a = 1  # First Fibonacci number
    b = 1  # Second Fibonacci number

    # Loop to calculate Fibonacci numbers from 3 to n
    for _ in range(2, n):  # Start from 2 because we already have the first two numbers
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers

    return b  # Return of the Fibonacci number

# Main program
n = int(input("Enter a positive integer n to find the nth Fibonacci number: "))  # Get user input
result = fibonacci(n)  # a function to get the nth Fibonacci number
print("The", n, "th Fibonacci number is:", result)  #The result

#PE4C8
# progarm to generate the Syracuse sequence
def syracuse(n):
    sequence = []  # Create an empty list to store the sequence

    while n != 1:  # Keep going until n is 1
        sequence.append(n)  
        if n % 2 == 0:  # Check if n is even
            n = n // 2  # If even divide by 2
        else:  # If n is odd
            n = 3 * n + 1  # If odd multiply by 3 and add 1

    sequence.append(1)  # Finally, add 1 to the sequence
    return sequence  # Return the complete sequence

# Main program
starting_value = int(input("Enter a natural number to generate the Syracuse sequence: "))  # Get user input

if starting_value > 0:  # Check if the input is a positive number
    result = syracuse(starting_value)  # Call the function to generate the sequence
    print("The Syracuse sequence starting from", starting_value, "is:", result)  # Print the sequence
else:
    print("Please enter a positive natural number.")  # Ask for valid input
