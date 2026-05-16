from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QStyle
from PySide6.QtCore import Qt


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
            fake_full_screen = screen_geo.adjusted(-1, -1, 1, 1)
            self.window().setGeometry(fake_full_screen)
            self.is_custom_maximized = True
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





# from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QStyle
# from PySide6.QtCore import Qt
#
#
# class TitleBar(QWidget):
#     """Custom header-model. Top window menu."""
#
#     BAR_HEIGHT = 40
#     BUTTON_SIZE = 40
#
#     _STYLES = {
#         "white": {"hover": "rgba(250, 250, 250, 0.2)", "pressed": "rgba(250, 250, 250, 0.3)"},
#         "red": {"hover": "rgba(230, 34, 34, 1)", "pressed": "rgba(250, 87, 75, 1)"},
#     }
#
#     def __init__(self) -> None:
#         super().__init__()
#         self.setFixedHeight(self.BAR_HEIGHT)
#
#         self.mouse_position = None
#         self.is_custom_maximized = False
#         self.normal_geometry = None
#
#         # Icons
#         exit_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton)
#         self.max_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton)
#         self.normal_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarNormalButton)
#         min_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_TitleBarMinButton)
#
#         # Buttons
#         btn_exit = self._create_button(exit_icon, self._close, "red")
#         self.btn_window_size = self._create_button(self.max_icon, self._toggle_maximize, "white")
#         btn_min = self._create_button(min_icon, self._minimize, "white")
#
#         # Layout
#         layout = QHBoxLayout()
#         layout.addStretch()
#         layout.addWidget(btn_min)
#         layout.addWidget(self.btn_window_size)
#         layout.addWidget(btn_exit)
#         layout.setContentsMargins(0, 0, 0, 0)
#         layout.setSpacing(0)
#         self.setLayout(layout)
#
#     @staticmethod
#     def _create_button(icon, click_handler, style_key) -> QPushButton:
#         button = QPushButton()
#         button.setIcon(icon)
#         button.setFixedSize(TitleBar.BUTTON_SIZE, TitleBar.BUTTON_SIZE)
#         button.setCursor(Qt.CursorShape.PointingHandCursor)
#         button.clicked.connect(click_handler)
#
#         profile = TitleBar._STYLES[style_key]
#         button.setStyleSheet(
#             f"QPushButton {{ border: none; background: transparent; }}"
#             f"QPushButton:hover {{background-color: {profile['hover']}; }}"
#             f"QPushButton:pressed {{background-color: {profile['pressed']}; }}"
#         )
#         return button
#
#     def _close(self) -> None:
#         self.window().close()
#
#     def _toggle_maximize(self) -> None:
#         if self.window().isMinimized():
#             return
#
#         if self.is_custom_maximized:
#             if self.normal_geometry:
#                 self.window().setGeometry(self.normal_geometry)
#             self.is_custom_maximized = False
#             self.btn_window_size.setIcon(self.max_icon)
#         else:
#             self.normal_geometry = self.window().geometry()
#             # ИСПОЛЬЗУЕМ НАТИВНЫЙ МЕТОД. nativeEvent в main_window уже убрал дырки!
#             self.window().showMaximized()
#             self.is_custom_maximized = True
#             self.btn_window_size.setIcon(self.normal_icon)
#
#     def _minimize(self) -> None:
#         self.window().showMinimized()
#
#     # --- DRAG & DROP (Абсолютные координаты) ---
#     def mousePressEvent(self, event, /):
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.mouse_position = event.globalPosition().toPoint() - self.window().frameGeometry().topLeft()
#
#     def mouseMoveEvent(self, event, /):
#         if self.mouse_position is not None and not self.is_custom_maximized:
#             new_pos = event.globalPosition().toPoint() - self.mouse_position
#             self.window().move(new_pos)
#
#     def mouseReleaseEvent(self, event, /):
#         self.mouse_position = None
#
#     def mouseDoubleClickEvent(self, event, /):
#         if event.button() == Qt.MouseButton.LeftButton:
#             self._toggle_maximize()