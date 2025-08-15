from tkinter import *
from Combox import ComboCheckbox

if __name__ == "__main__":
    root = Tk()
    root.geometry("200x200")

    main = Frame(root)
    main.pack(expand = False, fill = "both")

    root.ccb_val = StringVar()

    root.CCB1 = ComboCheckbox(main, values = ['SOMATIC-CELL-S1', 'SOMATIC-CELL-S2', 'SOMATIC-CELL-S3', 'SOMATIC-CELL-S4'])

    root.CCB1.bind("<<ComboCheckboxSelected>>", root.CCB1.put())
    # root.CCB1.bind("<<ComboCheckboxFocusOut>>", root.CCB1.put())

    root.ccb_val = root.CCB1.get
    print(f" {root.ccb_val} from combox")

    root.CCB1.pack(anchor = "w")

    root.mainloop()

