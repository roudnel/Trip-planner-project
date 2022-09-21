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
        
    Label(root, text="Faites le choix du mois auquel vous voulez partir :").grid(row=0, columnspan=4)
    
    for i in range(0,6):
        Label(root, text=list(dict_meteo)[i]).grid(row=i+1, column=0, sticky=E)
        Radiobutton(root, text=dict_meteo.get(list(dict_meteo)[i]), variable=month, value=list(dict_meteo)[i]).grid(row=i+1, column= 1, sticky=W)
    
    for i in range(6,12):
        Label(root, text=list(dict_meteo)[i]).grid(row=i-5, column=2, sticky=E)
        Radiobutton(root, text=dict_meteo.get(list(dict_meteo)[i]), variable=month, value=list(dict_meteo)[i]).grid(row=i-5, column= 3, sticky=W)

    Button(root, text='Confirmer', command=quit).grid(row=12, column=3)
    mainloop()
    return month2




