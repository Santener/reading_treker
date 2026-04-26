from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QStyle


class TitleBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(40)

        exit_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton)
        self.max_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton)
        self.normal_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarNormalButton)
        min_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMinButton)

        btn_exit = QPushButton()
        btn_exit.setIcon(exit_icon)
        btn_exit.clicked.connect(self.close_window)
        btn_exit.setFixedSize(40, 40)
        btn_exit.setStyleSheet("QPushButton { border-radius: 0px }"
                               "QPushButton:hover {background-color: #e62222}"
                               "QPushButton:pressed {background-color: #fa574b}")

        self.btn_window_size = QPushButton()
        self.btn_window_size.setIcon(self.max_icon)
        self.btn_window_size.setFixedSize(40, 40)
        self.btn_window_size.clicked.connect(self.change_window)
        self.btn_window_size.setStyleSheet("QPushButton { border-radius: 0px }"
                                           "QPushButton:hover {background-color: rgba(250, 250, 250, 0.2)}"
                                           "QPushButton:pressed {background-color: rgba(250, 250, 250, 0.3)}")

        btn_min = QPushButton()
        btn_min.setIcon(min_icon)
        btn_min.setFixedSize(40, 40)
        btn_min.clicked.connect(self.min_window)
        btn_min.setStyleSheet("QPushButton { border-radius: 0px }"
                              "QPushButton:hover {background-color: rgba(250, 250, 250, 0.2)}"
                              "QPushButton:pressed {background-color: rgba(250, 250, 250, 0.3)}")
        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(btn_min)
        layout.addWidget(self.btn_window_size)
        layout.addWidget(btn_exit)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

    def close_window(self):
        self.window().close()

    def change_window(self):
        if self.window().isMaximized():
            self.window().showNormal()
            self.btn_window_size.setIcon(self.max_icon)
        else:
            self.window().showMaximized()
            self.btn_window_size.setIcon(self.normal_icon)

    def min_window(self):
        self.window().showMinimized()



