import tkinter as tk
from tkinter import messagebox, Label, Tk, StringVar, CENTER, ttk

def conversor_temperatura():
    try:
        valor_temp = float(entrada_temp.get())
        tipo_conversion = sel_conversion.get()
        
        if tipo_conversion == "Celsius a Fahrenheit":
            resultado = (valor_temp * 9/5) + 32
            resultado_var.set(f"{valor_temp}°C = {resultado:.2f}°F")
        elif tipo_conversion == "Fahrenheit a Celsius":
            resultado = (valor_temp - 32) * 5/9
            resultado_var.set(f"{valor_temp}°F = {resultado:.2f}°C")
        else:
            messagebox.showerror("Error","Selecciones un tipo de conversión.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

#Configuración de la ventana principal
display = Tk()

display.title("CONVERSOR DE TEMPERATURA DE ALANIZ")  
display.geometry("400x300")
display.resizable(False, False) 

# Variables
entrada_temp = StringVar()
resultado_var = StringVar()
sel_conversion = StringVar()

# Etiquetas
Label(display, text="CONVERSOR DE TEMPERATURAS", font=("Helvetica", 16), anchor=CENTER).pack(pady=10)
Label(display, text="Ingrese el valor de la temperatura:", font=("Helvetica", 12)).pack(pady=5)

# Campo de entrada
caja_entrada = ttk.Entry(display, textvariable=entrada_temp, font=("Helvetica", 12), justify=CENTER)
caja_entrada.pack(pady=5)

# Selector de tipo de conversión
Label(display, text="Seleccione el tipo de conversion:", font=("Helvetica", 12)).pack(pady=5)
conversion_combobox = ttk.Combobox(
    display,
    textvariable=sel_conversion,
    font=("Helvetica", 12),
    state="readonly",
    values=["Celsius a Fahrenheit", "Fahrenheit a Celsius"]
)
conversion_combobox.pack(pady=5)

# Botón de conversión
boton_conversion = ttk.Button(display, text="Convertir", command= conversor_temperatura)
boton_conversion.pack(pady=10)

# Resultado
Label(display, text="Resultado:", font=("Helvetica", 12)).pack(pady=5)
rotulo_resultado = Label(display, textvariable=resultado_var, font=("Helvetica", 14), fg="blue", anchor=CENTER)
rotulo_resultado.pack(pady=5)

# Iniciar el bucle principal de la aplicación
display.mainloop()
