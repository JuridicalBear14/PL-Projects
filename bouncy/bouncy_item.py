#Parker Lowney


class Item:
    '''Object that represents an on screen item in bouncy.py'''

    #Constructor
    def __init__(self, text, direction, pos) -> None:
        self.text = text #Text the item represends, stored as a list of lines
        self.direction = direction #The slope of the line which the item is moving along, represented in rise/run
        self.size = (len(text[0]), len(text)) #Size of thie item in tuple form (width, height)
        self.pos = pos #Position of this item in tuple form, as a distance from the top left (down, right)

        #self.boxy_text = self.text.copy() #A version  of the text to be manipulated by boxy


    #Getters
    def get_text(self):
        '''Returns text value of item in the form of a list'''
        return self.text

    def get_dir(self):
        '''Returns the direction of this item'''
        return self.direction

    def get_size(self):
        '''Returns the size as a tuple (width, height)'''
        return self.size

    def get_pos(self):
        '''Returns position of item as a tuple'''
        return self.pos

    def ready_to_print(self):
        '''Returns the value of this item as a string ready to be printed'''
        offset = " " * self.get_pos()[1] #Space offset

        final = offset + ("\n" + offset).join(self.get_text()) #Joins list with newlines and offsets
        return final

    #Setters 
    def set_dir(self, dir):
        '''Sets item direction to dir parameter'''
        self.direction = dir

    def set_pos(self, pos):
        '''Sets the item's position'''
        self.pos = pos



class Boxy_Item(Item):
    '''Item subclass for a boxy item'''

    #Constructor
    def __init__(self, text, direction, pos) -> None:
        super(Boxy_Item, self).__init__(text, direction, pos)

        self.boxy_text = self.text.copy() #A version  of the text to be manipulated by boxy
        self.boxy_size()


    #Getters
    def ready_to_print(self):
        '''Returns the ready to print value, but in a box'''
        offset = " " * self.get_pos()[1] #Space offset

        new_text = ["X" * 53]
        for n in self.boxy_text:
            new_text.append("X " + n[:50] + "X")

        new_text.append("X" * 53)
        final = offset + ("\n" + offset).join(new_text) #Joins list with newlines and offsets

        #Remove one from each line
        for i in range(len(self.boxy_text)):
            self.boxy_text[i] = self.boxy_text[i][1:]

        if len(self.boxy_text[0]) < 60: #If boxy text is short enough it re adds regular text
            for i in range(len(self.boxy_text)):
                self.boxy_text[i] += self.get_text()[i]
                #print(self.boxy_text[i])

        return final

    #Setters
    def boxy_size(self):
        '''Adds two to the size of item'''
        self.size = (53, 7)

