import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
from datetime import datetime, date, timedelta
from PIL import Image, ImageTk
import csv

# ----------------------------- FUNCIONES -----------------------------
def calcular_edad():
    try:
        fecha_nacimiento = entrada_fecha_nac.get_date()
        hoy = date.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        resultado_edad.set(f"Edad: {edad} años")
    except Exception as e:
        resultado_edad.set("Fecha inválida")
        print("DEBUG:", e)

def calcular_diferencia():
    try:
        fecha1 = cal_fecha1.get_date()
        fecha2 = cal_fecha2.get_date()

        if fecha1 > fecha2:
            fecha1, fecha2 = fecha2, fecha1

        delta = fecha2 - fecha1
        años = delta.days // 365
        meses = (delta.days % 365) // 30
        dias = (delta.days % 365) % 30

        resultado_diff.set(f"{delta.days} días\n~ {años} años, {meses} meses y {dias} días")
    except Exception as e:
        resultado_diff.set("Error al calcular fechas")
        print("DEBUG:", e)

def exportar_resultados():
    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if archivo:
        with open(archivo, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Tipo", "Resultado"])
            writer.writerow(["Edad", resultado_edad.get()])
            writer.writerow(["Diferencia", resultado_diff.get()])
        messagebox.showinfo("Exportación", "Datos exportados correctamente.")

def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Calculadora de Fechas:\n- Selecciona tu fecha de nacimiento para calcular tu edad.\n- Selecciona dos fechas para calcular la diferencia entre ellas.\n- Puedes exportar los resultados desde el menú Archivo.")

def calcular_fecha_futura():
    try:
        base_date = future_base.get_date()
        dias_extra = int(dias_sumar.get())
        nueva_fecha = base_date + timedelta(days=dias_extra)
        resultado_futuro.set(f"Nueva fecha: {nueva_fecha.strftime('%Y-%m-%d')}")
    except Exception as e:
        resultado_futuro.set("Error en el cálculo")
        print("DEBUG futuro:", e)

# ----------------------------- VENTANA PRINCIPAL -----------------------------
root = tk.Tk()
root.title("⏳ Calculadora de Fechas Suprema")
root.geometry("700x550")
root.resizable(False, False)

# ----------------------------- MENÚ -----------------------------
menubar = tk.Menu(root)
menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Exportar Resultados", command=exportar_resultados)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

menu_ayuda = tk.Menu(menubar, tearoff=0)
menu_ayuda.add_command(label="Ver Ayuda", command=mostrar_ayuda)

menubar.add_cascade(label="Archivo", menu=menu_archivo)
menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
root.config(menu=menubar)

# ----------------------------- TABS -----------------------------
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# TAB 1: Edad
frame_edad = ttk.Frame(notebook, padding=20)
notebook.add(frame_edad, text="🧓 Calcular Edad")

ttk.Label(frame_edad, text="Fecha de nacimiento:", font=("Helvetica", 14)).pack(pady=10)
entrada_fecha_nac = DateEntry(frame_edad, width=20, date_pattern='y-mm-dd')
entrada_fecha_nac.pack(pady=5)

ttk.Button(frame_edad, text="📅 Calcular Edad", command=calcular_edad).pack(pady=15)
resultado_edad = tk.StringVar()
ttk.Label(frame_edad, textvariable=resultado_edad, font=("Courier", 16)).pack()

# TAB 2: Diferencia de fechas
frame_diff = ttk.Frame(notebook, padding=20)
notebook.add(frame_diff, text="📆 Diferencia entre Fechas")

ttk.Label(frame_diff, text="Fecha 1:").grid(row=0, column=0, padx=10, pady=10)
cal_fecha1 = DateEntry(frame_diff, width=20, date_pattern='y-mm-dd')
cal_fecha1.grid(row=0, column=1, padx=10)

ttk.Label(frame_diff, text="Fecha 2:").grid(row=1, column=0, padx=10, pady=10)
cal_fecha2 = DateEntry(frame_diff, width=20, date_pattern='y-mm-dd')
cal_fecha2.grid(row=1, column=1, padx=10)

resultado_diff = tk.StringVar()
ttk.Button(frame_diff, text="🔍 Calcular Diferencia", command=calcular_diferencia).grid(row=2, column=0, columnspan=2, pady=15)
ttk.Label(frame_diff, textvariable=resultado_diff, font=("Courier", 14)).grid(row=3, column=0, columnspan=2, pady=10)

# TAB 3: Calcular fecha futura
frame_futuro = ttk.Frame(notebook, padding=20)
notebook.add(frame_futuro, text="📅 Calcular Fecha Futura")

ttk.Label(frame_futuro, text="Fecha base:").grid(row=0, column=0, padx=10, pady=10)
future_base = DateEntry(frame_futuro, width=20, date_pattern='y-mm-dd')
future_base.grid(row=0, column=1, padx=10)

ttk.Label(frame_futuro, text="Días a sumar:").grid(row=1, column=0, padx=10, pady=10)
dias_sumar = ttk.Entry(frame_futuro, width=10)
dias_sumar.grid(row=1, column=1, padx=10)

resultado_futuro = tk.StringVar()
ttk.Button(frame_futuro, text="➕ Calcular Nueva Fecha", command=calcular_fecha_futura).grid(row=2, column=0, columnspan=2, pady=15)
ttk.Label(frame_futuro, textvariable=resultado_futuro, font=("Courier", 14)).grid(row=3, column=0, columnspan=2, pady=10)

# ----------------------------- FOOTER -----------------------------
ttk.Label(root, text="🔹 Powered by Python | Diseñado por Iosu Gómez", font=("Arial", 10, "italic"), foreground="gray").pack(pady=5)

root.mainloop()
