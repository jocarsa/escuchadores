import tkinter as tk

ventana = tk.Tk()

boton = tk.Button(ventana,text="Pulsame",command=pulsaBoton)
boton.pack(padx=20,pady=20)

ventana.mainloop()
