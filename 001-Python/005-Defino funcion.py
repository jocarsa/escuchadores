import tkinter as tk

def pulsaBoton():
    print("has pulsado el boton")

ventana = tk.Tk()

boton = tk.Button(ventana,text="Pulsame",command=pulsaBoton)
boton.pack(padx=20,pady=20)

ventana.mainloop()
