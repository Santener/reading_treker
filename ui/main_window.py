from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

from .title_bar import TitleBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1280, 850)
        self.setStyleSheet("QMainWindow"
                           " {background-image: url(resources/main_window_background3.png);"
                           " background-repeat: no repeat;"
                           " background-position: center;}")

        self.setWindowFlags(Qt.WindowType.Window |
                            Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowMinMaxButtonsHint)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(TitleBar())
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        container.setLayout(layout)
        self.setCentralWidget(container)




