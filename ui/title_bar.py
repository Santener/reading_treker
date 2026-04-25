from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class TitleBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(50)

        btn_exit = QPushButton()
        btn_exit.clicked.connect(self.close_window)
        btn_exit.setFixedSize(40, 40)

        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(btn_exit)
        self.setLayout(layout)

    def close_window(self):
        self.window().close()
