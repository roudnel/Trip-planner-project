from tkinter import *
from tkinter import messagebox
 
def error():
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    messagebox.showerror('Trip planner Error', 'Veuillez insérer au moins un critère de recherche')
    root.destroy()
 
error()