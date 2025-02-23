# Practica 3
# Alumno: Cosio Reatiga Jorge Enrique
# Materia: Topicos avanzados de programacion

import tkinter as tk
from tkinter import ttk, messagebox 

# Funcion para entrada de texto
#def mostrar_mensaje():
 #   texto_usuario = entry.get()
  #  messagebox.showinfo("Mensaje", f"El texto ingresado es: {texto_usuario}")

# Función para recibir datos
def enviar_datos():
    print("Nombre:", nombre.get())
    print("Correo:", correo.get())
    print("Edad:", edad.get())

def limpiar():
    nombre.delete(0, tk.END)
    correo.delete(0, tk.END)
    edad.delete(0, tk.END)


# Inicializar ventana, asignar nombre de ventana y dimensiones
window = tk.Tk()
window.title("Formulario")
window.geometry("400x250")

# Inicializar la etiqueta para el nombre, seguida del correo y de la edad
tk.Label(window, text="Nombre:").grid(row=0, column=0)
nombre = tk.Entry(window)
nombre.grid(row=0, column=1)

tk.Label(window, text="Correo:").grid(row=1, column=0)
correo = tk.Entry(window)
correo.grid(row=1, column=1)

tk.Label(window, text="Edad:").grid(row=2, column=0)
edad = tk.Entry(window)
edad.grid(row=2, column=1)

# Inicializar botón para mostrar el mensaje ingresado.
boton_enviar = tk.Button(window, text="Enviar", command=enviar_datos)
boton_enviar.grid(row=4, column=0)

# Inicializar botón para cerrar el programa
boton_limpiar = tk.Button(window, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=4, column=1)

# Llamar a la función ventana.
window.mainloop()
