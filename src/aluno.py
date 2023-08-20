# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
from ui.aluno_ui import Ui_JanelaAluno


class Aluno(QMainWindow, Ui_JanelaAluno):
    """
    Classe com funcionalidades da janela aluno.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bytes_foto_aluno = ''
        self.bytes_foto_responsavel = ''
        self.pb_pagina_pagamento.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0)
        )
        self.pb_pagina_ad_aluno.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1)
        )
        self.pb_pagina_excluir_aluno.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2)
        )
        self.pb_pagina_pesquisar_aluno.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(3)
        )
        self.pb_ad_foto_aluno.clicked.connect(self.adicionar_foto_aluno)
        self.pb_ad_foto_responsavel.clicked.connect(
            self.adicionar_foto_responsavel
        )
        self.cb_responsavel.stateChanged.connect(self.aluno_independente)

    # Desativa a sessão de responsável se o checkBox estiver ativo e ativa se o checkBox estiver desativado.
    def aluno_independente(self):
        responsavel_selecionado = not (self.cb_responsavel.isChecked())
        self.le_nome_responsavel.setEnabled(responsavel_selecionado)
        self.de_data_nascimento_responsavel.setEnabled(responsavel_selecionado)
        self.le_cpf_responsavel.setEnabled(responsavel_selecionado)
        self.le_celular_responsavel.setEnabled(responsavel_selecionado)
        self.le_bairro_responsavel.setEnabled(responsavel_selecionado)
        self.le_cep_responsavel.setEnabled(responsavel_selecionado)
        self.le_cidade_responsavel.setEnabled(responsavel_selecionado)
        self.le_email_responsavel.setEnabled(responsavel_selecionado)
        self.pb_ad_foto_responsavel.setEnabled(responsavel_selecionado)

    # Exibi uma mensagem passada por parâmetro.
    def mensagem_erro(self, titulo, mensagem):
        erro = QMessageBox(self)
        erro.setWindowTitle(titulo)
        erro.setText(mensagem)
        erro.open()

    # Converte a foto do aluno para binário e mostra uma visualização.
    def adicionar_foto_aluno(self):
        caminho_foto_aluno = QFileDialog.getOpenFileName()[0]
        with open(caminho_foto_aluno, 'rb') as file:
            cabecalho_foto = file.read(53)
            dados_pixel = file.read()
            imagem_montada = cabecalho_foto + dados_pixel
        foto = QPixmap()
        if foto.loadFromData(imagem_montada):
            self.l_foto_aluno.setPixmap(foto)
            self.bytes_foto_aluno = imagem_montada
        else:
            self.mensagem_erro(
                titulo='Erro no carregamento imagem',
                mensagem='Imagem não suportada, formatos aceitos: BMP, JPG, JPEG e PNG',
            )

    # Converte a foto do responsável para binário e mostra uma visualização.
    def adicionar_foto_responsavel(self):
        caminho_foto_responsavel = QFileDialog.getOpenFileName()[0]
        with open(caminho_foto_responsavel, 'rb') as file:
            cabecalho_foto = file.read(53)
            dados_pixel = file.read()
            imagem_montada = cabecalho_foto + dados_pixel
        foto = QPixmap()
        if foto.loadFromData(imagem_montada):
            self.l_foto_responsavel.setPixmap(foto)
            self.bytes_foto_responsavel = imagem_montada
        else:
            self.mensagem_erro(
                titulo='Erro no carregamento imagem',
                mensagem='Imagem não suportada, formatos aceitos: BMP, JPG, JPEG e PNG',
            )
