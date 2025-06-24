import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

API_KEY = "7f356ff517e14bdba0d05c5b80a2721b"

def convertir(v, o, d):
    if o == d: return v
    if o == "Fahrenheit": v = (v - 32) * 5/9
    elif o == "Kelvin": v -= 273.15
    if d == "Fahrenheit": return v * 9/5 + 32
    if d == "Kelvin": return v + 273.15
    return v

def act_conv():
    try:
        t = float(entry_temp.get())
        o, d = combo_origen.get(), combo_destino.get()
        r = convertir(t, o, d)
        label_res.config(text=f"{t:.2f}°{o[0]} → {r:.2f}°{d[0]}")
        h.append((datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), t, o, r, d))
        act_hist()
        graf_conv(t, o)
    except:
        label_res.config(text="❌ Valor inválido")

def act_hist():
    historial_box.delete(0, tk.END)
    for t, a, o, r, d in reversed(h[-20:]):
        historial_box.insert(tk.END, f"[{t}] {a}°{o[0]} → {r:.2f}°{d[0]}")

def graf_conv(t, o):
    fig_conv.clear()
    ax = fig_conv.add_subplot(111, facecolor=bg)
    keys = ["Celsius","Fahrenheit","Kelvin"]
    vals = [convertir(t, o, k) for k in keys]
    bars = ax.bar(keys, vals, color="#33aaff", edgecolor=fg)
    ax.set_facecolor(bg)
    ax.tick_params(colors=fg)
    ax.set_title("Comparación", color=fg)
    for bar in bars:
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
                f"{bar.get_height():.1f}", ha="center", color=fg)
    canvas_conv.draw()

def consultar_clima():
    ciudad, pais = entry_ciudad.get(), entry_pais.get()
    if not ciudad or not pais:
        messagebox.showwarning("", "Ciudad y país requeridos")
        return
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={API_KEY}&units=metric&lang=es"
    try:
        r = requests.get(url).json()
        main, wind, clouds = r["main"], r["wind"], r.get("clouds",{})
        vis = r.get("visibility", 0)
        datos = {
            "Temp (°C)": main["temp"], "Mín (°C)": main["temp_min"], "Máx (°C)": main["temp_max"],
            "Humedad (%)": main["humidity"], "Presión (hPa)": main["pressure"],
            "Visibilidad (m)": vis, "Viento (m/s)": wind["speed"], "Nubes (%)": clouds.get("all",0)
        }
        label_clima.config(text=f"{ciudad.title()}, {pais.upper()}\n{r['weather'][0]['description'].capitalize()}")
        graficar_clima(datos)
    except:
        messagebox.showerror("", "Error al obtener datos")

    ciudad, pais = entry_ciudad.get(), entry_pais.get()
    if not ciudad or not pais:
        messagebox.showwarning("", "Ciudad y país requeridos")
        return
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={API_KEY}&units=metric&lang=es"
    try:
        r = requests.get(url).json()
        main, wind, clouds = r["main"], r["wind"], r.get("clouds",{})
        vis = r.get("visibility", 0)
        datos = {
            "Temp": main["temp"], "Mín": main["temp_min"], "Máx": main["temp_max"],
            "Humedad": main["humidity"], "Presión": main["pressure"],
            "Visibilidad": vis, "Viento": wind["speed"], "Nubes": clouds.get("all",0)
        }
        label_clima.config(text=f"{ciudad.title()}, {pais.upper()}\n{r['weather'][0]['description'].capitalize()}")
        graficar_clima(datos)
    except:
        messagebox.showerror("", "Error al obtener datos")

def graficar_clima(datos):
    fig_clima.clear()
    ax = fig_clima.add_subplot(111, facecolor=bg)
    keys = list(datos.keys())
    vals = list(datos.values())
    bars = ax.bar(keys, vals, color="#ffa033", edgecolor=fg)
    ax.set_facecolor(bg)
    ax.tick_params(colors=fg, rotation=45)
    ax.set_title("Datos climáticos", color=fg)

    ymax = max(vals) * 1.2
    ax.set_ylim(0, ymax)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + ymax * 0.02,
                f"{height:.1f}", ha="center", color=fg)

    canvas_cli.draw()


def toggle_tema():
    global oscuro, bg, fg
    oscuro = not oscuro
    bg, fg = ("#1e1e1e","white") if oscuro else ("#f0f0f0","black")
    root.configure(bg=bg)
    for w in root.winfo_children(): 
        try: w.configure(bg=bg, fg=fg)
        except: pass
    for frame in [f1, f2, f3, f4]:
        for w in frame.winfo_children():
            try: w.configure(bg=bg, fg=fg)
            except: pass
    fig_conv.patch.set_facecolor(bg)
    fig_clima.patch.set_facecolor(bg)
    graf_conv(0, "Celsius")
    graficar_clima({})

root = tk.Tk()
root.title("🌡️ Clima & Conversor")
root.geometry("800x800")
oscuro = False
bg, fg = "#f0f0f0", "black"
h = []

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI",12))
style.configure("TButton", font=("Segoe UI",12))
style.configure("TCombobox", font=("Segoe UI",12))

nb = ttk.Notebook(root)
f1,f2,f3,f4 = [ttk.Frame(nb) for _ in range(4)]
nb.add(f1,text="Conversión")
nb.add(f2,text="Clima")
nb.add(f3,text="Historial")
nb.add(f4,text="Acerca")
nb.pack(expand=True,fill="both")

ttk.Label(f1,text="Temp:").pack(pady=5)
entry_temp = ttk.Entry(f1,justify='center'); entry_temp.pack()
ttk.Label(f1,text="De:").pack()
combo_origen = ttk.Combobox(f1, values=["Celsius","Fahrenheit","Kelvin"]); combo_origen.current(0); combo_origen.pack()
ttk.Label(f1,text="A:").pack()
combo_destino = ttk.Combobox(f1, values=["Celsius","Fahrenheit","Kelvin"]); combo_destino.current(1); combo_destino.pack()
ttk.Button(f1,text="Convertir",command=act_conv).pack(pady=10)
label_res = ttk.Label(f1,text="",font=("Segoe UI",14)); label_res.pack()
fig_conv = plt.Figure(figsize=(5,3), dpi=100)
canvas_conv = FigureCanvasTkAgg(fig_conv, master=f1)
canvas_conv.get_tk_widget().pack()

ttk.Label(f2,text="Ciudad:").pack()
entry_ciudad = ttk.Entry(f2); entry_ciudad.pack()
ttk.Label(f2,text="País (ej: es, us):").pack()
entry_pais = ttk.Entry(f2); entry_pais.pack()
ttk.Button(f2,text="Buscar",command=consultar_clima).pack(pady=5)
label_clima = ttk.Label(f2,text="",font=("Segoe UI",12),justify="center"); label_clima.pack(pady=5)
fig_clima = plt.Figure(figsize=(5,5), dpi=100)
canvas_cli = FigureCanvasTkAgg(fig_clima, master=f2)
canvas_cli.get_tk_widget().pack()

ttk.Label(f3,text="Historial:").pack()
historial_box = tk.Listbox(f3,font=("Segoe UI",11),height=20)
historial_box.pack(fill="both",expand=True,padx=10,pady=10)

info = "App para convertir temperaturas y ver el clima con todos los datos incluidos."
ttk.Label(f4,text=info,wraplength=700,justify="left").pack(padx=10,pady=10)

ttk.Button(root,text="🌗 Tema",command=toggle_tema).pack(pady=5)

root.configure(bg=bg)
root.mainloop()
