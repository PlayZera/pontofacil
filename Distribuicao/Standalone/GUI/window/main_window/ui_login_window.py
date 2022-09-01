# -*- coding: utf-8 -*-QPix

################################################################################
## Form generated from reading UI file 'AtualizadoSPTRXI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(479, 494)
        Frame.setMinimumSize(QSize(479, 494))
        Frame.setSizeIncrement(QSize(400, 420))
        self.verticalLayoutWidget = QWidget(Frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-10, 0, 501, 41))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.verticalLayoutWidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.label_login = QLabel(self.frame_top)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(20, 10, 101, 21))
        font = QFont()
        font.setFamilies([u"Uni Sans"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet(u"color: rgb(255, 255, 255);")

        # Botão para Fechar a aplicação
        self.pushButton_close = QPushButton(self.frame_top)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(455, 3, 31, 31))
        self.pushButton_close.setMouseTracking(False)
        self.pushButton_close.setStyleSheet(u"")
        self.pushButton_close.setIcon(QIcon("Distribuicao/Standalone/GUI/images/login_icons/icon_close.svg"))


        # Botão de Minimizar
        self.pushButton_min = QPushButton(self.frame_top)
        self.pushButton_min.setObjectName(u"pushButton_min")
        self.pushButton_min.setGeometry(QRect(422, 3, 31, 31))
        self.pushButton_min.setStyleSheet(u"")
        self.pushButton_min.setIcon(QIcon("Distribuicao/Standalone/GUI/images/login_icons/icon_min.svg"))

        self.verticalLayout.addWidget(self.frame_top)

        self.verticalLayoutWidget_2 = QWidget(Frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(-20, 40, 511, 431))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.verticalLayoutWidget_2)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)

        # Botão de Login
        self.pushButton_login = QPushButton(self.frame_content)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(190, 360, 121, 41))
        font1 = QFont()
        font1.setFamilies([u"Uni Sans"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_login.setFont(font1)
        self.pushButton_login.setStyleSheet(u"color: rgb(255, 255, 255);")


        # Configuração da Fonte:
        font_a = QFont()
        font_a.setFamilies([u"Arial"])
        font_a.setPointSize(10)
        font_a.setBold(True)

         # LineEdit == Usuario
        self.lineEdit_usuario = QLineEdit(self.frame_content)
        self.lineEdit_usuario.setObjectName(u"lineEdit_usuario")
        self.lineEdit_usuario.setGeometry(QRect(130, 250, 241, 31))
        font3 = QFont()
        font3.setFamilies([u"Uni Sans"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.lineEdit_usuario.setFont(font_a)
        self.lineEdit_usuario.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_usuario.setStyleSheet(u"color: rgb(255, 255, 255);")


        # LineEdit == Senha
        self.lineEdit_senha = QLineEdit(self.frame_content)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setGeometry(QRect(130, 303, 241, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.lineEdit_senha.setFont(font_a)
        self.lineEdit_senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_senha.setEchoMode(QLineEdit.Password)

        #  ========== FOTO DA EMPRESA ========== #
        self.label_logo = QLabel(self.frame_content)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(150, 30, 201, 171))
        self.label_logo.setAlignment(Qt.AlignCenter)
        self.label_logo.setPixmap(QPixmap("Distribuicao/Standalone/GUI/images/login_icons/logo_solved.svg"))

        self.label_senha = QLabel(self.frame_content)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setGeometry(QRect(69, 307, 61, 21))
        self.label_senha.setFont(font1)
        self.label_senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_usuario = QLabel(self.frame_content)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setGeometry(QRect(52, 256, 71, 21))
        self.label_usuario.setFont(font1)
        self.label_usuario.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_content)

        self.verticalLayoutWidget_3 = QWidget(Frame)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(-10, 470, 501, 31))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.frame_button = QFrame(self.verticalLayoutWidget_3)
        self.frame_button.setObjectName(u"frame_button")
        self.frame_button.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_button.setFrameShape(QFrame.StyledPanel)
        self.frame_button.setFrameShadow(QFrame.Raised)
        self.label_buttonsoft = QLabel(self.frame_button)
        self.label_buttonsoft.setObjectName(u"label_buttonsoft")
        self.label_buttonsoft.setGeometry(QRect(20, 3, 131, 16))
        font4 = QFont()
        font4.setFamilies([u"Uni Sans"])
        font4.setBold(True)
        self.label_buttonsoft.setFont(font4)
        self.label_buttonsoft.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_buttondate = QLabel(self.frame_button)
        self.label_buttondate.setObjectName(u"label_buttondate")
        self.label_buttondate.setGeometry(QRect(440, 3, 41, 16))
        self.label_buttondate.setFont(font4)
        self.label_buttondate.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.frame_button)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label_login.setText(QCoreApplication.translate("Frame", u"Login", None))
        self.pushButton_close.setText("")
        self.pushButton_min.setText("")
        self.pushButton_login.setText(QCoreApplication.translate("Frame", u"LOGIN", None))
        self.lineEdit_usuario.setText("")
        self.lineEdit_senha.setText("")
        self.label_logo.setText("")
        self.label_senha.setText(QCoreApplication.translate("Frame", u"SENHA:", None))
        self.label_usuario.setText(QCoreApplication.translate("Frame", u"USU\u00c1RIO:", None))
        self.label_buttonsoft.setText(QCoreApplication.translate("Frame", u"SolvedBySoftware\u2122", None))
        self.label_buttondate.setText(QCoreApplication.translate("Frame", u"\u00a9 2022", None))
    # retranslateUi

