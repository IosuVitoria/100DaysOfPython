import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from math import pi
from PIL import Image, ImageTk
import os
import datetime

class AreaCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📐 Calculadora de Áreas - Geometría")
        self.root.geometry("820x750")
        self.root.configure(bg="#ecf0f1")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        self.historial = []

        self.customize_style()
        self.setup_menu()
        self.setup_ui()
        self.status_var = tk.StringVar()
        self.create_status_bar()

    def customize_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 11), padding=6)
        style.configure("TLabel", font=("Segoe UI", 11), background="#ecf0f1")
        style.configure("TCombobox", font=("Segoe UI", 11))
        style.configure("TEntry", font=("Segoe UI", 11))

    def setup_menu(self):
        menubar = tk.Menu(self.root)

        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="🆕 Nuevo cálculo", command=self.reset_app)
        archivo_menu.add_command(label="🧹 Limpiar resultados", command=self.clear_result)
        archivo_menu.add_command(label="💾 Exportar historial", command=self.export_history)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="❌ Salir", command=self.confirm_exit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        ayuda_menu = tk.Menu(menubar, tearoff=0)
        ayuda_menu.add_command(label="📘 Instrucciones", command=self.show_instructions)
        ayuda_menu.add_command(label="ℹ️ Acerca de", command=self.show_about)
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)

        self.root.config(menu=menubar)

    def setup_ui(self):
        tk.Label(self.root, text="Calculadora de Áreas", font=("Arial", 20, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=10)

        figuras = [
            "Círculo", "Cuadrado", "Rectángulo", "Triángulo",
            "Trapecio", "Elipse", "Polígono Regular"
        ]
        self.figure_var = tk.StringVar()
        self.figure_dropdown = ttk.Combobox(self.root, textvariable=self.figure_var, values=figuras, state="readonly", width=30)
        self.figure_dropdown.set("Selecciona una figura")
        self.figure_dropdown.pack(pady=10)
        self.figure_dropdown.bind("<<ComboboxSelected>>", self.update_inputs)

        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="white", bd=2, relief=tk.RIDGE)
        self.canvas.pack(pady=10)

        self.inputs_frame = tk.LabelFrame(self.root, text="Parámetros de Entrada", bg="#dfe6e9", font=("Arial", 12, "bold"))
        self.inputs_frame.pack(pady=10, padx=20, fill=tk.X)

        self.calculate_btn = ttk.Button(self.root, text="✅ Calcular Área", command=self.calculate_area)
        self.calculate_btn.pack(pady=10)

        self.result_frame = tk.LabelFrame(self.root, text="Resultado", bg="#d1f2eb", font=("Arial", 12, "bold"))
        self.result_frame.pack(pady=10, padx=20, fill=tk.X)
        self.result_label = tk.Label(self.result_frame, text="", font=("Arial", 16, "bold"), fg="#2980b9", bg="#d1f2eb")
        self.result_label.pack(pady=10)

        self.history_frame = tk.LabelFrame(self.root, text="📜 Historial de esta sesión", bg="#fef9e7", font=("Arial", 12, "bold"))
        self.history_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.history_text = tk.Text(self.history_frame, height=10, font=("Courier", 10), bg="#fdfefe", state="disabled")
        self.history_text.pack(fill=tk.BOTH, padx=5, pady=5)

    def create_status_bar(self):
        status = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#d9d9d9")
        status.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_var.set("Listo")

    def clear_inputs(self):
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

    def clear_result(self):
        self.result_label.config(text="")
        self.status_var.set("Resultado limpiado")

    def reset_app(self):
        self.clear_inputs()
        self.canvas.delete("all")
        self.clear_result()
        self.figure_dropdown.set("Selecciona una figura")
        self.status_var.set("Aplicación reiniciada")

    def confirm_exit(self):
        if messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?"):
            self.root.destroy()

    def show_instructions(self):
        messagebox.showinfo("Instrucciones", "1. Selecciona una figura.\n2. Ingresa los datos.\n3. Pulsa 'Calcular Área'.")

    def show_about(self):
        messagebox.showinfo("Acerca de", "📐 Calculadora de Áreas\nAutor: Iosu Gómez Valdecantos\nVersión Profesional")

    def update_inputs(self, event):
        self.clear_inputs()
        self.clear_result()
        self.inputs = []
        figura = self.figure_var.get()
        campos = {
            "Círculo": ["Radio"],
            "Cuadrado": ["Lado"],
            "Rectángulo": ["Base", "Altura"],
            "Triángulo": ["Base", "Altura"],
            "Trapecio": ["Base Mayor", "Base Menor", "Altura"],
            "Elipse": ["Semieje Mayor", "Semieje Menor"],
            "Polígono Regular": ["Perímetro", "Apotema"]
        }

        for label_text in campos[figura]:
            frame = tk.Frame(self.inputs_frame, bg="#dfe6e9")
            frame.pack(pady=3)
            label = tk.Label(frame, text=label_text + ": ", font=("Segoe UI", 11), width=20, anchor="e", bg="#dfe6e9")
            spin = tk.Spinbox(frame, from_=0.0, to=10000.0, increment=0.1, width=10, format="%.2f", font=("Segoe UI", 11))
            label.pack(side=tk.LEFT, padx=5)
            spin.pack(side=tk.LEFT)
            self.inputs.append(spin)

        self.load_figure_image(figura)
        self.status_var.set(f"Figura: {figura}")

    def load_figure_image(self, figura):
        nombre_imagen = {
            "Círculo": "circulo.png",
            "Cuadrado": "cuadrado.png",
            "Rectángulo": "rectangulo.png",
            "Triángulo": "triangulo.png",
            "Trapecio": "trapecio.png",
            "Elipse": "elipse.png",
            "Polígono Regular": "poligono.png"
        }
        archivo = nombre_imagen.get(figura)
        self.canvas.delete("all")
        if archivo:
            try:
                ruta_base = os.path.dirname(__file__)
                ruta_imagen = os.path.join(ruta_base, "recursos", archivo)
                img = Image.open(ruta_imagen).resize((200, 200))
                self.tk_image = ImageTk.PhotoImage(img)
                self.canvas.create_image(100, 100, image=self.tk_image)
            except Exception as e:
                self.canvas.create_text(100, 100, text="Error cargando imagen", fill="red")
                print(f"[ERROR] Imagen: {archivo}\n{e}")
        else:
            self.canvas.create_text(100, 100, text="Sin imagen", fill="red")

    def get_inputs_as_floats(self):
        try:
            return [float(entry.get()) for entry in self.inputs]
        except ValueError:
            messagebox.showerror("Error", "Los campos deben contener números válidos.")
            return None

    def calculate_area(self):
        figura = self.figure_var.get()
        valores = self.get_inputs_as_floats()
        if valores is None:
            return

        area = 0
        try:
            if figura == "Círculo":
                area = pi * valores[0] ** 2
            elif figura == "Cuadrado":
                area = valores[0] ** 2
            elif figura == "Rectángulo":
                area = valores[0] * valores[1]
            elif figura == "Triángulo":
                area = (valores[0] * valores[1]) / 2
            elif figura == "Trapecio":
                area = ((valores[0] + valores[1]) * valores[2]) / 2
            elif figura == "Elipse":
                area = pi * valores[0] * valores[1]
            elif figura == "Polígono Regular":
                area = (valores[0] * valores[1]) / 2
            else:
                raise ValueError("Figura no reconocida.")
        except Exception as e:
            messagebox.showerror("Error", f"Error en el cálculo: {e}")
            return

        resultado = f"Área = {area:.2f}"
        self.result_label.config(text=resultado)
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        entrada = f"[{timestamp}] {figura}: {resultado}"
        self.historial.append(entrada)
        self.update_history(entrada)
        self.status_var.set("Cálculo realizado correctamente")

    def update_history(self, entrada):
        self.history_text.config(state=tk.NORMAL)
        self.history_text.insert(tk.END, entrada + "\n")
        self.history_text.config(state=tk.DISABLED)

    def export_history(self):
        if not self.historial:
            messagebox.showinfo("Exportar", "No hay historial para exportar.")
            return

        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
        if file:
            try:
                with open(file, "w", encoding="utf-8") as f:
                    f.write("Historial de Cálculos - Área Geométrica\n")
                    f.write("\n".join(self.historial))
                messagebox.showinfo("Exportado", f"Historial guardado en:\n{file}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo.\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculatorApp(root)
    root.mainloop()
