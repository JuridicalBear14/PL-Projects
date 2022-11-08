#Parker Lowney
import sys
import time
from datetime import datetime
import tkinter


#Colors
START_GREEN = "\033[32m"
END_COLOR = "\033[0m"
START_BLUE = "\033[94m"
START_RED = "\033[31m"

FILE = ""

#Delay
if len(sys.argv) == 2:
    DELAY = int(sys.argv[1])

elif len(sys.argv) == 3:
    DELAY = int(sys.argv[1])
    FILE = sys.argv[2]
else:
    DELAY = 3

#Tkinter object used to get the mouse position
t = tkinter.Tk()


#Methods

def get_mouse():
    '''Gets mouse position (in tuple form)'''

    return t.winfo_pointerxy()

def main():
    '''Main method'''
    if not FILE == "": #If a text file is specified
        f = open(FILE, 'a')

    print(f"{START_GREEN}RUNNING{END_COLOR}")
    #Prints current date and time
    print(f"{datetime.now()}")

    print("q: Quit, s: Save")

    running = True #Variable to control flow loop

    while running:
        time.sleep(DELAY) #Adds a delay so it doesn't flood you with info
        c_time = str(datetime.now().time()) #Gets the current time
        c_time = c_time[:c_time.find(".")] #Strips the decimal off of the second
        m_pos = get_mouse()

        #print(f"{START_BLUE}{c_time}{START_RED}-{START_GREEN}{m_pos}{END_COLOR}") #With color
        print(f"{c_time}-{m_pos}") #Without color

        if not FILE == "":
            f.write(f"\n{c_time}-{m_pos}\n")
        
    f.close()

if __name__ == "__main__":
    main()
