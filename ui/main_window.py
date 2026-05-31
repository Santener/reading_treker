from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PySide6.QtCore import Qt

import ctypes.wintypes
from .title_bar import TitleBar
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1280, 850)
        self.setStyleSheet("""QMainWindow {
                            background-image :url(resources/main_window_background3.2.png);
                            background-repeat: no-repeat;
                            background-position: center;
                            border-style: solid;
                            border-radius: 0px;}
        """)

        self.setWindowFlags(Qt.WindowType.Window |
                            Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowMinMaxButtonsHint)

        self.setWindowTitle("Reading trekker")

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(TitleBar())
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        container.setLayout(layout)
        self.setCentralWidget(container)

    @staticmethod
    def center_window(widget):
        screen = QApplication.primaryScreen().availableGeometry()
        size = widget.frameGeometry()
        size.moveCenter(screen.center())

        widget.move(size.topLeft())

    def nativeEvent(self, eventType, message):
        if eventType == b"windows_generic_MSG":
            msg = ctypes.wintypes.MSG.from_address(int(message))
            if msg.message == 0x0083:
                return True, 0
        return super().nativeEvent(eventType, message)

    def showEvent(self, event):
        super().showEvent(event)
        self._remove_rounded_corners()

    def _remove_rounded_corners(self):
        if sys.platform == "win32":
            try:
                hwnd = int(self.winId())

                preference = ctypes.c_int(1)
                ctypes.windll.dwmapi.DwmSetWindowAttribute(
                    hwnd, 33, ctypes.byref(preference), ctypes.sizeof(preference)
                )
            except Exception:
                pass


