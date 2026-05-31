from PySide6.QtWidgets import QLabel, QWidget, QPushButton, QHBoxLayout, QStyle
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class TitleBar(QWidget):
    """Custom header-model. Top window menu."""

    BAR_HEIGHT = 40
    BUTTON_SIZE = 40

    _STYLES = {
        "white": {"hover": "rgba(250, 250, 250, 0.2)", "pressed": "rgba(250, 250, 250, 0.3)"},
        "red": {"hover": "rgba(230, 34, 34, 1)", "pressed": "rgba(250, 87, 75, 1)"},
    }

    def __init__(self) -> None:
        super().__init__()

        label_chip = QLabel()
        chip = QPixmap("resources/chip7.0.png")
        label_chip.setPixmap(chip)

        label_emblem = QLabel()
        emblem = QPixmap("resources/main_emblem3.0.png")
        scaled_emblem = emblem.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        label_emblem.setPixmap(scaled_emblem)


        # Titlebar size
        self.setFixedHeight(self.BAR_HEIGHT)

        self.setStyleSheet("QWidget { border-radius: 0px; }")

        self._delta = None
        self._old_pos = None

        # Made to prevent bag 01 for occurring
        self.is_custom_maximized = False
        self.normal_geometry = None

        # icons
        exit_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton)
        self.max_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton)
        self.normal_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarNormalButton)
        min_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMinButton)

        # buttons
        btn_exit = self._create_button(exit_icon, self._close, "red")
        self.btn_window_size = self._create_button(self.max_icon, self._toggle_maximize, "white")
        btn_min = self._create_button(min_icon, self._minimize, "white")

        # layout
        layout = QHBoxLayout()
        layout.addWidget(label_chip)
        layout.addStretch()
        layout.addWidget(btn_min)
        layout.addWidget(self.btn_window_size)
        layout.addWidget(btn_exit)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)


    @staticmethod
    def _create_button(icon, click_handler, style_key) -> QPushButton:
        """Create custom button for Titlebar."""
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

    def _close(self) -> None:
        """close app"""
        self.window().close()

    def _toggle_maximize(self) -> None:
        """toggle size of the window between normal and max"""
        if self.window().isMinimized():
            return

        if self.is_custom_maximized:

            if self.normal_geometry:
                self.window().setGeometry(self.normal_geometry)

            self.is_custom_maximized = False
            self.btn_window_size.setIcon(self.max_icon)

        else:
            self.normal_geometry = self.window().geometry()
            screen_geo = self.window().screen().availableGeometry()
            self.window().setGeometry(screen_geo)
            self.is_custom_maximized = True
            TitleBar.IS_CUSTOM_MAXIMIZED = True
            self.btn_window_size.setIcon(self.normal_icon)

    def _minimize(self) -> None:
        """minimize window"""
        self.window().showMinimized()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self._old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """Drag and Drop"""
        if not self.is_custom_maximized and self._old_pos is not None:
            self._delta = event.globalPosition().toPoint() - self._old_pos
            self.window().move(self.window().pos() + self._delta)
            self._old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self._old_pos = None
        self._delta = None

    def mouseDoubleClickEvent(self, event):
        self._toggle_maximize()


