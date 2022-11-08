#Parker Lowney
import os
import time


#CONSTANTS
WIDTH = os.get_terminal_size().columns
START_BUFFER = " " * ((WIDTH // 2) - 5)
KERNING_BUFFER = " " * 2
LETTER_HEIGHT = 6
CLEAR_LINE = "\033[k"
CURSOR_UP = f"\033[{LETTER_HEIGHT}A"
TIME_DELAY = 0.1



#________________________

INPUT = "this is a very long string of characters"

#________________________

LOOP = True

#Basic boxes for testing
test_box = ["++++ ",
            "+  ++",
            "+++++",
            "+   +",
            "+++++"
            ]

test_box2 = ["+++++",
             "+   +",
             "+++++",
             "+  + ",
             "+   +"
            ]

test_box3 = ["+++++",
             "+   +",
             "+   +",
             "+   +",
             "+++++"
            ]



#Functions

def generate_lines(letters):
    '''Generates the final list of lines by adding the others together
    Takes in double array of letters and returns a list of final lines'''

    final_lines = [START_BUFFER, START_BUFFER, START_BUFFER, START_BUFFER, START_BUFFER]

    for l in range(len(final_lines)):
        for s in letters:
            final_lines[l] += s[l] + KERNING_BUFFER

    #for i in final_lines:
        #print(i)

    return final_lines


def read_alphabet():
    '''Reads the alphabet file into a dictionary (num:list)'''
    f = open("alphabet.txt", "r")
    letters = {}
    f = f.readlines().copy() #Convert text file to list

    #Loop through txt file
    for n in range(65, 91, 1):
        letters[n] = [] #Makes new list for key

        for i in range(5):
            letters[n].append(f.pop(0).strip("\n")) #Pops 5 values into it

        f.pop(0) #Pops blank space

    #Adds all the non-alphabetical characters
    weird_chars = [33, 63, 46, 44, 40, 41, 45]
    for c in weird_chars:
        letters[c] = [] #Makes new list for key

        for i in range(5):
            letters[c].append(f.pop(0).strip("\n")) #Pops 5 values into it

        f.pop(0) #Pops blank space

    #Adds space
    letters[32] = ["       ", "       ", "       ", "       ", "       "]


    return letters



def parse_input(string):
    '''Takes an input string and parses it into a list of big letters'''
    alph = read_alphabet() #Dictionary of big letter values
    #alph = {66 : test_box, 82 : test_box2, 79 : test_box3}
    letters = []
    nums = []

    #Loop through string and convert to ints
    for c in string:
        nums.append(ord(c))

    #Loop through int list and converts to big letters
    for n in nums:
        letters.append(alph[n])

    return letters


def print_frame(lines):
    '''Prints one frame of the letters using the lines passed and width variable'''

    #Clear old lines and move cursor before printing
    print(CURSOR_UP)
    
    #Print a set selection of lines
    for i in lines:
        print(CLEAR_LINE + i[:WIDTH])

    
def longest_line(lines):
    '''Returns the index of the longest line in a list of strings'''
    longest = 0

    for i, s in enumerate(lines):
        #print(len(s.strip()), len(lines[longest]))
        if len(s.strip()) > len(lines[longest].strip()):
            longest = i

    return longest

def main():
    '''Main function'''
    letters = parse_input(INPUT.upper()) #Parses input string into big letters
    final_lines = generate_lines(letters) #Generates final lines
    end = longest_line(final_lines)
    print(f"\033[{LETTER_HEIGHT + 3}B") #I'm incredibly lazy


    while "+" in final_lines[end]: #Goes until final lines is completely off screen
        print_frame(final_lines)

        for s in range(len(final_lines)): #Removes first char from each line
            #print(final_lines[s])
            final_lines[s] = final_lines[s][1 : len(final_lines[s])]
            #print(final_lines[s])


        if LOOP:
            if len(final_lines) < WIDTH: #Once the lines are short enough, generate the lines again and add them
                new_lines = generate_lines(letters)

                for i in range(len(final_lines)):
                    final_lines[i] += new_lines[i]

        time.sleep(TIME_DELAY)

    print_frame(final_lines[s][1 : len(final_lines[s])]) #Clears the last plus

    #for l in test_box:
        #print(start_buffer + l)


if __name__ == "__main__":
    main()
