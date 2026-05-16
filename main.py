from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
import sys

from ui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    MainWindow.center_window(window)
    window.show()
    sys.exit(app.exec())








