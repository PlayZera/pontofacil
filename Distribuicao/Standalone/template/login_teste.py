# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerAmCCLy.ui'
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 420)
        self.verticalLayoutWidget = QWidget(Frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 30, 401, 391))
        self.content = QVBoxLayout(self.verticalLayoutWidget)
        self.content.setObjectName(u"content")
        self.content.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(210, 199, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_login = QPushButton(self.frame)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(30, 350, 75, 24))
        self.pushButton_faq = QPushButton(self.frame)
        self.pushButton_faq.setObjectName(u"pushButton_faq")
        self.pushButton_faq.setGeometry(QRect(280, 350, 91, 24))
        self.lineEdit_usuario = QLineEdit(self.frame)
        self.lineEdit_usuario.setObjectName(u"lineEdit_usuario")
        self.lineEdit_usuario.setGeometry(QRect(90, 150, 221, 21))
        self.lineEdit_senha = QLineEdit(self.frame)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setGeometry(QRect(90, 230, 221, 21))
        self.label_Login = QLabel(self.frame)
        self.label_Login.setObjectName(u"label_Login")
        self.label_Login.setGeometry(QRect(180, 30, 49, 16))
        self.label_usuario = QLabel(self.frame)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setGeometry(QRect(30, 150, 49, 16))
        self.label_senha = QLabel(self.frame)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setGeometry(QRect(30, 230, 49, 16))

        self.content.addWidget(self.frame)

        self.verticalLayoutWidget_2 = QWidget(Frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 401, 31))
        self.top_bar = QVBoxLayout(self.verticalLayoutWidget_2)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.verticalLayoutWidget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"background-color: rgb(134, 249, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_empresa = QLabel(self.frame_2)
        self.label_empresa.setObjectName(u"label_empresa")
        self.label_empresa.setGeometry(QRect(0, 0, 121, 16))
        self.pushButton_exitr = QPushButton(self.frame_2)
        self.pushButton_exitr.setObjectName(u"pushButton_exitr")
        self.pushButton_exitr.setGeometry(QRect(370, 0, 21, 24))
        self.pushButton_maximize = QPushButton(self.frame_2)
        self.pushButton_maximize.setObjectName(u"pushButton_maximize")
        self.pushButton_maximize.setGeometry(QRect(340, 0, 21, 24))
        self.pushButton_minimize = QPushButton(self.frame_2)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        self.pushButton_minimize.setGeometry(QRect(310, 0, 20, 24))

        self.top_bar.addWidget(self.frame_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.pushButton_login.setText(QCoreApplication.translate("Frame", u"Login", None))
        self.pushButton_faq.setText(QCoreApplication.translate("Frame", u"Quem Somos?", None))
        self.lineEdit_usuario.setText("")
        self.label_Login.setText(QCoreApplication.translate("Frame", u"Login", None))
        self.label_usuario.setText(QCoreApplication.translate("Frame", u"Usu\u00e1rio", None))
        self.label_senha.setText(QCoreApplication.translate("Frame", u"Senha", None))
        self.label_empresa.setText(QCoreApplication.translate("Frame", u"Ponto Fac\u00edl", None))
        self.pushButton_exitr.setText(QCoreApplication.translate("Frame", u"exit", None))
        self.pushButton_maximize.setText(QCoreApplication.translate("Frame", u"maximize", None))
        self.pushButton_minimize.setText(QCoreApplication.translate("Frame", u"Minimize", None))
    # retranslateUi

