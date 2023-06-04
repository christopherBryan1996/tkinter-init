import tkinter as tk
from tkinter import ttk
from time import sleep

ventana = tk.Tk()

textoCaja = tk.StringVar(value='valor por defecto')

alto = 500
ancho = 400

ventana.geometry(f'{alto}x{ancho}')
ventana.title("Barra de progreso")

ventana.iconbitmap("img/party_mexico_dead_donkey_mexican_pinata_icon_252385.ico")

def comenzar():
    barra.start()
    barra['maximum']=10
    for valor in range(11):
        sleep(0.1)
        barra['value']=valor
        barra.update()
    barra['value']=0
    barra.stop()
def parar():
    barra.stop()

barra = ttk.Progressbar(ventana, orient='horizontal', length=450)
barra.grid(row=0, column=1, padx=15, pady=15, columnspan=3)
btn_comenzar = ttk.Button(ventana, text='comenzar', command=comenzar)
btn_comenzar.grid(row=1, column=2)
btn_parar=ttk.Button(ventana, text='parar', command=parar)
btn_parar.grid(row=1, column=3)


ventana.mainloop()
