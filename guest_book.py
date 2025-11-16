#Pseudocode
# do a while loop, keeps asking user for name till the type quit 
# Tak whatever they type and store it as the variable name 
# check if what they type ignoring upper and lower case, if the word is "quit"
# If its quit print message book complete and end 
# if its not pring welcome message using their name 
# open file guest_book.txt in append mode so you can add it w/out deleting whats inside
# write persons name into the file
# close file 
# go back to the while loop till user ends 

while True:
    name = input("enter your name(or 'quit' to stop):  ")  # Ask for name 

    if name.lower() == "quit":  # if they typed quit 
        print("Guest book complete.")  # its done
        break  # end the loop

    print(f"Welcome, {name}!")  # if they enter a name 

    with open("guest_book.txt", "a") as file: # Open file in append so we dont delete old entries 
        file.write(name + "\n")  # write name on a new line
