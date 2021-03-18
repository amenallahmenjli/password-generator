# This is a simple password generator built using python

# Importing necessary modules
import random
import string
import sys
import getopt

# Get user parameters
def get_input(argv):
    length = 0
    uppercase = False
    lowercase = False
    numbers = False
    symbols = False
    try:
        options, arguments = getopt.getopt(argv,"hl:o:")
        for option, argument in options:
            if option == '-h':
                help()
            elif option == "-l":
                length = int(argument)
            elif option == "-o":
                parameters = argument
                if "u" in parameters : uppercase = True
                if "l" in parameters : lowercase = True
                if "n" in parameters : numbers = True
                if "s" in parameters : symbols = True
        return [length, uppercase, lowercase, numbers, symbols]
            
    except getopt.GetoptError:
        help()

# Show help text
def help():
    
    print(text)
    sys.exit()

# Generate password based on parameters
def generate(params):
    password_characters = []
    symbols_list = "!#$%&*+?@^"
    if params[1] == True: password_characters += list(string.ascii_uppercase)
    if params[2] == True: password_characters += list(string.ascii_lowercase)
    if params[3] == True: password_characters += list(string.digits)
    if params[4] == True: password_characters += list(symbols_list)
    password = []
    for i in range(params[0]):
        password.append(random.choice(password_characters))
    password = ''.join(password)
    print(f"Your password is {password}")
    

if __name__ == "__main__":
    params = get_input(sys.argv[1:])
    generate(params)
