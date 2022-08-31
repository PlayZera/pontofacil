# /////////////////////////////////////////////////////////////
#
#   Por: Lucas Amaral
#   Project Made With: Python - Pyside6 - Qt Designer
#   Version: 1.0
#
# /////////////////////////////////////////////////////////////

# IMPORT QTCORE
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import * 
from PySide6.QtSvgWidgets import * 

# IMPORT PAGES
from Distribuicao.Standalone.GUI.page import Ui_application_pages

# IMPORT CUSTOM WIDGETS
from Distribuicao.Standalone.GUI.widgets.py_push_Button import PyPushButton
from Distribuicao.Standalone.GUI.widgets.py_push_Button import PyTitleButton



# MAIN WINDOW 
class Ui_MainWindow(object):
    def setup_ui (self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # PARAMETRO INICIAL DE TAMANHO
        parent.resize(1080, 700)
        parent.setMinimumSize(1280, 768)

        # Criação do Frame Principal
        self.central_frame = QFrame()
        

        # Criação do Layout Total
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        # Criação do Layout Left Menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #1D2025")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # Left Menu layout
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)
        
        # Frame Para icones <- Left Menu Layout
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setMinimumHeight(40)

        

        # Left Menu Top Layout
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)

        # Top Bins
        self.toggle_button = PyPushButton(
            text = "Ocultar Menu",
            icon_path = "icon_menu_1.svg"
        )
        self.btn_1 = PyPushButton(
            text = "Página Principal",
            is_active = True ,
            icon_path = "icon_home_2.svg"
        )
        self.btn_2 = PyPushButton(
            text = "Hora do Ponto",
            icon_path = "icon_timer_3.svg"

        )
        self.btn_3 = PyPushButton(
            text = "Chat Box",
            icon_path = "icon_chatbox_4.svg"

        )

        self.btn_4 = PyPushButton(
            text = "Perfil",
            icon_path = "icon_perfil_5.svg"

        )
        

        # Add Bins to Layout
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)
        self.left_menu_top_layout.addWidget(self.btn_3)
        self.left_menu_top_layout.addWidget(self.btn_4)

        # Espaçador Vertical <- Left Menu Layout
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Frame Para icones button <- Left Menu Layout
        self.left_menu_button_frame = QFrame()
        self.left_menu_button_frame.setObjectName("left_menu_button_frame")
        self.left_menu_button_frame.setMinimumHeight(40)


        self.left_menu_button_layout = QVBoxLayout(self.left_menu_button_frame)
        self.left_menu_button_layout.setContentsMargins(0,0,0,0)
        self.left_menu_button_layout.setSpacing(0)

        # Button Bins
        self.settings_button = PyPushButton(
            text = "Configurações",
            icon_path = "icon_config_6.svg"
        )

        # Add Button Bins to Layout
        self.left_menu_button_layout.addWidget(self.settings_button)

        # Label Versão da Aplicação
        self.left_menu_label_version = QLabel("v1.0.3")
        self.left_menu_label_version.setStyleSheet("font: 'Segoe UI'; color:#eeeee4")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)

        # Adicionado ao Layout
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_button_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        # Conteúdo
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282c34")

        # Barra Superior
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21252b")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)
        self.top_bar_layout.setSpacing(3)

        # Label Esquerda Superior
        self.top_label_left = QLabel("Ponto Fácil Project")
        self.top_label_left.setStyleSheet("font: 700 9pt 'Segoe UI'; color: #eeeee4")

        # Espacamento Barra Superior
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Label Direita Superior
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'; color: #eeeee4 ")

        # Adiciona ao Layout 
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)

        # Criando botões de Controle
        self.btn_min = PyTitleButton(
            icon_path = "icon_min.svg"

        )
        self.btn_max = PyTitleButton(
            icon_path = "icon_max.svg"

        )
        self.btn_close = PyTitleButton(
            icon_path = "icon_close.svg"

        )

        # Adicionando Botões ao Layout
        self.top_bar_layout.addWidget(self.btn_min)
        self.top_bar_layout.addWidget(self.btn_max)
        self.top_bar_layout.addWidget(self.btn_close)

        # Barra Inferior
        self.button_bar = QFrame()
        self.button_bar.setMaximumHeight(30)
        self.button_bar.setMinimumHeight(30)
        self.button_bar.setStyleSheet("background-color: #21252b")

        self.button_bar_layout = QHBoxLayout(self.button_bar)
        self.button_bar_layout.setContentsMargins(10,0,10,0)

        # Label Direita Superior
        self.button_label_left = QLabel("SolvedBySoftware™")
        self.button_label_left.setStyleSheet("font: 700 9pt 'Segoe UI'; color: #eeeee4")

        # Espacamento Barra Superior
        self.button_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Label Direita Superior
        self.button_label_right = QLabel("© 2022")
        self.button_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'; color: #eeeee4")

        # Adiciona ao Layout 
        self.button_bar_layout.addWidget(self.button_label_left)
        self.button_bar_layout.addItem(self.button_spacer)
        self.button_bar_layout.addWidget(self.button_label_right)

        # Pagina de Conteúdo
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #c8b7e9")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)

        # Conteudo do Layout 
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # Adicionando ao Conteudo do Layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.button_bar)

        # Adicionando Widget para Aplicação
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)


        # Set Central Widget
        parent.setCentralWidget(self.central_frame)