from tkinter import *
import tkinter as tk
import tkinter.ttk
import Combox
from Combox import ComboCheckbox


class ComboCheckState(tk.Frame):

    def __init__(self, master = None):
        self.__title = "ComboCheckbox"


    def create_widgets(self):
        window = tk.Tk()
        window.title(self.__title)
        window.geometry("200x200")
        root = tk.Frame(window)

        root.pack(expand = False, fill = "both")

        self.ccb_val = StringVar()
        self.orgName_tuple = ['-all-', 'SOMATIC-CELL-S1', 'SOMATIC-CELL-S2', 'SOMATIC-CELL-S3', 'SOMATIC-CELL-S4']

        '''
        self.org_combobox = tkinter.ttk.Combobox(root, values = self.orgName_tuple, width = 16)
        # self.org_combobox.bind("<<ComboboxSelected>>", self.ccbValue)
        self.org_combobox.bind("<FocusOut>", self.ccbValue)
        self.org_combobox.grid(row = 7, column = 3, sticky = 'NEW', rowspan = 2)
        '''

        # '''
        self.CCB = Combox.ComboCheckbox(root, values = ['-all-', 'SOMATIC-CELL-S1', 'SOMATIC-CELL-S2', 'SOMATIC-CELL-S3', 'SOMATIC-CELL-S4'])
        self.CCB.bind("<<ComboCheckboxFocusIn>>", self.ccbValue)
        self.CCB.pack(anchor = "w")
        # '''


        # self.CCB.bind("<<Escape>>", self.ccbValue)
        # self.CCB.bind("<<ComboCheckboxSelected>>", self.ccbValue)

        # self.CCB.bind("<<ComboCheckboxFocusOut>>", self.ccbValue)

        print(f" {self.ccb_val} from combox")


        window.mainloop()


    def ccbValue(self, event):
        print("ComboCheckbox")
        # print("ComboCheckbox: %s" % self.CCB.get())
        # self.ccb_val.set(self.CCB.get())
        # self.fetchCCBval()


    def fetchCCBval(self):
        fccbval = self.ccb_val.get()
        print(fccbval)


    










if __name__ == "__main__":
    tbm = ComboCheckState()
    tbm.create_widgets()

