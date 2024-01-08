import tkinter as tk

def pulsaBoton(mensaje):
    print("has pulsado el boton")
    print("Y el mensaje es:"+mensaje)

def entraRaton(self):
    print("has entrado en el boton")
    print(self)

ventana = tk.Tk()

boton = tk.Button(ventana,text="Pulsame",command=lambda:pulsaBoton("hola"))
boton.pack(padx=20,pady=20)

boton.bind("<Enter>",entraRaton)

ventana.mainloop()
