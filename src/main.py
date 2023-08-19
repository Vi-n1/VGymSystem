import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.central_ui import Ui_JanelaCentral
from aluno import Aluno


class VgymSystem(QMainWindow, Ui_JanelaCentral):
    """
    Classe principal.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.janela_aluno = None
        self.pb_pagina_login.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2)
        )
        self.pb_pagina_cadastro.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(3)
        )
        self.pb_aluno.clicked.connect(self.exibir_janela_aluno)

    def exibir_janela_aluno(self):
        self.janela_aluno = Aluno()
        self.janela_aluno.show()
        self.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = VgymSystem()
    janela.show()
    sys.exit(app.exec())
