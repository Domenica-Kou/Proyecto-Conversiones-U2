import tkinter as tk
from tkinter import ttk, messagebox

def conversion_longitud(conversion, valor):
    if conversion == "Metros a Kilómetros":
        return valor / 1000, "kilómetros"
    elif conversion == "Pulgadas a Metros":
        return valor * 0.0254, "metros"
    
def conversion_masa(conversion, valor):
    if conversion == "Kilogramos a Gramos":
        return valor * 1000, "gramos"
    elif conversion == "Libras a Kilogramos":
        return valor * 0.453592, "kilogramos"
    
def conversion_tiempo(conversion, valor):
    if conversion == "Segundos a Minutos":
        return valor / 60, "minutos"
    elif conversion == "Horas a Días":
        return valor / 24, "días"

def realizar_conversiones(combo, entrada, resultado_label, funcion_conversion):
    try: 
        valor = float(entrada.get())
        conversion = combo.get()
        resultado, unidad = funcion_conversion(conversion, valor)
        resultado_label.config(text="Resultado: " + str(round(resultado, 4)) + " " + unidad)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

def mostrar_converiones(conversion_a_realizar):
    ventana = tk.Tk()
    ventana.title("Conversión de " + conversion_a_realizar)
    ventana.geometry("400x300")
    ventana.configure(bg="#d8a3ee")

    if conversion_a_realizar == "Longitud":
        conversiones = ["Metros a Kilómetros", "Pulgadas a Metros"]
        funcion = conversion_longitud
    elif conversion_a_realizar == "Masa":
        conversiones = ["Kilogramos a Gramos", "Libras a Kilogramos"]
        funcion = conversion_masa
    elif conversion_a_realizar == "Tiempo":
        conversiones = ["Segundos a Minutos", "Horas a Días"]
        funcion = conversion_tiempo

    tk.Label(ventana, text="Conversión de " + conversion_a_realizar, bg="#d8a3ee", font=("Courier", 14)).pack(pady=10)
    tk.Label(ventana, text="Selecciona tipo de conversión:", bg="#d8a3ee", font=("Courier", 12)).pack()

    combo = ttk.Combobox(ventana, values=conversiones, state="readonly", font=("Courier", 12))
    combo.pack(pady=5)
    combo.current(0)

    tk.Label(ventana, text="Valor a convertir:", bg="#d8a3ee", font=("Courier", 12)).pack()
    entrada = tk.Entry(ventana, font=("Courier", 12))
    entrada.pack(pady=5)

    resultado_label = tk.Label(ventana, text="Resultado: ", bg="#d8a3ee", font=("Courier", 12))
    resultado_label.pack(pady=10)

    boton_convertir = tk.Button(
        ventana,
        text="Convertir",
        command=lambda: realizar_conversiones(combo, entrada, resultado_label, funcion),
        bg="#763193", fg="white",
        font=("Courier", 12)
    )
    boton_convertir.pack(pady=10)

    ventana.mainloop()

def mostrar_menu():
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú de Conversiones")
    ventana_menu.geometry("300x250")
    ventana_menu.configure(bg="#d8a3ee")

    tk.Label(ventana_menu, text="Selecciona una opción:", bg="#d8a3ee", font=("Courier", 14)).pack(pady=15)

    tk.Button(ventana_menu, text="Conversión de Longitud", command=lambda:mostrar_converiones("Longitud"), font=("Courier", 12), bg="#a74ccd").pack(pady=5)
    tk.Button(ventana_menu, text="Conversión de Masa", command=lambda:mostrar_converiones("Masa"), font=("Courier", 12), bg="#a74ccd").pack(pady=5)
    tk.Button(ventana_menu, text="Conversión de Tiempo", command=lambda:mostrar_converiones("Tiempo"), font=("Courier", 12), bg="#a74ccd").pack(pady=5)

    ventana_menu.mainloop()

mostrar_menu()