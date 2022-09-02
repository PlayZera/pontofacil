# Imports
from cgitb import text
from cmath import rect
from msvcrt import kbhit
import os
from re import S
from tarfile import is_tarfile
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import * 
from PySide6.QtSvgWidgets import * 

class PyCloseButton(QPushButton):
    def __init__(
        self,
        text = "",
        height = 30,
        minimum_width = 30,
        text_padding = 2,
        text_color = "White",
        icon_path = "",
        icon_color = "White",
        btn_color = "",
        btn_hover = "#6F1313",
        btn_pressed = "",
        is_active = False
    ):

        super().__init__()

        # Set Default Parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom  Parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding 
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set Style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu
        )

    def set_style(
        self,
        text_padding = 2,
        text_color = "White",
        btn_color = "#272A31",
        btn_hover = "#2c313c",
        btn_pressed = "#4B5364",
        is_active = False
    ):

        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
            }}
        QPushButton:hover {{
            background-color: {btn_hover};


            }}
        QPushButton:pressed {{
            background-color: {btn_pressed};


            }}
        """
        
        active_style = f"""
        QPushButton {{
            background-color: {btn_hover};
            border-right: 5px solid #0E0E10;

        }}
        """

        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):

        # Retornar o Stylo Padrão e não sobrepor
        QPushButton.paintEvent(self, event)

        # Painter
        
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0,0, self.minimum_width, self.height())
        
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end

    def draw_icon(self, qp, image, rect, color):
        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "Distribuicao/Standalone/GUI/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        
        # Draw Icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()


class PyTitleButton(QPushButton):
    def __init__(
        self,
        text = "",
        height = 30,
        minimum_width = 30,
        text_padding = 2,
        text_color = "White",
        icon_path = "",
        icon_color = "White",
        btn_color = "",
        btn_hover = "#2c313c",
        btn_pressed = "",
        is_active = False
    ):

        super().__init__()

        # Set Default Parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom  Parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding 
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set Style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu
        )

    def set_style(
        self,
        text_padding = 2,
        text_color = "White",
        btn_color = "#272A31",
        btn_hover = "#2c313c",
        btn_pressed = "#4B5364",
        is_active = False
    ):

        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
            }}
        QPushButton:hover {{
            background-color: {btn_hover};


            }}
        QPushButton:pressed {{
            background-color: {btn_pressed};


            }}
        """
        
        active_style = f"""
        QPushButton {{
            background-color: {btn_hover};
            border-right: 5px solid #0E0E10;

        }}
        """

        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):

        # Retornar o Stylo Padrão e não sobrepor
        QPushButton.paintEvent(self, event)

        # Painter
        
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0,0, self.minimum_width, self.height())
        
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end

    def draw_icon(self, qp, image, rect, color):
        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "Distribuicao/Standalone/GUI/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        
        # Draw Icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()



class PyPushButton(QPushButton):
    def __init__(
        self,
        text = "",
        height = 40,
        minimum_width = 50,
        text_padding = 55,
        text_color = "White",
        icon_path = "",
        icon_color = "White",
        btn_color = "#272A31",
        btn_hover = "#2c313c",
        btn_pressed = "#4B5364",
        is_active = False
    ):

        super().__init__()

        # Set Default Parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom  Parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding 
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set Style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu
        )

    def set_style(
        self,
        text_padding = 55,
        text_color = "White",
        btn_color = "#272A31",
        btn_hover = "#2c313c",
        btn_pressed = "#4B5364",
        is_active = False
    ):

        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
            }}
        QPushButton:hover {{
            background-color: {btn_hover};


            }}
        QPushButton:pressed {{
            background-color: {btn_pressed};


            }}
        """
        
        active_style = f"""
        QPushButton {{
            background-color: {btn_hover};
            border-right: 5px solid #0E0E10;

        }}
        """

        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):

        # Retornar o Stylo Padrão e não sobrepor
        QPushButton.paintEvent(self, event)

        # Painter
        
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0,0, self.minimum_width, self.height())
        
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end

    def draw_icon(self, qp, image, rect, color):
        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "Distribuicao/Standalone/GUI/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        
        # Draw Icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()



class PyLoginButtons(QPushButton):
    def __init__(
        self,
        text = "",
        height = 24,
        minimum_width = 24,
        text_padding = 24,
        text_color = "White",
        icon_path = "",
        icon_color = "White",
        btn_color = "#272A31",
        btn_hover = "#2c313c",
        btn_pressed = "#4B5364",
        is_active = False
    ):

        super().__init__()

        # Set Default Parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom  Parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding 
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set Style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu
        )

    def set_style(
        self,
        text_padding = 55,
        text_color = "#be4d25",
        btn_color = "#272A31",
        btn_hover = "#2c313c",
        btn_pressed = "#4B5364",
        is_active = False
    ):

        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
            }}
        QPushButton:hover {{
            background-color: {btn_hover};


            }}
        QPushButton:pressed {{
            background-color: {btn_pressed};


            }}
        """
        
        active_style = f"""
        QPushButton {{
            background-color: {btn_hover};
            border-right: 5px solid #0E0E10;

        }}
        """

        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):

        # Retornar o Stylo Padrão e não sobrepor
        QPushButton.paintEvent(self, event)

        # Painter
        
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0,0, self.minimum_width, self.height())
        
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end

    def draw_icon(self, qp, image, rect, color):
        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "Distribuicao/Standalone/GUI/images/login_icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        
        # Draw Icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()

