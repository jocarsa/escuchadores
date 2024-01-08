import tkinter as tk

def pulsaBoton(mensaje):
    print("has pulsado el boton")
    print("Y el mensaje es:"+mensaje)

ventana = tk.Tk()

boton = tk.Button(ventana,text="Pulsame",command=pulsaBoton("hola"))
boton.pack(padx=20,pady=20)

ventana.mainloop()
