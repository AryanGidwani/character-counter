# Aryan Gidwani
# December 10, 2021
# ICS3UO - A
# The purpose of this program is to find how much each letter appears in any
# string that the user inputs in. After calculating how much each letter
# appears in a user-inputted string, it will inform the user of the important
# information.

import sys
# imports a module which helps with the program

def stopProgram(userInput):
    if userInput.lower() == "quit":
        print("Thank you for using this program!")
        # concluding message
        sys.exit()
        # terminates the program

    else:
        pass
        # does nothing

def characterCounter():
    flag = True
    # creates a flag which holds the boolean value of True
    while flag:
        characterDict = {}
        # creates an empty dictionary, where keys and values will be added on later
        chosenString = input("Enter in any string of your choice, and the program will count how many times each character appears!: ")
        # asks the user to input a string of their choice
        chosenString = chosenString.lower()
        # makes all the letters of the string lowercase
        stopProgram(chosenString)
        # checks and sees if the user wanted to quit
        chosenString = list(chosenString)
        # puts the string into a list
        for counter in range(0, len(chosenString)):
            if chosenString[counter] in characterDict:
                characterDict[chosenString[counter]] = characterDict[chosenString[counter]] + 1
                # loops through the dictionary while looping through the user
                # inputted string, and increments the value of how many times
                # a letter is detected

            else:
                characterDict[chosenString[counter]] = 1
                # adds the character to the dictionary and sets the value to 1

        print("Here is the list of characters and how many times they appear! " + "\n" + str(characterDict) + "\n")
        # prints out the dictionary and information
                    
name = input("Hello! What is your name? ")
# asks the user for their name
print("Hello " + name + "! The purpose of this program is to find how much of each character or letter there is in a string that you input! You will input a string, and the program will tell you the rest of the information!")
# introductory message

characterCounter()
# calls the characterCounter function
