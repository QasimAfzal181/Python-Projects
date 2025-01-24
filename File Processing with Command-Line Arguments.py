##############################################################################################################
##  Program Name: Assignment 4                                                                              ##
##  Author: Qasim Afzal                                                                                     ##
##  Date: December 5th, 2023                                                                               ##
##  Class: PRGM1000 - Scripting Fundamentals                                                                ##
##  Instructor: John Zabiuk                                                                                 ##
##  About: program reads a file, modifies it to a new file, if not, an error message will display           ##
##############################################################################################################

#import module
from datetime import datetime
import os
import sys


def main():
    # Define default directory
    defaultpath = "c:\\prgm1000\\"
    # Check if input file exists
    inputFileName = defaultpath + 'myinputfile.txt'
    if not os.path.exists(inputFileName):
        print("Error: Input file 'myinputfile.txt' not found.")
        sys.exit(1)

    # Check the number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: workingwithfiles.py myinputfile.txt outputfile.txt")
        sys.exit(1)

    outputFileName = defaultpath + sys.argv[2]  # Output file

    # Check if the output file already exists
    if os.path.exists(outputFileName):
        UserInput = input("The output file already exists. Do you want to overwrite it? (Y/N): ")
        if UserInput.upper() == "Y":
            print("We are overwriting the file.")
            print("Overwrite has succeeded.")
        elif UserInput.upper() == "N":
            NewFileName = input("Enter a new filename to overwrite to: ")
            if not NewFileName:
                print("You didn't enter a file name.")
                sys.exit(1)
            print("New file is being created. Overwrite file is in: " + defaultpath + NewFileName)
            outputFileName = defaultpath + NewFileName
            # Copy the content from the existing output file to the new filename
            try:
                with open(defaultpath + 'outputfile.txt', 'r') as ExistingFile, open(outputFileName, 'w') as NewFile:
                    NewFile.write(ExistingFile.read())
                print("File was not overwritten.")
                print("Goodbye! Thank you for using my program!")
                sys.exit(1)
            except Exception as error:
                print("Error: Something went wrong while overwriting the file. Rebooting...")
                sys.exit(1)
        else:
            print("Invalid input. Exiting...")
            sys.exit(1)
    try:
        # Read the input file and write to the output file
        with open(inputFileName, "r") as inputFile, open(outputFileName, "w") as outputFile:
            # Header information - output file stuff - os, login user, date and time it was run
            outputFile.write("Operating System program ran on: " + os.name +
                             " (Window System) " + "\n" +
                             "Logged-in user who ran the program: " + os.getlogin() + "\n" +
                             "The date and time that the program was run in the format:\n" +
                             str(datetime.now()) + "\n")
            # Process each line of the input file - output the stuff from the input file with the time
            for line in inputFile:
                timeFile = str(datetime.now()) + " " + line
                outputFile.write(timeFile)
        print("File processing completed successfully!")
    except Exception as error:
        print("Error: Something went wrong while writing to the output file. Rebooting...")
        sys.exit(1)


if __name__ == "__main__":
    main()
