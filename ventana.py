import tkinter as tk
from tkinter import ttk, messagebox

class Ventana(tk.Tk):
    def __init__(self, titulo, ancho, alto):
        super().__init__()
        tamaño = f'{ancho}x{alto}'
        self.geometry(tamaño)
        self.title(titulo)
        self._crea_boton()

    def _crea_boton(self):
        self.btn_click = ttk.Button(self, text='click', command=self.click)
        self.btn_click.grid(row=3, column=3, padx=20, pady=20, ipadx=10, ipady=10)

    def click(self):
        print('has pulsado el boton')

if __name__ == '__main__':
    titulo = 'mi vetana'
    ancho= 500
    alto=200
    ventana = Ventana(titulo, ancho, alto)

    ventana.mainloop()