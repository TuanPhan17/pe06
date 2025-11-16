# Program: Cats and Dogs Reader
# Description: Reads two text files (cats.txt and dogs.txt)
# and prints their contents. If a file is missing, a friendly
# error message is shown.

# Read cat names
try:
    with open("cats.txt", "r") as cats_file: # Open cats.txt in read mode 
        print("Cat names:")
        print(cats_file.read()) # print contents of file 

except FileNotFoundError:
    print("Error: cats.txt file not found.") # if file doesn't exist 

# Read dog names
try:
    with open("dogs.txt", "r") as dogs_file: # Open dogs.txt in read mode
        print("Dog names:")
        print(dogs_file.read()) # print contents 

except FileNotFoundError: # if file doesn't exist
    print("Error: dogs.txt file not found.")