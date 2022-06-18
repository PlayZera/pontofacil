# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'falha_Login_Diag.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 120)
        Dialog.setMinimumSize(QSize(400, 120))
        Dialog.setMaximumSize(QSize(400, 120))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.bg_diag = QFrame(Dialog)
        self.bg_diag.setObjectName(u"bg_diag")
        self.bg_diag.setStyleSheet(u"background-color: rgb(29, 0, 86);\n"
"border-radius: 10px;")
        self.bg_diag.setFrameShape(QFrame.NoFrame)
        self.bg_diag.setFrameShadow(QFrame.Raised)
        self.tittle_bar = QFrame(self.bg_diag)
        self.tittle_bar.setObjectName(u"tittle_bar")
        self.tittle_bar.setGeometry(QRect(10, 10, 361, 31))
        self.tittle_bar.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QFrame.Raised)
        self.lbl_falhaLogar = QLabel(self.tittle_bar)
        self.lbl_falhaLogar.setObjectName(u"lbl_falhaLogar")
        self.lbl_falhaLogar.setGeometry(QRect(64, -9, 241, 41))
        self.lbl_falhaLogar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Segoe UI\";")
        self.pushButton = QPushButton(self.bg_diag)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(161, 60, 61, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(53, 159, 159);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Segoe UI\";\n"
"")

        self.verticalLayout.addWidget(self.bg_diag)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_falhaLogar.setText(QCoreApplication.translate("Dialog", u"Falha ao logar usu\u00e1rio", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi

