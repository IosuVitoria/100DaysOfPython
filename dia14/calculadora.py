import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QTextEdit, QMessageBox, QDialog, QTableWidget, QTableWidgetItem,
    QHeaderView, QFileDialog, QMainWindow, QMenuBar, QMenu, QGridLayout, QInputDialog
)
from PyQt6.QtGui import QAction, QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt
from scipy import stats
from datetime import datetime


class ModalDatos(QDialog):
    def __init__(self, datos_actuales=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Introducir Datos")
        self.setGeometry(150, 150, 400, 300)
        layout = QVBoxLayout()

        cantidad, ok = QInputDialog.getInt(self, "Cantidad de datos", "¿Cuántos datos vas a introducir?", 10, 1, 1000)
        if not ok:
            self.reject()
            return

        self.tabla = QTableWidget(cantidad, 1)
        self.tabla.setHorizontalHeaderLabels(["Dato"])
        self.tabla.horizontalHeader().setStretchLastSection(True)

        if datos_actuales:
            for i, dato in enumerate(datos_actuales):
                if i < cantidad:
                    self.tabla.setItem(i, 0, QTableWidgetItem(str(dato)))

        layout.addWidget(self.tabla)
        btn_ok = QPushButton("Aceptar")
        btn_ok.clicked.connect(self.accept)
        layout.addWidget(btn_ok)
        self.setLayout(layout)

    def obtener_datos(self):
        datos = []
        for row in range(self.tabla.rowCount()):
            item = self.tabla.item(row, 0)
            if item and item.text().strip():
                try:
                    datos.append(float(item.text().strip()))
                except ValueError:
                    QMessageBox.warning(self, "Dato inválido", f"El valor en la fila {row + 1} no es un número válido.")
                    return []
        return datos


class CalculadoraEstadistica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Estadística")
        self.setGeometry(100, 100, 900, 850)
        self.setStyleSheet("background-color: #e0e9f1; color: #000000;")
        self.datos = []
        self.init_ui()

    def init_ui(self):
        menu_bar = self.menuBar()
        menu_ayuda = menu_bar.addMenu("Ayuda")
        accion_ayuda = QAction("Cómo usar", self)
        accion_ayuda.triggered.connect(self.mostrar_ayuda)
        menu_ayuda.addAction(accion_ayuda)

        contenedor = QWidget()
        layout = QVBoxLayout()

        icono = QLabel()
        icono.setPixmap(QPixmap("statistics_icon.png").scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio))
        icono.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(icono)

        titulo = QLabel("Calculadora Estadística")
        titulo.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)

        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)
        self.resultado.setStyleSheet("background-color: #ffffff; padding: 10px; border-radius: 8px; color: black;")
        layout.addWidget(self.resultado)

        botones = QGridLayout()

        btn_nuevos = QPushButton(QIcon("icon_add.png"), "Agregar Datos")
        btn_nuevos.clicked.connect(self.agregar_datos)

        btn_calc = QPushButton(QIcon("icon_calc.png"), "Calcular")
        btn_calc.clicked.connect(self.calcular_estadisticas)

        btn_informe = QPushButton(QIcon("icon_report.png"), "Informe")
        btn_informe.clicked.connect(self.generar_informe)

        btn_grafico = QPushButton(QIcon("icon_chart.png"), "Graficar")
        btn_grafico.clicked.connect(self.graficar_datos)

        for i, btn in enumerate([btn_nuevos, btn_calc, btn_informe, btn_grafico]):
            btn.setStyleSheet("background-color: #c0d8f0; color: black; padding: 10px; border-radius: 10px;")
            btn.setFont(QFont("Arial", 12))
            botones.addWidget(btn, 0, i)

        layout.addLayout(botones)
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def mostrar_ayuda(self):
        texto = (
            "1. Haz clic en 'Agregar Datos' para introducir valores.\n"
            "2. Haz clic en 'Calcular' para obtener estadísticas descriptivas.\n"
            "3. 'Informe' guarda los resultados en un archivo de texto.\n"
            "4. 'Graficar' muestra el histograma y curva de distribución normal.\n"
            "\nEstadísticas Calculadas:\n"
            "- 🔢 Media, Mediana, Moda\n"
            "- 🌐 Desviación estándar, Varianza\n"
            "- ⚖️ Rango, Mínimo, Máximo\n"
            "- 🌌 Asimetría, Curtosis\n"
            "- 🌍 Distribución normal ajustada\n"
        )
        QMessageBox.information(self, "Ayuda", texto)

    def agregar_datos(self):
        dialogo = ModalDatos(self.datos, self)
        if dialogo.exec():
            nuevos = dialogo.obtener_datos()
            if nuevos:
                self.datos.extend(nuevos)
                QMessageBox.information(self, "Datos añadidos", f"Total datos: {len(self.datos)}")

    def calcular_estadisticas(self):
        if not self.datos:
            QMessageBox.warning(self, "Error", "Introduce datos primero.")
            return

        x = np.array(self.datos)
        moda_resultado = stats.mode(x, keepdims=True)
        moda_valor = moda_resultado.mode[0] if moda_resultado.count[0] > 0 else np.nan

        resultado = (
            f"📈 <b>Cantidad de datos:</b> {len(x)}\n"
            f"✏️ <b>Media:</b> {np.mean(x):.4f}\n"
            f"🔢 <b>Mediana:</b> {np.median(x):.4f}\n"
            f"🔍 <b>Moda:</b> {moda_valor:.4f}\n"
            f"🔌 <b>Desviación estándar:</b> {np.std(x, ddof=1):.4f}\n"
            f"🔹 <b>Varianza:</b> {np.var(x, ddof=1):.4f}\n"
            f"⚖️ <b>Rango:</b> {np.ptp(x):.4f}\n"
            f"🔽 <b>Mínimo:</b> {np.min(x):.4f}\n"
            f"🔼 <b>Máximo:</b> {np.max(x):.4f}\n"
            f"🌌 <b>Asimetría:</b> {stats.skew(x):.4f}\n"
            f"🌐 <b>Curtosis:</b> {stats.kurtosis(x):.4f}\n"
        )

        dist = stats.norm.fit(x)
        resultado += f"\n☀️ <b>Distribución normal ajustada:</b> media={dist[0]:.4f}, std={dist[1]:.4f}"
        self.resultado.setHtml(f"<pre>{resultado}</pre>")

    def generar_informe(self):
        if not self.resultado.toPlainText():
            QMessageBox.warning(self, "Vacío", "No hay resultados.")
            return
        nombre, _ = QFileDialog.getSaveFileName(self, "Guardar informe", "informe.txt", "Text Files (*.txt)")
        if nombre:
            with open(nombre, "w", encoding="utf-8") as f:
                f.write(self.resultado.toPlainText())
            QMessageBox.information(self, "Guardado", f"Informe guardado en {nombre}")

    def graficar_datos(self):
        if not self.datos:
            QMessageBox.warning(self, "Error", "Introduce datos primero.")
            return
        plt.figure(figsize=(8, 5))
        plt.hist(self.datos, bins=10, color='#a2c4f5', edgecolor='black', density=True)
        mu, std = stats.norm.fit(self.datos)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = stats.norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        plt.title("Histograma con ajuste normal")
        plt.xlabel("Valores")
        plt.ylabel("Densidad")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraEstadistica()
    ventana.show()
    sys.exit(app.exec())