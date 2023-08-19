from PySide6.QtWidgets import QMainWindow
from ui.aluno_ui import Ui_JanelaAluno


class Aluno(QMainWindow, Ui_JanelaAluno):
    """
    Classe com funcionalidades da janela aluno.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
