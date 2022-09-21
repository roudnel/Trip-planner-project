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
    
    Label(root, text="Faites un choix parmis les 10 meilleures villes pour le mois choisi :").grid(row=0, columnspan=2)
    
    for i in range(0,5):
        Radiobutton(root, text=cities[i], variable=city, value=cities[i]).grid(row=i+1, column= 0, sticky=W)
    
    for i in range(5,10):
        Radiobutton(root, text=cities[i], variable=city, value=cities[i]).grid(row=i-4, column= 1, sticky=W)

    
    Button(root, text='Confirmer', command=quit).grid(row=10, column=1)
    mainloop()    
    return city2