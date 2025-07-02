# Purpose: this program uses read-only and input fields within a GUI
# Purpose: to create a window with Entry fields and labels.
# important: pack makes the component visisble. fill argument to BOTH and expand to True
# automatically resizes itself.
import tkinter as tk
import tkinter as ttk
from turtle import mainloop

# root window
root = tk.Tk()
root.title("Future Value Calculator")
root.geometry("300x150")

# frame
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# how to create a label and display it
# a label is a component that displays text. can be used to identify another component such as an entry field
ttk.Label(frame, text="Monthly Investment").pack()

# how to create a text field and bind it to a StringVar object
investmentText = tk.StringVar()
investmentEntry = ttk.Entry(frame, width=25, textvariable=investmentText)

# This is needed to actually display the Entry field. 
# Text did not say that
investmentEntry.pack()

# future value read-only
ttk.Label(frame, text="Future Value").pack()

# how to create a read-only text entry field and bind it to a StringVar object
fvText = tk.StringVar()
fvEntry = ttk.Entry(frame, width=25, textvariable=fvText, state="readonly")

# Same thing here
fvEntry.pack()

# how to get or set a string in a text entry field
investment = investmentText.get()
fvText.set("$2,000")

root.mainloop()

if __name__ == "__main__":
    mainloop()