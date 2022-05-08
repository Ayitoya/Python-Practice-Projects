from cProfile import label
from re import A
from tkinter import *
from datetime import date, datetime
from time import strftime
from tkinter import font
from pip import main
    # Window size and position
w=Tk()
w.geometry("750x200")
w.minsize(750,200)
w.title("DIgital Clock")
f1=Frame(w, width=750, height=200, bg="#0e1013")
f1.place(x=0,y=0)
    # Day
a=datetime.today().strftime("%A")
b=a.upper()
c=b[0:2]
    # Time function
def time():
    a=strftime('%H : %M : %S')
    l1.config(text=a)
    l1.after(1000,time)
    # GUI Design for time
l1 =Label(f1, font=('Century Gothic',60),bg='black', foreground='#d3d3d3')
l1.place(x=270,y=35)
l2=Label(f1, font=('Century Gothic',60),bg='black', foreground='#d3d3d3')
l2.config(text=c+" |")
l2.place(x=80,y=35)
    # Call time function
time()
w.mainloop()