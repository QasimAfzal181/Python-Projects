##############################################################################################################
##  Program Name: Assignment 3                                                                              ##
##  Author: Qasim Afzal                                                                                     ##
##  Date: November 11, 2023                                                                                 ##
##  Class: PRGM1000 - Scripting Fundamentals                                                                ##
##  Instructor: John Zabiuk                                                                                 ##
##  About: Entering an IPv4 address will validate it, tells the network class and the binary conversion     ##
##############################################################################################################



def main(): #Prompts the User to enter a IPv4 address or quit, call out the other function if the user hasn't quit
    QuitFlag = False #indicate if user has quit or not in a variable
    while not QuitFlag: #while the user hasn't quit yet
        UserInput = input("Enter an IPv4 address in decimal notation or 'q' or 'Quit' to exit (e.g. 192.168.10.0): ") #ask the user to enter a IPv4 address or 'q' to exit or 'quit' to exit
        if UserInput.lower() == 'q' or UserInput.lower() == 'quit': #if user enters q or quit,
            #display a goodbye message
            print("Thanks for using my program! See you next time!")
            QuitFlag= True #make it true since the user has quit
        else: #otherwise
            if validateip(UserInput): #if validateip based on userput, display the info, the ip class which is equal to getclass function based on the userinput
                ipclass = getclass(UserInput) #ip class will be based on the getclass function by the userinput
                BinaryNum = ipaddrbits(UserInput) #binary num is the variable which is based on the ipaddrbits function based on the userinput
                displayipinfo(UserInput, ipclass, BinaryNum) #BinaryNum)
            else: #otherwise
                QuitFlag = False #user didn't quit, set it to false
    return

def getipaddress(UserInput, QuitFlag): #function that will get the ip address based on the  user input and the quit flag
    if UserInput.lower() == 'q' or UserInput.lower() == 'quit': #check if the user wants to quit or not by entering 'q' or 'quit'
        QuitFlag = True #set it to true
        IPAddr = False #set it to false, meaning the ip address is false
    else: #otherwise
        IPAddr = validateip(UserInput) #Get the validate ip function to validate the userinput as a ip address
        if IPAddr: #if ip is true, go to the next step
            ipclass = getclass(IPAddr) #get the class function to determine the IP address class
            displayipinfo(IPAddr, ipclass) #get the display info to display the ip address, the ip class
    return IPAddr #return the ip address which is either valid or not


def getclass(UserInput): #indicates if it's class A,B,C, D or E
    octet = UserInput.split(".") #split the userinput using periods and store it in a variable called oct
    firstOctet = int(octet[0]) #convert oct[0] which is the first octet and store it in a variable called firstOctet
    if 0 <= firstOctet <= 127: #if the first octet is in range between 1 to 126
        return "A" #return it's a Class A
    elif 128 <= firstOctet <= 191: #otherwise if the first octet is ranging between 128 and 191
        return "B"  #return it's a Class B
    elif 192 <= firstOctet <= 223: #otherwise if the first octet is ranging between 192 and 223
        return "C"  #return it's a Class C
    elif 224 <= firstOctet <= 239: #otherwise if the first octet is ranging between 224 and 239
        return "D (Multicast)"  #return it's a Class D which is a multicast address
    elif 240 <= firstOctet <= 255: #otherwise if the first octet is ranging between 240 and 255
        return "E (Reserved)" #return a class E which is a reservered address
    else: #otherwise
        return #return nothing as the user didn't enter any ip based on a certain class range

def validateip(UserInput): #function that validate based on what the user enter, if it's a valid IPv4 address, or not
    lOctets = UserInput.split(".") #define lOctets which is equal to userinput split by "." in each octet
    if "." in UserInput:  # check if there are decimal when the user enter
        if len(lOctets) == 4: # Check if user entered 4 items in each decimal
            for octet in lOctets: # loop in each octets
                if not octet.isnumeric():  #check if each octet is not a number
                    errormessage(3) #if it is not a number show the errormessage 3
                    return False #return false meaning it's not a number
                if not (0 <= int(octet) <= 255): #check if it's not in the range of 0-255
                    errormessage(0) #show error message 0 indicating the octets are out of range
                    return False #return false meaning it's invalid
        elif len(lOctets) > 4: #if the lenth of the octet is less than 4
            errormessage(4) #show the error message that correspond to it
            return False #return false meaning it's invalid
        else: #otherwise
            errormessage(1) #if user didn't entered 4 octet show the errormessage 1
            return False #return false meaning it's invalid
    else: #otherwise
        errormessage(2) #if there is no period show the errormessage 2
        return False  #return false meaning it's invalid
    return UserInput #return what the user has entered


def displayipinfo(ipaddr, ipclass, BinaryNum): #function that displays ip class, the binary, and the ip address (or what the user has entered)
        print("---IPv4 Information---") #Displays the IPv4 information
        print("You entered: ", ipaddr) #display you entered and the ip address
        print("Network Class:", ipclass) #display the ip class
        print("Binary: ", BinaryNum) #display the binary conversion for the ip address
        return #return nothing as it will just display the print statement above

def errormessage(idnum): #function that displays the error message based on id num which is the id for the error to display
    errlist = [  #errlist is a list of error to display in a certain case when the user makes a error
        "IP out of range. Octet 1/2/3/4 are out of range.", #0 #if the user entered more than 255 , show this error message
        "You entered less than 4 octet", #1 #show this error message if the user entered less than 4 octet
        "Not the right format for an IP address.", #2 #show this error message if the user didn't type in the correct format for an IPv4 address
        "You entered non-numeric octets.", #3 #show this error message if the user entered 4 items seperated by periods but not numbers eg: x.x.x.x or a.b.c.d
        "You entered more than 4 octet" #4 #show this error message if the user has entered more than 4 octet
        ]
    if idnum >= 0 and idnum < len(errlist): #if the id num is in a correct range of error messages or default to 0
        errindex = idnum #if it is true, the error index will be based on the id num which is the error id
    else: #otherwise
        errindex = 0 #the error index will be 0, out of range
    print(errlist[errindex]) #display from the errlist of the errindex based on the user error
    return #otherwise

def ipaddrbits(ipaddress): #Accepts an IP address in string format and returns a list of bits for each octet
    lOctets = ipaddress.split(".") #lOctets is the list by splitting the ipaddress seperated by periods
    binaryOctets = [] #create BinaryOctets as a empty list to store the binary representation
    for binOct in lOctets: #convert each binary in each list of ocets
       binaryOctet = bin(int(binOct))[2:] #convert the octet to binary and remove the '0b' prefix
       binaryOctet = "0" * (8 - len(binaryOctet)) + binaryOctet #binary representation is 8 bits long and the leading zeros
       binaryOctets.append(binaryOctet) #add the binary representaion to the octet list
       #print(len(binaryOctet))
    return binaryOctets #return the binary conversion based on the IP address




if __name__ == '__main__':
    main()