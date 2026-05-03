from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QStyle
from PySide6.QtCore import QPointF


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

        self.setFixedHeight(self.BAR_HEIGHT)

        self.mouse_position = None

        # Made to prevent bag 01 for occurring
        self._is_custom_maximized = False
        self._normal_geometry = None

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

        if self._is_custom_maximized:
            self.window().showNormal()

            if self._normal_geometry:
                self.window().setGeometry(self._normal_geometry)

            self._is_custom_maximized = False
            self.btn_window_size.setIcon(self.max_icon)

        else:
            self._normal_geometry = self.window().geometry()
            self.window().showMaximized()
            self._is_custom_maximized = True
            self.btn_window_size.setIcon(self.normal_icon)

    def _minimize(self) -> None:
        """minimize window"""
        self.window().showMinimized()

    def mousePressEvent(self, event, /):
        self.mouse_position = QPointF(event.position())
        print(f"тыкнули здесь {event.position()}")
        print(f"окно здесь {self.window().pos()}")

    def mouseMoveEvent(self, event, /):
        if not self._is_custom_maximized:
            _x = QPointF(self.window().pos()).x() + (QPointF(event.position()).x() - self.mouse_position.x())
            _y = QPointF(self.window().pos()).y() + (QPointF(event.position()).y() - self.mouse_position.y())
            self.window().move(_x, _y)

    def mouseDoubleClickEvent(self, event, /):
        self._toggle_maximize()
