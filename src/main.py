# -*- coding: utf-8 -*-
import sys
from time import sleep
import psutil
from threading import Thread
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.central_ui import Ui_JanelaCentral
from aluno import Aluno
from professor import Professor
from graficos import Graficos
from con_db.vgymsystem_db import VGymSystemDB
from util import exibir_mensagem


class VgymSystem(QMainWindow, Ui_JanelaCentral):
    """
    Classe principal.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.janela_aluno = None
        self.janela_professor = None
        self.janela_graficos = None
        self.aplicacao_ativa = True
        self.logado = False
        self.GIGABYTE = 1_000_000_000
        self.TITULO_MSG_ERRO = 'Erro no usuário'
        self.MSG_ERRO = 'Usuário não autorizado'
        self.vgymsystem_db = VGymSystemDB()
        self.pb_pagina_login.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2)
        )
        self.pb_pagina_cadastro.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(3)
        )
        self.pb_pagina_graficos.clicked.connect(self.exibir_janela_graficos)
        self.pb_aluno.clicked.connect(self.exibir_janela_aluno)
        self.pb_professor.clicked.connect(self.exibir_janela_professor)
        self.pb_confirmar_usuario.clicked.connect(self.logar)
        self.thead_visualizacao_recursos = Thread(
            target=self.informacoes_recursos_sistema
        )
        self.thead_visualizacao_recursos.start()

    # Cria uma instância da janela de aluno e exibe.
    def exibir_janela_aluno(self):
        if self.logado:
            self.janela_aluno = Aluno()
            self.janela_aluno.show()
            self.showMinimized()
        else:
            exibir_mensagem(self, self.TITULO_MSG_ERRO, self.MSG_ERRO)

    # Cria uma instância da janela de professor e exibe.
    def exibir_janela_professor(self):
        if self.logado:
            self.janela_professor = Professor()
            self.janela_professor.show()
            self.showMinimized()
        else:
            exibir_mensagem(self, self.TITULO_MSG_ERRO, self.MSG_ERRO)

    # Cria uma instância da janela de Graficos e exibe.
    def exibir_janela_graficos(self):
        if self.logado:
            self.janela_graficos = Graficos()
            self.janela_graficos.show()
            self.showMinimized()
        else:
            exibir_mensagem(self, self.TITULO_MSG_ERRO, self.MSG_ERRO)

    # Realiza o login no sistema.
    def logar(self):
        usuario_informado = self.le_usuario.text()
        senha_informada = self.le_senha.text()
        usuario, senha = self.vgymsystem_db.get_usuario()
        if usuario_informado == usuario and senha_informada == senha:
            self.logado = True
            self.l_status_login.setText(f'{{usuario}}')

    # Método responsável por acrescentar informações do uso dos recursos do computador.
    def informacoes_recursos_sistema(self):
        total_memoria = psutil.virtual_memory().total / self.GIGABYTE
        total_armazenamento = psutil.disk_usage('.').total / self.GIGABYTE
        self.progress_bar_memoria.setMaximum(total_memoria)
        self.progress_bar_armazenamento.setMaximum(total_armazenamento)
        while self.aplicacao_ativa:
            memoria_usada = psutil.virtual_memory().used / self.GIGABYTE
            self.progress_bar_memoria.setValue(memoria_usada)
            armazenamento_usado = psutil.disk_usage('.').used / self.GIGABYTE
            self.progress_bar_armazenamento.setValue(armazenamento_usado)
            sleep(1)

    # Se a janela for fechada a instância do banco de dados é fechado.
    def closeEvent(self, event):
        self.aplicacao_ativa = False
        self.vgymsystem_db.fechar_db()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = VgymSystem()
    janela.show()
    sys.exit(app.exec())
