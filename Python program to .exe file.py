##############################################################################################################
##  Program Name: Assignment 5                                                                              ##
##  Author: Qasim Afzal                                                                                     ##
##  Date: December 7th, 2023                                                                                ##
##  Class: PRGM1000 - Scripting Fundamentals                                                                ##
##  Instructor: John Zabiuk                                                                                 ##
##  About: user enter something, it writes it to a file (since it's a append file), prints the logged in    ##
##  user and the date and the time it was run                                                               ##
##############################################################################################################
#import module
import os
from datetime import datetime
import sys
#Define Variables - username current loggedIn user, current date - the date that is today
CurrentDate = datetime.today()
UserName = os.getlogin()
FullDirectory = "F:\PRGM1000\Exercise\ExerciseProgram 1-15\output\Assignment5FreeStyle\\"
#create a logfile
LogFile = "LogEntry.txt"
#open the logfile and write the loggedIn user, the date and time it was run as append file
with open(LogFile, "a") as LogFile:
    LogFile.write("Logged-in user who ran the program: " + UserName + "\n" +
                  "The date and time that the program was run: \n" +
                  str(CurrentDate) + "\n")
#Greet the user who is logged in and ask the user what is their favourite date
print("Hello", UserName, "! What is your favourite date?")
UserInput = input("Enter a date in the form of 'MM DD YYYY: ")
#split each of the month days and years
UserDateList = UserInput.split(" ")
UserDate = datetime(int(UserDateList[2]), int(UserDateList[1]),int(UserDateList[0]))
#calcluate the days difference by the current date and the date the user has entered
DaysBetween = CurrentDate - UserDate
#print out the #of days between the user date and today's date
print("The number of days between your favourite date and today is ", DaysBetween.days, "days!")
UserInput = input("\n Press ENTER to continue")