import time
from tkinter import Tk, Label

root = Tk()
root.title("Digital Clock")
root.configure(bg="black")


def start():
    text = time.strftime("%I:%M:%S %p")
    Label.config(text=text)
    Label.after(1000, start)


Label = Label(root, font=("ds-digital", 100), bg="black", fg="cyan")
Label.grid(row=0, column=1)
print('done')
start()

root.mainloop()
