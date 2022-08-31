import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from modules.ui_login import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())