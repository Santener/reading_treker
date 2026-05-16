from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PySide6.QtCore import Qt, QEvent, QTimer

from .title_bar import TitleBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1280, 850)
        self.setStyleSheet("""QMainWindow {background-image: url(resources/main_window_background3.png);
                            background-repeat: no-repeat;
                            background-position: center;
                            border-style: solid;
                            border-radius: 0px;}
        """)

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

    @staticmethod
    def center_window(widget):
        screen = QApplication.primaryScreen().availableGeometry()
        size = widget.frameGeometry()
        size.moveCenter(screen.center())

        widget.move(size.topLeft())




# import sys
# import ctypes.wintypes
# from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
# from PySide6.QtCore import Qt
#
# from .title_bar import TitleBar
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setMinimumSize(1280, 850)
#
#         # РЕШЕНИЕ ЗАДАЧИ 6 (ФОН): background-size: cover растянет картинку под любой размер окна
#         self.setStyleSheet(
#             "QMainWindow {"
#             "   background-image: url('resources/main_window_background3.png');"
#             "   background-repeat: no-repeat;"
#             "   background-position: center;"
#             "   background-size: cover;"  # <--- ВОТ ОНО
#             "}"
#         )
#
#         # УБРАЛИ WindowMinMaxButtonsHint. Он был причиной 80% наших багов с рамками!
#         self.setWindowFlags(
#             Qt.WindowType.Window |
#             Qt.WindowType.FramelessWindowHint
#         )
#
#         container = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(TitleBar())
#         layout.addStretch()
#         layout.setContentsMargins(0, 0, 0, 0)
#         layout.setSpacing(0)
#
#         container.setLayout(layout)
#         self.setCentralWidget(container)
#
#     @staticmethod
#     def center_window(widget):
#         screen = QApplication.primaryScreen().availableGeometry()
#         size = widget.frameGeometry()
#         size.moveCenter(screen.center())
#         widget.move(size.topLeft())
#
#     # МАГИЯ ДЛЯ УБИРАНИЯ ДЫРОК (Windows 10/11 DWM)
#     def nativeEvent(self, eventType, message):
#         if eventType == b"windows_generic_MSG":
#             msg = ctypes.wintypes.MSG.from_address(int(message))
#             # 0x0083 = WM_NCCALCSIZE. Перехватываем расчет рамок Windows
#             if msg.message == 0x0083:
#                 return True, 0
#         return super().nativeEvent(eventType, message)
#
#     # МАГИЯ ДЛЯ УБИРАНИЯ СКРУГЛЕНИЙ В FULLSCREEN
#     def showEvent(self, event):
#         super().showEvent(event)
#         # Вызываем ТОЛЬКО после того, как окно реально отрисовалось (появился winId)
#         self._remove_rounded_corners()
#
#     def _remove_rounded_corners(self):
#         if sys.platform == "win32":
#             try:
#                 hwnd = int(self.winId())
#                 # 33 = DWMWA_WINDOW_CORNER_PREFERENCE
#                 # 1 = DWMWCP_DONOTROUND (Убрать скругления)
#                 preference = ctypes.c_int(1)
#                 ctypes.windll.dwmapi.DwmSetWindowAttribute(
#                     hwnd, 33, ctypes.byref(preference), ctypes.sizeof(preference)
#                 )
#             except Exception:
#                 pass  # Игнорируем, если запустили не на Windows