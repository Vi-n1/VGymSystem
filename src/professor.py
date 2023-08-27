from PySide6.QtWidgets import QMainWindow
from ui.professor_ui import Ui_Professor


class Professor(QMainWindow, Ui_Professor):
    """
    Classe com funcionalidades da janela professor.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_pagina_pagamento.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(3)
        )
        self.pb_pagina_ad_prof.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0)
        )
        self.pb_pagina_excluir_prof.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2)
        )
        self.pb_pagina_pesquisar_prof.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1)
        )
