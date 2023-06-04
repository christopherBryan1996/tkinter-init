import tkinter as tk
from tkinter import ttk

#creamos objeto de la clase tk
ventana =tk.Tk()
ancho = 800
alto=600
tamaño =f'{ancho}x{alto}'

#tamaño
ventana.geometry(tamaño)
#titulo
ventana.title("Tabs")

control_tab = ttk.Notebook(ventana)

tab01 = ttk.Frame(control_tab)
control_tab.add(tab01, text="Tab 01")
control_tab.pack(fill='both') #rellena todo el espacio
txt_nombre = ttk.Entry(tab01,width=40)
txt_nombre.grid(row=0,column=0,padx=10,pady=10)

tab02 = ttk.LabelFrame(control_tab,text='Tab con etiqueta')
control_tab.add(tab02, text="Tab 02")
btn_pulsar = ttk.Button(tab02, text='Click')
btn_pulsar.grid(row=0, column=0, padx=10, pady=10)

#importante poner, para q se ejecute continuamente 
ventana.mainloop()