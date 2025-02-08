import tkinter as tk
from tkinter import ttk, messagebox 

def mostrar_mensaje():
    texto_usuario = entry.get()
    messagebox.showinfo("Mensaje", f"El texto ingresado es: {texto_usuario}")

window = tk.Tk()
window.title("Exercise 1")
window.geometry("400x250")

welcome = ttk.Label(window, text="Bienvenidos")
welcome.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

boton_mostrar = tk.Button(window, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mostrar.pack(pady=10)

boton_cerrar = tk.Button(window, text="Cerrar", command=window.quit)
boton_cerrar.pack(pady=10)

window.mainloop()
