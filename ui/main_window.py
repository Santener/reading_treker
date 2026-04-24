from PySide6.QtWidgets import  QMainWindow
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1280, 850)
        self.setStyleSheet("QMainWindow"
                           " {background-image: url(resources/main_window_background3.png);"
                           " background-repeat: no repeat;"
                           " background-position: center;}")

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)




