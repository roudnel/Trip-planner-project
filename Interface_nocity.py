### Interface if no city got see
from tkinter import *

def city_choice(cities):
    root = Tk()
    root.title("Trip Planner")
    city = StringVar()
    city2 =[]
    def quit():
        city2.append(city.get())
        root.destroy()
        
    for i in range(0,10):
        Radiobutton(root, text=cities[i], variable=city, value=cities[i]).grid(row=i, column= 0, sticky=W)
    
    Button(root, text='Confirmer', command=quit).grid(row=10, column=0)
    mainloop()    
    return city2