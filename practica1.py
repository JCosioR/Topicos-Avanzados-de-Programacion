# Practica 1
# Ventana con elementos basicos
# Alumno: Cosio Reatiga Jorge Enrique
# Materia: Topicos avanzados de programacion

import tkinter as tk
from tkinter import ttk, messagebox 

# Funcion para entrada de texto
def mostrar_mensaje():
    texto_usuario = entry.get()
    messagebox.showinfo("Mensaje", f"El texto ingresado es: {texto_usuario}")

# Inicializar ventana, asignar nombre de ventana y dimensiones
window = tk.Tk()
window.title("Exercise 1")
window.geometry("400x250")

# Inicializar la etiqueta con el mensaje de Bienvenidos
welcome = ttk.Label(window, text="Bienvenidos")
welcome.pack(pady=10)

# Llamar a la mostrar_mensaje()
entry = tk.Entry(window)
entry.pack(pady=10)

# Inicializar botón para mostrar el mensaje ingresado.
boton_mostrar = tk.Button(window, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mostrar.pack(pady=10)

# Inicializar botón para cerrar el programa
boton_cerrar = tk.Button(window, text="Cerrar", command=window.quit)
boton_cerrar.pack(pady=10)

# Llamar a la función ventana.
window.mainloop()
