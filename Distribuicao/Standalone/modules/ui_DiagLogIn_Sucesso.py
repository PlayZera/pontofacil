from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide6 import QtCore
from PySide6.QtCore import Qt

from GUI.window.diagLoginSucesso import Ui_Dialog


class DiagLoginSucesso(QDialog):
    def __init__(self):
        super(DiagLoginSucesso, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.frame_content.mouseMoveEvent = self.moveWindow
        self.ui.pushButton_close_2.clicked.connect(self.fecharDiag)

        # <editor-fold desc="Window Default Config">
        # essas configs removem a barra do Windows
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # </editor-fold>

    # <editor-fold desc="Move Window and overring mousePressEvent">
    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    # </editor-fold>

    # <editor-fold desc="Buttons actions">

    def fecharDiag(self):
        self.close()
    # </editor-fold>
