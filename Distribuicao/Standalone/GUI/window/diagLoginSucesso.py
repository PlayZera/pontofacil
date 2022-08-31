from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import * 
from PySide6.QtSvgWidgets import * 

class Ui_Dialog(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(399, 167)
        Frame.setMinimumSize(QSize(399, 167))
        Frame.setMaximumSize(QSize(399, 167))
        self.frame_content = QFrame(Frame)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setGeometry(QRect(-20, 20, 409, 131))
        self.frame_content.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.pushButton_close_2 = QPushButton(self.frame_content)
        self.pushButton_close_2.setObjectName(u"pushButton_close_2")
        self.pushButton_close_2.setGeometry(QRect(130, 80, 161, 21))
        font = QFont()
        font.setFamilies([u"Uni Sans"])
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_close_2.setFont(font)
        self.pushButton_close_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(125, 39, 28);")
        self.label_anuncio = QLabel(self.frame_content)
        self.label_anuncio.setObjectName(u"label_anuncio")
        self.label_anuncio.setGeometry(QRect(35, 13, 371, 51))
        font1 = QFont()
        font1.setFamilies([u"Uni Sans"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_anuncio.setFont(font1)
        self.label_anuncio.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_anuncio.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(Frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 401, 21))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_button_3 = QFrame(self.verticalLayoutWidget)
        self.frame_button_3.setObjectName(u"frame_button_3")
        self.frame_button_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_button_3.setFrameShape(QFrame.StyledPanel)
        self.frame_button_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_button_3)

        self.verticalLayoutWidget_2 = QWidget(Frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(385, 20, 16, 131))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_button = QFrame(self.verticalLayoutWidget_2)
        self.frame_button.setObjectName(u"frame_button")
        self.frame_button.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_button.setFrameShape(QFrame.StyledPanel)
        self.frame_button.setFrameShadow(QFrame.Raised)
        self.frame_button_4 = QFrame(self.frame_button)
        self.frame_button_4.setObjectName(u"frame_button_4")
        self.frame_button_4.setGeometry(QRect(10, 0, 14, 129))
        self.frame_button_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_button_4.setFrameShape(QFrame.StyledPanel)
        self.frame_button_4.setFrameShadow(QFrame.Raised)
        self.frame_button_5 = QFrame(self.frame_button)
        self.frame_button_5.setObjectName(u"frame_button_5")
        self.frame_button_5.setGeometry(QRect(-375, -20, 399, 19))
        self.frame_button_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_button_5.setFrameShape(QFrame.StyledPanel)
        self.frame_button_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_button)

        self.verticalLayoutWidget_3 = QWidget(Frame)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 20, 16, 131))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_button_6 = QFrame(self.verticalLayoutWidget_3)
        self.frame_button_6.setObjectName(u"frame_button_6")
        self.frame_button_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_button_6.setFrameShape(QFrame.StyledPanel)
        self.frame_button_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_button_6)

        self.verticalLayoutWidget_4 = QWidget(Frame)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 150, 401, 21))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_button_2 = QFrame(self.verticalLayoutWidget_4)
        self.frame_button_2.setObjectName(u"frame_button_2")
        self.frame_button_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_button_2.setFrameShape(QFrame.StyledPanel)
        self.frame_button_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_button_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.pushButton_close_2.setText(QCoreApplication.translate("Frame", u"Fechar", None))
        self.label_anuncio.setText(QCoreApplication.translate("Frame", u"LOGIN EFETUADO COM SUCESSO!", None))
    # retranslateUi

