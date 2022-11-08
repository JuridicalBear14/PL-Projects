#Parker Lowney
import sys
import time

#sys.stdout.write("\033[F" * 2 + "Test")

#Constants
START_BLUE = "\033[94m" #Wrap any text in these two variables HTML style to make them blue or green
END_COLOR = "\033[0m"
START_GREEN = "\033[32m"
START_RED = "\033[31m"
START_YELLOW = "\033[33m"


#Variables
lines = [] #Array to store the contents of every line
file = "" #Current open file
line_num = 1 #Current furthest line


#Methods


#Adss new lines to output and into array
def addLine(line):
    global lines
    global line_num

    print("\033[3A" + "\033[K" + START_BLUE + str(line_num) + ":" + END_COLOR + line) #Prints given line three spaces up with a blue line num, clears to be safe
    print("\033[K") #Clears old border
    print("\033[K" + "\r", end="") #Clears input line
    print((START_BLUE + "\u22C0" + END_COLOR) * 50) #Reprints bottom border

    line_num += 1 #Adds one to line num

    #print("\n" + "\u22C0" * 50)



#Reads file into array
def readFile():
    global file
    global lines

    print(START_GREEN + "What file would you like to open? (full path)" + END_COLOR)
    file = input()

    #if file == "exit": #Exits back to startup
        #return
    
    try: #Ew try catch block
        f = open(file, "r") #Opens file, adds n, seeks back to beginning
        #f.write("n")
        #f.seek(0)

    except:
        print(START_RED + "Invalid file path" + END_COLOR) #Error message
        readFile()
        return

    #for i in f: #Loops through the file and reads each line into memory
        #lines.append(i)

    lines = f.readlines().copy()

    #print(lines)
    f.close()




#Prints file contents onto the screen
def printFile():
    global lines

    if len(lines) > 1: #If the file isn't empty
        lines[len(lines) - 1] = lines[len(lines) - 1].replace("\n", "") #Delte new line on last line
        print("\033[1B") #Moves the cursor down one so everything lines up

    for i in range(len(lines)):
        addLine(lines[i])

    #print("\033[25A")
    #print("\033[1A" + "\033[K" + "\033[1A" + ((START_BLUE + "\u22C0" + END_COLOR) * 50) + "\033[1B")


#Used to save file when done
def writeFile():

    f = open(file, "w")

    for i in lines:
        if not (i.endswith("\n")):
            i += "\n"
        
        f.write(i)
        
    f.close()

    #Clear the existing stuff in file and write new data


#Replaces line with new text
def replace(inputt):
    if inputt.startswith("replace-"):
        inputt = inputt.replace("replace-", "", 1) #For some reason not replacing

    else:
        inputt = inputt.replace("r-", "", 1)

    l = inputt[0: inputt.index(":")] #The line which is being replaced

    up_num = 4 + (len(lines) - int(l)) #The number of lines to move the cursor up

    #Cuts it down to just the user input
    line = inputt[inputt.index(":") + 1: len(inputt)]

    lines[int(l) - 1] = line #Replaces it in lines
    
    print("\033[" + str(up_num) + "A" + "\033[K" + START_BLUE + str(l) + ":" + END_COLOR + line) #Prints given line three spaces up with a blue line num, while deleting the old text

    print("\033[" + str(up_num - 3) + "B") #Moves cursor back down to input line
    print("\033[K" + "\r", end="") #Clears input line


#Clears the window
def clear():
    pass

#Gets size of the window
def getWinSize():
    pass

#Resizes the editing area
def resize():
    pass

#Moves screen up and down
def moveScreen():
    pass

#Saves the state of the terminal before screen clear
def saveState():
    pass

#REstarts the code to default
def restart():
    global lines
    global file
    global line_num

    lines = [] #Array to store the contents of every line
    file = "" #Current open file
    line_num = 1 #Current furthest line

    startUp()


#User loop
def userLoop():
    running = True #Controls the user loop

    while running:
        inputt = input() #User input

        if inputt.lower() == "fquit": #End
            running = False

        elif inputt.startswith("replace-") or inputt.startswith("r-"):
            replace(inputt)

        elif inputt == "save":
            writeFile()
            running = False

        elif inputt == "discard":
            print(START_GREEN + "Are you sure you want to " + START_RED + "discard " + START_GREEN + "changes?" + END_COLOR)
            print(START_BLUE + "[Y/N]" + END_COLOR)

            if input().lower() == "y": #Stops running if yes
                running = False

            else: #If they change their mind, just deletes the whole thing
                print(("\033[K" + "\033[1A") * 5)

        else: #Append line
            lines.append(inputt)
            addLine(inputt)

    restart()

    #Commands: Replace line, save, discard, replace selection?, help? (on save and discard restart)
    #Make sure to ask confirmation for most commands
    #Use backslash to literally type commands as text, just delete backslash after they hit enter?
    #Maybe highlight line to be replaced (oh god, not RGB)



#Method that runs on startup
def startUp():
    global START_BLUE
    global END_COLOR
    global file

    #Welcome message
    print(START_GREEN + "Welcome to ParText!" + END_COLOR)
    print(START_GREEN + "Would you like to do?")
    print(START_BLUE + "[Create] [Open] [Quit]" + END_COLOR)

    get_file = True #Variable to control my lil baby input loop for getting a file choice


    while get_file:
        inputt = input().lower()

        if inputt == "open":
            readFile() 
            get_file = False

        elif inputt == "create":
            print(START_GREEN + "What would you like to name your file? (include extension)" + END_COLOR)
            file = input()
            #Creates and then closes the file
            f = open(file, "x")
            f.close()
            get_file = False

        elif inputt == "quit":
            exit()

        else:
            print(START_RED + "Please choose one of the options" + END_COLOR)


    #Top border and file title with a gap of new lines
    print("\n" + START_YELLOW + file + END_COLOR)
    print((START_BLUE + "\u22C1" + END_COLOR) * 50)

    #First two line numbers
    print("\n")
    #print(START_BLUE + "1:" + END_BLUE)
    #print(START_BLUE + "2:" + END_BLUE)

    #End border
    print((START_BLUE + "\u22C0" + END_COLOR) * 50)

    #Prints any lines already in the file
    printFile()

    userLoop() #Starts the user loop

    #Get file to work with and store it
    #Print it out if it already has stuff in it
    #Call user loop

startUp()