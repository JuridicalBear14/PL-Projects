#Parker Lowney

import tkinter as t
import math as m

root = t.Tk()
root.geometry("300x300")
root.configure(background = "dim gray")
root.title("Pixel Measure")

p1_label = t.Label(root, width = 40, height = 1, background = "blue", text = "Point 1")
p1_label.pack()

p1 = t.Label(root, width = 40, height = 2, background = "gray", text = "[None]")
p1.pack()

p2_label = t.Label(root, width = 40, height = 1, background = "red", text = "Point 2")
p2_label.pack()

p2 = t.Label(root, width = 40, height = 2, background = "gray", text = "[None]")
p2.pack()

dist_label = t.Label(root, width = 40, height = 1, background = "Green", text = "Distance")
dist_label.pack()

dist = t.Label(root, width = 40, height = 2, background = "gray", text = "[None]")
dist.pack()

point1 = None
point2 = None

def on_press(event):
    '''Method that handles key presses'''
    global point1
    global point2


    if event.char == "x": #Exit sequence
        root.destroy()

    elif event.char in (" ", "\n", "n"):

        if point1 is None: #If the first point isn't set
            point1 = root.winfo_pointerxy()
            p1.config(text = f"{point1}")
            #print("-" * 10) #Makes a top border
            #print(f"Point 1: {point1}")

        else: #If the first point is set
            point2 = root.winfo_pointerxy()
            p2.config(text = f"{point2}")

            x = abs(point1[0] - point2[0])
            y = abs(point1[1] - point2[1])

            dist.config(text = str(calc_distance(x, y)))
            #print(f"Point 2: {point2}")
            #print("-" * 10) #Makes a bottom border

    elif event.char == "r":
        point1 = None
        point2 = None
        p1.config(text = "[None]")
        p2.config(text = "[None]")
        dist.config(text = "[None]")

def calc_distance(i, n):
    '''Calculates distance between two coordinate points'''
    output = round(m.sqrt((i * i) + (n * n)), 2)
    return output


print("RUNNING")
root.bind("<KeyPress>", on_press)
root.mainloop()
