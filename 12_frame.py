import tkinter as tk
from tkinter import ttk, Frame, PhotoImage
from PIL import Image,ImageTk

ventana = tk.Tk()

textoCaja = tk.StringVar(value='valor por defecto')

alto = 800
ancho = 600

ventana.geometry(f'{alto}x{ancho}')
ventana.title("Imagen en Frame")

ventana.iconbitmap("img/party_mexico_dead_donkey_mexican_pinata_icon_252385.ico")

frame = Frame(ventana)
frame.pack(padx=10, pady=10)
frame.config(bg='lightblue')
frame.config(width=400,height=300)
frame.config(cursor='pirate')
frame.config(relief='sunken')
frame.config(bd=25)

#nos ayuda para cargar cualquier imagen
imagen = ImageTk.PhotoImage(Image.open("img/descarga (1).jfif"))
#solo acepta png
#imagen = PhotoImage(file='img/images.png')
lbl_imagen = ttk.Label(frame, image=imagen).pack()

ventana.mainloop() 