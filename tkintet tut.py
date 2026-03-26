from tkinter import *

root = Tk()

# creating a label widget
mylabel1 = Label(root, text = "Hello World").grid(row = 0, column = 0)
mylabel2 = Label(root, text = "My Name is Lemmy").grid(row = 1, column = 0)

# shoving it onto the screen
# mylabel1.grid(row = 0, column = 0)
# mylabel2.grid(row = 1, column = 0)

root.mainloop()


