from ast import Lambda
import os
import sys
from tkinter import messagebox
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtSvgWidgets import * 
from PySide6.QtGui import *
import time
import threading 

##from gui.window.main_window.ui_login_window import Ui_LoginWindow
from GUI.window.main_window.ui_login_window import Ui_LoginWindow
from infra.carregarConfigs import carregarConfigs
from infra.connector_LogarUser import LogarUser
from modules.Context import Context
from modules.ui_DiagLogIn_Sucesso import DiagLoginSucesso
from modules.ui_DiagLogIn_Falha import DiagLoginFalha
from GUI.window.menu import MainWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # Remoção da Title Bar Padrão do Windows
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Acões dos Botões
        self.ui.pushButton_min.clicked.connect(self.minimizeWindow)
        self.ui.pushButton_close.clicked.connect(self.closeWindow)
        self.ui.frame_top.mouseMoveEvent = self.moveWindow
        self.ui.pushButton_login.clicked.connect(self.loginUser)

        self.show()

    def closeWindow(self):
        self.close()
        exit()

    def minimizeWindow(self):
        self.showMinimized()

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def loginUser(self):
        t_1 = 2
        user = self.ui.lineEdit_usuario.text()
        password = self.ui.lineEdit_senha.text()

        logIn = LogarUser.logarUser(user, password)

        if logIn:
            MessageBox = DiagLoginSucesso()
            Context.set_User(self, logIn[1])
            Context.set_TypeUser(self, logIn[3])
            print(Context.userRet)
            print(Context.typeUserRet)

            MainWindow()
            self.close()

        else:
            MessageBox = DiagLoginFalha()
            MessageBox.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())