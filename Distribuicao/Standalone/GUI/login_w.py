# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_w.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 520)
        MainWindow.setMinimumSize(QSize(450, 520))
        MainWindow.setMaximumSize(QSize(450, 520))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bg_frame_2 = QVBoxLayout(self.centralwidget)
        self.bg_frame_2.setSpacing(0)
        self.bg_frame_2.setObjectName(u"bg_frame_2")
        self.bg_frame_2.setContentsMargins(10, 10, 10, 10)
        self.bg_frame = QFrame(self.centralwidget)
        self.bg_frame.setObjectName(u"bg_frame")
        self.bg_frame.setStyleSheet(u"background-color: rgb(29, 0, 86);\n"
"border-radius: 10px;")
        self.bg_frame.setFrameShape(QFrame.NoFrame)
        self.bg_frame.setFrameShadow(QFrame.Raised)
        self.tittle_bar = QFrame(self.bg_frame)
        self.tittle_bar.setObjectName(u"tittle_bar")
        self.tittle_bar.setGeometry(QRect(10, 10, 411, 31))
        self.tittle_bar.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.tittle_bar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 61, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Segoe UI\";")
        self.button_close = QPushButton(self.tittle_bar)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(380, 0, 21, 24))
        self.button_close.setStyleSheet(u"background-color: rgb(152, 0, 0);\n"
"font: 14pt \"Segoe UI\";")
        self.button_minimize = QPushButton(self.tittle_bar)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setGeometry(QRect(350, 0, 21, 24))
        self.button_minimize.setStyleSheet(u"background-color: rgb(53, 159, 159);\n"
"font: 14pt \"Segoe UI\";")
        self.user_login = QLineEdit(self.bg_frame)
        self.user_login.setObjectName(u"user_login")
        self.user_login.setGeometry(QRect(60, 160, 301, 51))
        self.user_login.setStyleSheet(u"background-color: rgb(53, 159, 159);\n"
"")
        self.pass_login = QLineEdit(self.bg_frame)
        self.pass_login.setObjectName(u"pass_login")
        self.pass_login.setGeometry(QRect(60, 281, 301, 51))
        self.pass_login.setStyleSheet(u"background-color: rgb(53, 159, 159);\n"
"")
        self.user_lbl = QLabel(self.bg_frame)
        self.user_lbl.setObjectName(u"user_lbl")
        self.user_lbl.setGeometry(QRect(170, 110, 81, 41))
        self.user_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Segoe UI\";")
        self.senha_lbl = QLabel(self.bg_frame)
        self.senha_lbl.setObjectName(u"senha_lbl")
        self.senha_lbl.setGeometry(QRect(179, 230, 71, 41))
        self.senha_lbl.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Segoe UI\";")
        self.btn_login = QPushButton(self.bg_frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(160, 360, 101, 41))
        self.btn_login.setStyleSheet(u"background-color: rgb(53, 159, 159);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Segoe UI\";\n"
"")

        self.bg_frame_2.addWidget(self.bg_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.button_close.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.button_minimize.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.user_lbl.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.senha_lbl.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Logar", None))
    # retranslateUi


