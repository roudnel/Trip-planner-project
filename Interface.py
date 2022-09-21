#### Fonction first interface ###

from tkinter import *

def Interface_Saisie():
    root = Tk()
    root.title("Trip Planner")
    lc = []
    lm = []
    def quit():
        city = city_insert.get()
        month = month_insert.get()
        lc.append(city)
        lm.append(month)
        root.destroy()
    ##
    city_label = Label(root, text='Choisissez une ville :')
    city_label.grid(row=0, column=0)
    ##
    month_label = Label(root, text='Choisissez un mois :')
    month_label.grid(pady=18, padx=18, row=0, column=2)
    ##
    city_insert = Entry(root)
    city_insert.grid(pady=18, padx=18, row=0, column=1)
    ##
    month_insert = Entry(root)
    month_insert.grid(pady=18, padx=18, row=0, column=3)
    ##
    b1 = Button(root, text='Valider votre choix', command=quit)
    b1.grid(pady=10, row=1, column=3)
    root.mainloop()
    return lc[0], lm[0]

result = Interface_Saisie()
city = str(result[0])
month = str(result[1])
