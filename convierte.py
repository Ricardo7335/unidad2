import tkinter as tk
from tkinter import Tk

def convertir_base(base):
    try:
        numero = int(entrada_numero.get())
        if base == 'bin':
            resultado.set(f"Binario: {bin(numero)[2:]}")
        elif base == 'oct':
            resultado.set(f"Octal: {oct(numero)[2:]}")
        elif base == 'hex':
            resultado.set(f"Hexadecimal: {hex(numero)[2:].upper()}")
    except ValueError:
        resultado.set("Por favor, ingresa un número válido.")
ventana = tk.Tk()
ventana.title("Rosal Castillo Ricardo")
ventana.geometry("400x250")
ventana.configure(bg="white")
titulo = tk.Label(ventana, text="Convertir Numeros", font=("Arial", 16, "bold"), bg="light blue", fg="gray")
titulo.pack(pady=10)
entrada_numero = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada_numero.pack(pady=5)
resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Arial", 14), bg="white", fg="black")
etiqueta_resultado.pack(pady=10)
frame_botones = tk.Frame(ventana, bg="white")
frame_botones.pack(pady=10)
boton_binario = tk.Button(frame_botones, text="Binario", command=lambda: convertir_base('bin'), bg="pink", font=("Arial", 12), width=10)
boton_binario.grid(row=0, column=0, padx=5)
boton_octal = tk.Button(frame_botones, text="Octal", command=lambda: convertir_base('oct'), bg="pink", font=("Arial", 12), width=10)
boton_octal.grid(row=0, column=1, padx=5)
boton_hex = tk.Button(frame_botones, text="Hexadecimal", command=lambda: convertir_base('hex'), bg="pink", font=("Arial", 12), width=10)
boton_hex.grid(row=0, column=2, padx=5)
ventana.mainloop()