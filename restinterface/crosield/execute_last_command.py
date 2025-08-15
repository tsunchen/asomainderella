import tkinter as tk

def command1():
    print("Command 1 executed")
    last_command[0] = command1
    btn_last_command.config(text="Execute Command 1 Again")

def command2():
    print("Command 2 executed")
    last_command[0] = command2
    btn_last_command.config(text="Execute Command 2 Again")

def execute_last_command():
    if last_command[0]:
        last_command[0]()
    else:
        print("No command executed yet")

root = tk.Tk()

# Initialize the list with None to track the last command
last_command = [None]

# Buttons to execute command1 and command2
btn1 = tk.Button(root, text="Execute Command 1", command=command1)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Execute Command 2", command=command2)
btn2.pack(pady=10)

# Button to execute the last executed command
btn_last_command = tk.Button(root, text="Execute Last Command", command=execute_last_command)
btn_last_command.pack(pady=10)

root.mainloop()
