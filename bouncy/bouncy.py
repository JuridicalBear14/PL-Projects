#Parker Lowney
import time
import os
from bouncy_item import Item, Boxy_Item


#CONSTANTS

WIDTH = os.get_terminal_size().columns #Height and width of terminal window
HEIGHT = os.get_terminal_size().lines
CLEAR = "\033[2J"
TO_TOP = "\033[1A" * HEIGHT #Code to jump to the top of the window

#Text variables
TEXT = "very extra cool text "
KERNING_BUFFER = " " * 2

#Basic boxes for testing
test_box = ["+++++",
            "+   +",
            "+   +",
            "+   +",
            "+++++"
            ]


#Functions

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


def generate_lines(letters):
    '''Generates the final list of lines by adding the others together
    Takes in double array of letters and returns a list of final lines'''

    final_lines = ["", "", "", "", ""]

    for l in range(len(final_lines)):
        for s in letters:
            final_lines[l] += s[l] + KERNING_BUFFER

    #for i in final_lines:
        #print(i)

    return final_lines


def parse_input(string):
    '''Takes an input string and parses it into a list of big letters (totally not swiped from big L)'''
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


def render_frame(item):
    '''Renders one frame with given data'''
    down = item.get_pos()[0]
    #right = item.get_pos()[1]
    print(f"\033[{down}B")
    #print(" " * right, end="")
    #print(f"\033[{right}C") #Moves cursor into position
    draw_item(item)


def draw_item(item):
    '''Draws an item at a given position, can be assumed to have no intersection issues'''
    #text = item.print_boxy().strip("\n")
    text = item.ready_to_print().strip("\n")

    print(text, end="")


def check_border_collision(item):
    '''Checks for collisions with the screen border,
    returns a tuple of either -1 or 1, -1 if going to hit and 1 if not,
    a jank boolean of sorts, vertical first then horizontal'''
    vert = 1
    hor = 1 #Variables for if the top or bottom will collide
    
    item_width = item.get_size()[0]
    item_height = item.get_size()[1]

    pos = item.get_pos()

    #Evaluate vertical
    if pos[0] == 1: #If going to hit top of screen
        vert = -1
    elif pos[0] + (item_height) == HEIGHT - 1: #Going to hit bottom
        vert = -1

    #Evaluate horizontal
    if pos[1] == 0: #Going to hit left
        hor = -1
    elif pos[1] + (item_width) == WIDTH: #Going to hit right
        hor = -1

    return (vert, hor)





def main():
    '''Main function'''
    letters = parse_input(TEXT.upper())
    final_text = generate_lines(letters)
    item = Boxy_Item(final_text, (1, 1), (8, 20)) #Creates an item for testing
    #item.boxy_size() #Enable if using box mode

    #Event loop
    while True:
        #Draws items
        print(CLEAR)
        #time.sleep(0.5)
        print(TO_TOP, end="")
        render_frame(item)

        #Updates position
        new_pos = item.get_pos()
        dir = item.get_dir()

        new_pos = (new_pos[0] + dir[0], new_pos[1] + dir[1]) 
        item.set_pos(new_pos)

        #Eval reflections
        check = check_border_collision(item)
        new_dir = (check[0] * dir[0], check[1] * dir[1])
        item.set_dir(new_dir)

        time.sleep(0.3)


if __name__ == "__main__":
    main()
