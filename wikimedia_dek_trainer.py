import os
from tkinter import *

# Declare input file and directory here.
inputfile = "./inputfile.txt"
pngdirectory = "./png/"

def make_inventory():
    """Transform PNG file names to words and make a dictionary of them."""
    inv = {}
    for png in os.listdir(pngdirectory):
        tag = png[(png.rfind("_-_") + 3):-4]
        word = tag.replace("_v2", "").replace("ABER", ":").replace("_", " ")
        inv[word.lower()] = os.path.join(pngdirectory, png)
    return inv

def check_inventory(sentence, inventory):
    """Return list of words if all words from sentence are in inventory."""
    string = re.sub(r"([^\s\w]|_)+", "", sentence[:-1]).lower()
    words = string.split(" ")
    if set(words).issubset(set(inventory)):
        return words
    else:
        return False

def show_off(top, outlines):
    """Display PNGs of outlines and use top window title."""
    root = Tk()
    root.geometry("+0+0")
    root.title(top)
    root.resizable(FALSE, FALSE)
    nextbutton = Button(root, text = "Neuen Satz generieren", command = root.destroy)
    nextbutton.pack(anchor = NW)
    quitbutton = Button(root, text = "Programm beenden", command = quit)
    quitbutton.pack(anchor = NW)
    for outline in outlines:
        img = PhotoImage(file = invent[outline])
        panel = Label(root, image = img)
        panel.image = img
        panel.pack(side = LEFT)
    root.mainloop()

invent = make_inventory()
with open(inputfile) as i:
    ilines = set(i.readlines())
for iline in ilines:
    outlines = check_inventory(iline, invent)
    if outlines and len(outlines) <= 12:
        show_off(iline, outlines)
    else:
        pass
