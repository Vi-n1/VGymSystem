# -*- coding: utf-8 -*-
import sys
import psutil
from time import sleep
from threading import Thread
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.central_ui import Ui_JanelaCentral
from aluno import Aluno
from con_db.vgymsystem_db import VGymSystemDB


class VgymSystem(QMainWindow, Ui_JanelaCentral):
    """
    Classe principal.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.janela_aluno = None
        self.aplicacao_ativa = True
        self.GIGABYTE = 1_000_000_000
        self.vgymsystem_db = VGymSystemDB()
        self.pb_pagina_login.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2)
        )
        self.pb_pagina_cadastro.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(3)
        )
        self.pb_aluno.clicked.connect(self.exibir_janela_aluno)
        self.thead_visualizacao_recursos = Thread(
            target=self.informacoes_recursos_sistema
        )
        self.thead_visualizacao_recursos.start()

    # Cria uma instância da janela de aluno e exibe.
    def exibir_janela_aluno(self):
        self.janela_aluno = Aluno()
        self.janela_aluno.show()
        self.showMinimized()

    # Método responsável por acrescentar informações do uso dos recursos do computador.
    def informacoes_recursos_sistema(self):
        total_memoria = psutil.virtual_memory().total / self.GIGABYTE
        self.progress_bar_memoria.setMaximum(total_memoria)
        total_armazenamento = psutil.disk_usage('.').total / self.GIGABYTE
        self.progress_bar_armazenamento.setMaximum(total_armazenamento)
        while self.aplicacao_ativa:
            memoria_usada = psutil.virtual_memory().used / self.GIGABYTE
            self.progress_bar_memoria.setValue(memoria_usada)
            armazenamento_usado = psutil.disk_usage('.').used / self.GIGABYTE
            self.progress_bar_armazenamento.setValue(armazenamento_usado)
            sleep(2)

    def closeEvent(self, event):
        self.aplicacao_ativa = False
        self.vgymsystem_db.fechar_db()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = VgymSystem()
    janela.show()
    sys.exit(app.exec())
