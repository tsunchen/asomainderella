from tkinter import *
from ComboCheckbox import ComboCheckbox

if __name__ == "__main__":
    root = Tk()
    root.geometry("200x200")

    CCB = StringVar()

    main = Frame(root)
    main.pack(expand = False, fill = "both")
    CCB1 = ComboCheckbox(main, values = ['CELL-S1', 'CELL-S2', 'CELL-S3', 'CELL-S4'])
    CCB1.pack(anchor = "w")
    root.mainloop()

