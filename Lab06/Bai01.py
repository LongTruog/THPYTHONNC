import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Goodnight', command=lambda:
window.destroy())
button.pack()
window.mainloop()