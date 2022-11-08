#Created By Parker Lowney 7/31/21

from tkinter import *

root = Tk()
root.geometry("600x500")
root.title("PCypher")
root.config(background = "gray")


entry = Entry(root, font = "calibri 15")
entry.place(relx = 0.25, rely = 0.4, relwidth = 0.5)

Bdecode = Button(root, text = "Decode", font = "calibri 15", command = lambda: decode())
Bdecode.place(relx =  0.2, rely = 0.55, relwidth = 0.15, relheight = 0.15)

Bencode = Button(root, text = "Encode", font = "calibri 15", command = lambda: encode())
Bencode.place(relx =  0.65, rely = 0.55, relwidth = 0.15, relheight = 0.15)


#Encodes a given phrase
def encode():
    global entry

    phrase = entry.get()
    entry.delete(0, "end")

    phrase = phrase + " "
    on = True
    start = 0 #Starting point for each word
    newPhrase = "" #Output phrase

    while on:
        end = phrase.index(" ", start) #Sets the end to the next space after start
        word = phrase[start: end]
        
        #Loops through word and sets each letter
        for i in range(len(word)): 
            newChar =ord(word[i]) + len(word) #Turns given letter to ASCII, then adds length of word, then converts back to character and adds to new phrase

            if newChar > ord("z"): #Deals with wrapping around
                newChar -= 26

            newPhrase = newPhrase + chr(newChar)
            #word.replace(word[i], chr(ord(word[i]) + len(word)), 1)

        newPhrase = newPhrase + " " #Adds a space for the next word

        start = end + 1 #Sets start to the next word

        if start >= len(phrase): #If start is past the end, that was the last word
            on = False

    newPhrase = newPhrase[0: len(newPhrase) - 1] #Removes extra space
    entry.insert(0, newPhrase)
    #return newPhrase




#Decodes a given phrase
def decode():
    global entry

    phrase = entry.get().lower()
    entry.delete(0, "end")

    phrase = phrase + " "
    on = True
    start = 0 #Starting point for each word
    newPhrase = "" #Output phrase

    while on:
        end = phrase.index(" ", start) #Sets the end to the next space after start
        word = phrase[start: end]
        
        #Loops through word and sets each letter
        for i in range(len(word)): 
            newChar =ord(word[i]) - len(word) #Turns given letter to ASCII, then adds length of word, then converts back to character and adds to new phrase

            if newChar < ord("a"): #Deals with wrapping around
                newChar += 26

            newPhrase = newPhrase + chr(newChar)
            #word.replace(word[i], chr(ord(word[i]) + len(word)), 1)

        newPhrase = newPhrase + " " #Adds a space for the next word

        start = end + 1 #Sets start to the next word

        if start >= len(phrase): #If start is past the end, that was the last word
            on = False

    newPhrase = newPhrase[0: len(newPhrase) - 1] #Removes extra space
    entry.insert(0, newPhrase)
    #return newPhrase



running = True


root.mainloop()



'''#User loop
while running:

    print("Input a phrase to be converted!")
    phrase = input().lower()
    print("Would you like to encode or decode this phrase?")
    inputt = input().lower()

    if inputt == "decode":
        print(decode(phrase))

    elif inputt == "encode":
        print(encode(phrase))

    elif inputt == "quit":
        running = False
        
    else:
        print("Please say \"encode\" or \"decode\"")'''