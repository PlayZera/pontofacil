import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from modules.ui_login import ui_Login

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ui_Login()
    window.show()

    sys.exit(app.exec())