import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.setWindowTitle("Mi Aplicación PySide6")
        self.resize(1000, 500)

        # Contenedor central obligatorio en QMainWindow
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        # Layout principal vertical
        layout_principal = QVBoxLayout()
        widget_central.setLayout(layout_principal)

        # --- Componentes UI ---

        # Título / Encabezado
        self.label_titulo = QLabel("¡Bienvenido a PySide6!")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_titulo.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        layout_principal.addWidget(self.label_titulo)

        # Layout horizontal para entrada de texto
        layout_entrada = QHBoxLayout()
        
        label_nombre = QLabel("Nombre:")
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Escribe tu nombre aquí...")
        
        layout_entrada.addWidget(label_nombre)
        layout_entrada.addWidget(self.input_nombre)
        
        layout_principal.addLayout(layout_entrada)

        # Botón de acción
        self.btn_saludar = QPushButton("Saludar")
        self.btn_saludar.setCursor(Qt.CursorShape.PointingHandCursor)
        layout_principal.addWidget(self.btn_saludar)

        # --- Conexión de Señales y Slots ---
        self.btn_saludar.clicked.connect(self.mostrar_saludo)
        self.input_nombre.returnPressed.connect(self.mostrar_saludo)  # Al presionar Enter

    def mostrar_saludo(self):
        nombre = self.input_nombre.text().strip()

        if nombre:
            QMessageBox.information(
                self,
                "Saludo",
                f"¡Hola, {nombre}! Bienvenido a la aplicación."
            )
        else:
            QMessageBox.warning(
                self,
                "Atención",
                "Por favor, ingresa tu nombre antes de saludar."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())