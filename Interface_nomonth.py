#### Interface if no month selected ###
from tkinter import *

def month_choice(dict_meteo):
    root = Tk()
    root.title("Trip Planner")
    month = StringVar()
    month2 =[]
    def quit():
        month2.append(month.get())
        root.destroy()
        
    for i in range(0,12):
        Label(root, text=list(dict_meteo)[i]).grid(row=i, column=0, sticky=E)
        Radiobutton(root, text=dict_meteo.get(list(dict_meteo)[i]), variable=month, value=list(dict_meteo)[i]).grid(row=i, column= 1, sticky=W)
    
    Button(root, text='Confirmer', command=quit).grid(row=12, column=1)
    mainloop()
    return month2




