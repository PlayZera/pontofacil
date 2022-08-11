from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide6 import QtCore
from PySide6.QtCore import Qt

from GUI.login_w import Ui_MainWindow
from infra.connector_LogarUser import LogarUser
from modules.ui_DiagLogIn_Sucesso import DiagLoginSucesso
from modules.ui_DiagLogIn_Falha import DiagLoginFalha
from modules.ui_page import MainWindow

class ui_Login(QMainWindow):
    def __init__(self):
        super(ui_Login, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tittle_bar.mouseMoveEvent = self.moveWindow
        self.ui.button_close.clicked.connect(self.closeWindow)
        self.ui.button_minimize.clicked.connect(self.minimizeWindow)
        self.ui.btn_login.clicked.connect(self.loginUser)

        # <editor-fold desc="Window Default Config">
            #essas configs removem a barra do Windows
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # </editor-fold>

    # <editor-fold desc="Move Window and overwriting mousePressEvent">
    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    # </editor-fold>

    # <editor-fold desc="Buttons actions">

    def closeWindow(self):
        self.close()
        exit()

    def minimizeWindow(self):
        self.showMinimized()

    def loginUser(self):
        user = self.ui.user_login.text()
        password = self.ui.pass_login.text()

        logIn = LogarUser.logarUser(user, password)

        if logIn:
            MessageBox = DiagLoginSucesso()
            MessageBox.show()
            MainWindow()

        else:
            MessageBox = DiagLoginFalha()
            MessageBox.show()
    # </editor-fold>





