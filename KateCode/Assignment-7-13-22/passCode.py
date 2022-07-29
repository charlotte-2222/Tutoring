# This code will act as a basic password generator for me to continue working on

# This inputs the modules we need to form the password randomly
import random
import string

# This will allow the user to choose the complexity of their password
choice = int(input("Please choose from the following: 1 for letters; 2 for letters and number; 3 for numbers, letters, and symbols"))

# This dedicates different character lists depending on
if choice == 1:
    characters = list(string.ascii_letters)
elif choice == 2:
    characters = list(string.ascii_letters + string.digits)
elif choice == 3:
    characters = list(string.ascii_letters
                      + string.digits
                      + string.punctuation)
else:
    print("Invalid input")

# This allows the user to determine the length of their password
length = int(input("Please enter your desired password length:"))

# This arranges our characters in a random order
random.shuffle(characters)

# This snips part of the character list according to the users desired password length
password = []
for i in range(length):
    password.append(random.choice(characters))

# This shuffles the password again
random.shuffle(password)

# This prints the password as a string after being converted from a list
print("".join(password))

