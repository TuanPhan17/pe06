# Ask user for first number 
# try to convert 1st number into integer 
# if converting 1st input casuses error print error message, has to be a number 
# Ask user for 2nd number 
# to convert 2nd number in a integer 
# if converting 2st input casuses error print error message, has to be a number 
# if both 1st and 2nd are valid integers , add them and print sum 

try: # catches either bad inputs 
    num1 = int(input("Enter the first number: ")) # Ask for the first number

    num2 = int(input("Enter the second number: "))  # Ask for the second number

    total = num1 + num2  # Ask for the second number

    print("The sum is:", total)

except ValueError:
    print("Error: You must enter a valid number.") # If either input is not a number