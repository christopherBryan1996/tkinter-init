import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

alto = 800
ancho = 600

ventana.geometry(f'{alto}x{ancho}')

ventana.title("Caja de textos")

ventana.mainloop()