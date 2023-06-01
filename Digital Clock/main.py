from tkinter import *
from time import *

root=Tk()
root.title("Digital Clock")

#3 Seperate Labels-1)Time 2)Day of the week 3)Date


def fun():
    try:
        timestring = strftime('%H:%M:%S %p') # %p gives AM PM   # %H coverts a clock to 24 hr
        time_label.config(text=timestring) #Converts the time which would be in tuple function to string
        root.after(1000, fun) #Makes clock update itself every 1000 millisecond[acts as arecursive function]
    

        date_string=strftime('%B %d, %Y')
        date_label.config(text=date_string)

        day_string=strftime('%A')
        day_label.config(text=day_string)

    except:
        pass

time_label=Label(root,font="Arial 50",fg="red",bg="black")
time_label.pack(anchor='center')

date_label=Label(root,font="Arial 30")
date_label.pack(anchor='center')

day_label=Label(root,font="Arial  30")
day_label.pack(anchor='center')


fun()
root.mainloop()