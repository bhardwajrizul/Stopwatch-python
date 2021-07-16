from tkinter import *

root = Tk()
root.minsize(width=300, height=300)
timer = False
counter = -1


def start():
    global timer, counter
    timer = True
    button.config(state="disabled")
    buttonstop.config(state="active")
    label.after(1000, incCounter)


def incCounter():
    global counter
    counter += 1
    label.config(text=str(counter))
    if timer:
        start()


def stop():
    global timer
    timer = False
    button.config(state="active")
    buttonstop.config(state="disabled")


def reset():
    global counter, timer
    timer = False
    counter = -1

    button["state"] = "active"
    buttonstop["state"] = "disabled"
    buttonreset["state"] = "active"

    if not timer:
        label["text"] = "Stop Watch"


label = Label(root, text="Stop Watch", font=("timesnow", 20), bg="lightblue", fg="black")
label.pack(fill=BOTH)

button = Button(root, text="Start", fg="pink", bg="black", command=start)
button.pack(fill="x", ipady=7)

buttonstop = Button(root, text="Stop", fg="pink", bg="black", command=stop)
buttonstop.pack(fill="x", ipady=7)
buttonstop["state"] = "disabled"

buttonreset = Button(root, text="Reset", fg="pink", bg="black", command=reset)
buttonreset.pack(fill="x", ipady=7)

root.mainloop()
