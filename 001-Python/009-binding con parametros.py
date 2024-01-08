import tkinter as tk

def pulsaBoton(mensaje):
    print("has pulsado el boton")
    print("Y el mensaje es:"+mensaje)

def entraRaton(mensaje):
    print("has entrado en el boton")
    print(mensaje)

ventana = tk.Tk()

boton = tk.Button(ventana,text="Pulsame",command=lambda:pulsaBoton("hola"))
boton.pack(padx=20,pady=20)

boton.bind("<Enter>",lambda event:entraRaton("hola"))

ventana.mainloop()
