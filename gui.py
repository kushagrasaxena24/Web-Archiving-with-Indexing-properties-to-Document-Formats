from Tkinter import *
import os
def callback():
    if var1.get() is 1:
        extct ="-x "
    else:
        extct =""

    os.chdir("C:")
    os.system('python3 main.py '+ e.get()+" "+ '"'+e2.get()+'"' )
def callback1():
    if var1.get() is 1:
        extct ="-x "
    else:
        extct =""

    os.chdir("C:")
    os.system('python web2pdf.py '+ "-u" + '"'+e2.get()+'"' )

master = Tk()
extct = ""
l1 = Label(master, text="Storage Path:")
l2 = Label(master, text="Web Page path:")

e = Entry(master)
e2 = Entry(master)
b = Button(master, text="Create EPUB", width=15, command=callback)
b2 = Button(master, text="Create PDF", width=15, command=callback1)
l1.grid(row=0)
l2.grid(row=1)

e.grid(row=0,column=1)
e2.grid(row=1,column=1)
var1 = IntVar()

#Checkbutton(master, text="Index Enabled", variable=var1).grid(row=2, column=0 )

b.grid(row=2, column=1)
b2.grid(row=2, column=0)
e2.focus_set()






master.mainloop()
