import tkinter as tk
from tkinter import ttk, Menu
import sys # para salir de la aplicacion

ventana = tk.Tk()

textoCaja = tk.StringVar(value='valor por defecto')

alto = 800
ancho = 600

ventana.geometry(f'{alto}x{ancho}')
ventana.title("Plantilla")

ventana.iconbitmap("img/party_mexico_dead_donkey_mexican_pinata_icon_252385.ico")

def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()

#menu
def menu():
    menu_principal = Menu(ventana)

    menu_archivo = Menu(menu_principal, tearoff=0)
    menu_archivo.add_command(label="Nuevo")
    menu_archivo.add_separator()
    menu_archivo.add_command(label='Salir', command=salir)

    menu_ayuda = Menu(menu_principal, tearoff=0)
    menu_ayuda.add_command(label="Acerca de")
    
    menu_principal.add_cascade(menu=menu_archivo,label='Archivo')
    menu_principal.add_cascade(menu=menu_ayuda,label='Ayuda')

    ventana.config(menu=menu_principal)

menu()
ventana.mainloop()