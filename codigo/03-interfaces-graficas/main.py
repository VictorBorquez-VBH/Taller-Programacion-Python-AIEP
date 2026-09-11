import sys
from PySide6.QtWidgets import QApplication, QDialog
# Importamos la clase Ui_Dialog desde tu archivo generado
# (Asumo que tu archivo se llama "archivo_ui.py", cámbialo si tiene otro nombre)
from a03_qt_for_python_ui import Ui_Dialog  

class MiVentana(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Aquí se cargan tus botones y el diseño

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show() # Hace visible el diálogo en pantalla
    sys.exit(app.exec())
