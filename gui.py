import tkinter as tk
from tkinter import filedialog, Text
import os
from functools import partial

root = tk.Tk()
apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps=[x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def remove(lb):
    global apps
    selection = lb.curselection()
    for item in selection:
        del apps[item] 
        lb.delete(item)

def removeApps():
    global apps
    top = tk.Toplevel()
    canvas = tk.Canvas(top, height=500, width=500, bg="#263D42")
    canvas.pack()
    frame = tk.Frame(top, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    lb = tk.Listbox(frame, height=300, width=300)
    lb.pack()
    counter=0
    for app in apps:
        lb.insert(counter, app)
        counter+=1
    action_with_arg = partial(remove, lb)
    tk.Button(top, text="Remove", padx=10, pady=6, fg="white", bg="#263D42", command=action_with_arg).pack()
    
    

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=6, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=6, fg="white", bg="#263D42", command=runApps)
runApps.pack()

removeApps = tk.Button(root, text="Remove Apps", padx=10, pady=6, fg="white", bg="#263D42", command=removeApps)
removeApps.pack()

for app in apps:
    label=tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
