# IMPORT MODULES
from ast import Lambda
import os
import sys
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import * 
from PySide6.QtSvgWidgets import * 

# IMPORT MAIN WINDOW
from GUI.window.main_window.ui_main_window import Ui_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        # Configuração da Janela Principal
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button (Evento de Animação Gerado pelo Botão)
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # ========== Evento de Seleção de Páginas =========
        # Botão Home>

        self.ui.btn_1.clicked.connect(self.show_page_1)
        self.ui.btn_2.clicked.connect(self.show_page_2)
        self.ui.btn_3.clicked.connect(self.show_page_3)
        self.ui.btn_4.clicked.connect(self.show_page_4)
        self.ui.settings_button.clicked.connect(self.show_page_5)

        # ============ Evento do Title Bar ================
        self.ui.btn_close.clicked.connect(self.closeWindow)
        self.ui.btn_min.clicked.connect(self.minimizeWindow)
        self.ui.btn_max.clicked.connect(self.maximizeWindow)
        self.ui.top_bar.mouseMoveEvent = self.moveWindow
        self.ui.central_frame.mouseGrabber = self.resizewindow

        # Exibe a Aplicação
        self.show()

    def resizewindow(self):
        self.adjustSize()

    def closeWindow(self):
        self.close()
        exit()

    def minimizeWindow(self):
        self.showMinimized()

    def maximizeWindow(self):
        self.showMaximized()

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)

            except:
                pass

    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.btn_3.set_active(True)

    def show_page_4(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)
        self.ui.btn_4.set_active(True)

    def show_page_5(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_5)
        self.ui.settings_button.set_active(True)
    

    def toggle_button(self):
        # Get Menu Width
        menu_width = self.ui.left_menu.width()

        # Check Width
        width = 50 
        if menu_width == 50:
            width = 250
        
        # Inicio da Animação de Transição
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.setDuration(500)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
