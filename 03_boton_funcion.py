import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

contador=0



def click():
    global contador 
    contador+=1
    print("boton pulsado")
    boton01.config(text=f"Has pulsado el botos de activar {contador} veces")

ventana.title("boton con funcion")
alto= 600
ancho = 800

ventana.geometry(f"{ancho}x{alto}")
ventana.iconbitmap("img/transportation_vehicle_parking_car_garage_icon_252337.ico")

boton01 = ttk.Button(ventana,text="click")
boton01.pack()

boton02 = ttk.Button(ventana, text="activar", command=click)
boton02.pack()

ventana.mainloop()