from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QStyle


class TitleBar(QWidget):
    _STYLES = {
        "white": {"hover": "rgba(250, 250, 250, 0.2)", "pressed": "rgba(250, 250, 250, 0.3)"},
        "red": {"hover": "rgba(230, 34, 34, 1)", "pressed": "rgba(250, 87, 75, 1)"},
    }

    def __init__(self):
        super().__init__()

        self.setFixedHeight(40)

        exit_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton)
        self.max_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton)
        self.normal_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarNormalButton)
        min_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMinButton)

        btn_exit = self._create_button(exit_icon, self.close_window, "red")
        self.btn_window_size = self._create_button(self.max_icon, self.change_window, "white")
        btn_min = self._create_button(min_icon, self.min_window, "white")

        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(btn_min)
        layout.addWidget(self.btn_window_size)
        layout.addWidget(btn_exit)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

    @staticmethod
    def _create_button(icon, click_handler, style_key):
        button = QPushButton()
        button.setIcon(icon)
        button.setFixedSize(40, 40)
        button.clicked.connect(click_handler)
        profile = TitleBar._STYLES[style_key]
        hover = profile["hover"]
        pressed = profile["pressed"]
        button.setStyleSheet(f"QPushButton {{ border-radius: 0px; }}"
                             f"QPushButton:hover {{background-color: {hover}; }} "
                             f"QPushButton:pressed {{background-color: {pressed}; }}")

        return button

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
