#################################################################################################
##  Program Name: Validating an IP address                                                    ##
##  Author: Qasim Afzal                                                                       ##
##  Date: October 7th, 2023                                                                   ##
##  How to use the program:                                                                   ##
##  Enter a IPv4 address in decimal notation and the program will check if it's valid or not  ##
##  Class: PRGM1000 - Scripting Fundamentals                                                  ##
################################################################################################


# State the Variables:
QuitFlag = False  # variable to indicate if the user has quit or not
# Validate an IPv4 address while the user hasn't typed quit
while not QuitFlag:
    UserInput = input("Enter an IPv4 address in decimal notation or 'Quit' to exit (e.g. 192.168.10.0): ")
    # If the user entered Quit, the program ends; otherwise, continue
    if UserInput.upper() == "QUIT":
        QuitFlag = True
    else:
        # check if there are decimal when the user enter
        if "." in UserInput:
            lOctets = UserInput.split(".")  # define lOctets which is equal to userinput split by "." in each octet

            if len(lOctets) == 4:  # Check if user entered 4 items in each decimal
                IPValid = False  # Set the IP valid to false since there are 4 octets; not sure if they are in the range or not
                for octet in lOctets:  # loop in each octets
                    # check if each octet is not a number or if it's not in the range of 0-255
                    if not octet.isnumeric() or not 0 <= int(octet) <= 255:
                        IPValid = False  # set the IP to false since the octet is either out of range or it's not a number
                    else:  # otherwise
                        IPValid = True  # set the IPValid to true; meaning there are 4 octet in range: (0-255)
                # check if the IP is valid; the 4 octets are seperated by decimal notation, are in range between 0-255
                if IPValid is True:
                    # print what the user typed indicating it's a valid IPv4 address
                    print("You entered:", UserInput, " which is a valid IP address.")
                else:
                    # if everything above is false, tell the user what they typed and say it's an invalid IP address
                    print("You entered:", UserInput, "which is an invalid IP address because it's not in range.")
            else:
                # If the user didn't type 4 numbers or 'quit,' tell the user that what they entered is not a valid IP address
                print("You entered:", UserInput, " which is not a valid IP address. Try again or type 'Quit'.")
        else:
            # user entered anything else than a number or quit, display a message and let the user restart
            print("You entered something else that is not an IP address! Try again or type 'Quit'.")
