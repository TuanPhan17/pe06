# Word counter 
# Ask user for a text file name, reads the file
# prints how many words are in it 
filename = input("Enter filename: ") # Ask for file name - We used "tuan.txt"

#Expected output is 4 words

try:
    with open(filename, "r") as file: #Open file in read mode
        text = file.read() # reads entire file into a string 
        words = text.split() # splits text into a list of words 
        print("Number of words:", len(words)) # Prints total number of words 
except FileNotFoundError: # If file doesn't exist or cant be open. 
    print("Error: File not found.")
