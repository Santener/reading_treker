from PySide6.QtWidgets import QApplication, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1280, 850)
        self.setStyleSheet("QMainWindow"
                           " {background-image: url(resources/main_window_background2.jpg);"
                           " background-repeat: no repeat;"
                           "background-position: center;}")