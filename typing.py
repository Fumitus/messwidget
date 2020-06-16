import tkinter


window = tkinter.Tk()
window.title("Typing detect")


def on_key_press(event):
    print("User is typing", repr(event.char))


if __name__ == '__main__':

    frame = tkinter.Label(window, text="Demo window")
    frame.bind("<KeyPress>", on_key_press)

    # pack() reikalaingas pavaizduoti objekt1 lange
    frame.pack()
    frame.focus_set()

    window.mainloop()
