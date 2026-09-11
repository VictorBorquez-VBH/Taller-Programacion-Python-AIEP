import tkinter as tk
from tkinter import messagebox


def saludar():
    nombre = entrada_nombre.get()

    if nombre.strip() == "":
        messagebox.showwarning("Validación", "Debe ingresar su nombre.")
        return

    messagebox.showinfo("Bienvenido", f"Hola {nombre}")

ventana = tk.Tk()

ventana.title("Mi primera aplicación")
ventana.geometry("400x250")

etiqueta = tk.Label(ventana,text="Ingrese su nombre:")

etiqueta.pack(pady=10)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=10)


boton = tk.Button(ventana,text="Saludar",command=saludar)

boton.pack(pady=10)


ventana.mainloop()
