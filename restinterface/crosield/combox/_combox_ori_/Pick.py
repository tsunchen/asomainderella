import tkinter.ttk as ttk
from tkinter import *

class Pick(ttk.Frame):
    def __init__(self, master = None, values = [], entry_idw = None,
                 activebackground = '#b1dcfb', activeforeground = 'black',
                 selectbackground = '#003eff', selectforeground = 'white',
                 command = None, borderwidth = 1, relief = "solid"):
        self._selected_item = None
        self._values = values
        self._entry_idw = entry_idw
        self._sel_bg = selectbackground
        self._sel_fg = selectforeground
        self._act_bg = activebackground
        self._act_fg = activeforeground
        self._command = command
        self.index = 0
        ttk.Frame.__init__(self, master, borderwidth = borderwidth, height = 10, relief = relief)
        self.bind("<FocusIn>", lambda event: self.event_generate('<<PickFocusIn>>'))
        self.bind("<FocusOut>", lambda event: self.event_generate('<<PickFocusOut>>'))
        F = LabelFrame(self)
        F.pack(fill = 'x')
        self.canvas = Canvas(F, scrollregion = (0, 0, 500, (len(self._values) * 23)))
        vbar = Scrollbar(F, orient = VERTICAL)
        vbar.pack(side = RIGHT, fill = Y)

        frame = Frame(self.canvas)
        vbar.config(command = self.canvas.yview)

        sbar2 = Scrollbar(F, orient = HORIZONTAL)
        sbar2.pack(side = BOTTOM, fill = X)

        # self.canvas.pack(side = 'left', fill = 'x', expand = True)
        self.canvas.create_window((0, 0,), window = frame, anchor = 'nw', tags = 'frame')

        self.canvas.config(highlightthickness = 0)
        vbar.config(command = self.canvas.yview)
        sbar2.config(command = self.canvas.xview)
        self.canvas.config(width = 300, height = 150)
        self.canvas.config(yscrollcommand = vbar.set, xscrollcommand = sbar2.set)
        # self.canvas.config(scrollregion = self.canvas.bbox('all'))
        # self._font = tkFont.Font()
        self.dict_checkbutton = {}
        self.dict_checkbutton_var = {}
        self.dict_intvar_item = {}
        for index, item in enumerate(self._values):
            self.dict_intvar_item[item] = IntVar()
            self.dict_checkbutton[item] = ttk.Checkbutton(frame, text = item, variable = self.dict_intvar_item[item],
                                                          command = lambda ITEM = item: self._command(ITEM))
            self.dict_checkbutton[item].grid(row = index, column = 0, sticky = NSEW, padx = 5)
            self.dict_intvar_item[item].set(0)
            if item in self._entry_idw.get().split(','):
                self.dict_intvar_item[item].set(1)
        self.canvas.pack(side = LEFT, expand = True, fill = BOTH)
        self.canvas.bind("<MouseWheel>", self.processWheel)
        frame.bind("<MouseWheel>", self.processWheel)
        for i in self.dict_checkbutton:
            self.dict_checkbutton[i].bind("<MouseWheel>", self.processWheel)
        self.bind("<MouseWheel>", self.processWheel)


    def processWheel(self, event):
        if int(-(event.delta)) > 0:
            self.canvas.yview_scroll(1, UNITS)
        else:
            self.canvas.yview_scrool(-1, UNITS)