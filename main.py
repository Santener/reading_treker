import sys
import ctypes
from PySide6.QtWidgets import QApplication

from PySide6.QtGui import QIcon
import sys
from ui.main_window import MainWindow

appid = "company.product.version1.3"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("resources/main_emblem3.0.png"))
    window = MainWindow()
    MainWindow.center_window(window)
    window.show()
    sys.exit(app.exec())








