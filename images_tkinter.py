from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")
root.iconbitmap("C:/Users/Lenny/Desktop/Programmieren/ICO Icons/iconfolder_ico.ico")


my_img = ImageTk.PhotoImage(Image.open("würfel.png"))
my_label = Label(image = my_img)
my_label.pack()













button_quit = Button(root, text = "Exit", command = root.quit)
button_quit.pack()






root.mainloop()