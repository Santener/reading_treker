from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QStyle


class TitleBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(40)

        exit_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton)

        btn_exit = QPushButton()
        btn_exit.setIcon(exit_icon)
        btn_exit.clicked.connect(self.close_window)
        btn_exit.setFixedSize(40, 40)
        btn_exit.setStyleSheet("QPushButton { border-radius: 0px }"
                               "QPushButton:hover {background-color: #e62222}"
                               "QPushButton:pressed {background-color: #fa574b}"
                               )

        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(btn_exit)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

    def close_window(self):
        self.window().close()
