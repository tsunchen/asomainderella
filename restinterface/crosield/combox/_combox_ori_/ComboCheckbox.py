import tkinter.ttk as ttk
from tkinter import *
from Pick import Pick


class ComboCheckbox(ttk.Combobox, Pick):
    def __init__(self, master, values = [], entryvar = None, entrywidth = None,
                 entrystyle = None, onselect = None,
                 activebackground = '#ef476f', activeforeground = 'red', 
                 selectbackground = '#ffd166', selectforeground = 'green',
                 borderwidth = 1, relief = "solid"):
        self.values = values
        self.master = master
        self.activeforeground = activeforeground
        self.activebackground = activebackground
        self.selectforeground = selectforeground
        self.selectbackground = selectbackground
        self.resval = []

        if entryvar is not None:
            self.entry_var = entryvar
        else:
            self.entry_var = StringVar()

        entry_config = {}
        if entrywidth is not None:
            entry_config["width"] = entrywidth

        if entrystyle is not None:
            entry_config["style"] = entrystyle

        ttk.Entry.__init__(self, master, textvariable = self.entry_var, **entry_config, state = "")

        self._is_menuoptions_visible = False
        self.pick_frame = Pick(self.winfo_toplevel(), values = values, entry_idw = self.entry_var,
                               activebackground = activebackground, activeforeground = activeforeground,
                               selectbackground = selectbackground, selectforeground = selectforeground,
                               command = self._on_selected_check
                              )
        self.bind_all("<1>", self._on_click, "+")

        self.bind("<Escape>", lambda event: self.hide_pick())

        self.bind("<FocusOut>", lambda event: self.event_generate('<<ComboCheckboxFocusOut>>'))


    @property
    def current_value(self):
        try:
            value = self.entry_var.get()
        except ValueError:
            return None


    @current_value.setter
    def current_value(self, INDEX):
        self.entry_var.set(self.values.index(INDEX))


    def _on_selected_check(self, SELECTED):
        if self.entry_var.get() != "" and self.entry_var.get() != None:
            temp_value = self.entry_var.get()
            self.resval = temp_value.split(",")

        if str(SELECTED) in self.resval:
            if 'allsel' == str(SELECTED):
                self.resval.clear()
            else:
                self.resval.remove(str(SELECTED))
                ## self.resval.sort()
        else:
            if 'allsel' == str(SELECTED):
                self.resval = self.values
            else:
                self.resval.append(str(SELECTED))
                ## self.resval.sort()

        temp_value = ""
        for index, item in enumerate(self.resval):
            if item != "":
                if index != 0:
                    temp_value += ","
                temp_value += str(item)
        self.entry_var.set(temp_value)

        if 'allsel' == str(SELECTED):
            self.hide_pick()
            self.show_pick()


    def _on_click(self, event):
        str_widget = str(event.widget)
        if str_widget == str(self):
            if not self._is_menuoptions_visible:
                self.show_pick()
        else:
            if not str_widget.startswith(str(self.pick_frame)) and self._is_menuoptions_visible:
                self.hide_pick()


    def hide_pick(self):
        if self._is_menuoptions_visible:
            self.pick_frame.place_forget()
            # self.pick_frame.destory()
        self._is_menuoptions_visible = False
        self.get()


    def show_pick(self):
        if not self._is_menuoptions_visible:
            self.pick_frame = Pick(self.winfo_toplevel(), values = self.values,
                                   entry_idw = self.entry_var,
                                   activebackground = self.activebackground, activeforeground = self.activeforeground,
                                   selectbackground = self.selectbackground, selectforeground = self.selectforeground,
                                   command = self._on_selected_check)
            self.bind_all("<1>", self._on_click, "+")
            self.bind("<Escape>", lambda event: self.hide_pick())
            self.pick_frame.lift()
            self.pick_frame.place(in_ = self, relx = 0, rely = 1, relwidth = 1)
        self._is_menuoptions_visible = True


    def get(self):
        print(self.resval)


    def put(self, objtar):
        objtar = self.get()