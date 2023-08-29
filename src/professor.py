# -*- coding: utf-8 -*-
from datetime import datetime
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QPixmap
from ui.professor_ui import Ui_Professor
from con_db.vgymsystem_db import VGymSystemDB


class Professor(QMainWindow, Ui_Professor):
    """
    Classe com funcionalidades da janela professor.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Data de hoje
        self.DATA_HOJE = datetime.now().strftime('%d/%m/%y')

        # Binário da fotos.
        self.binario_foto = ''

        # Instância do banco.
        self.vgymsystem_db = VGymSystemDB()

        # Atribuindo as funções para trocar de página.
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

        # Atribuindo o métodos de adicionar imagem.
        self.pb_novo_ad_foto.clicked.connect(self.adicionar_foto)

        # Atribuindo o método que faz o tratamento de dados e salva os dados no banco.
        self.pb_pg_novo_salvar_dados.clicked.connect(self.tratamento_dados)

    def adicionar_foto(self):
        caminho_foto = QFileDialog.getOpenFileName(self)[0]

        # Obtendo o binário da foto.
        with open(caminho_foto, 'rb') as arquivo:
            cabecalho_foto = arquivo.read(53)
            dados_pixel = arquivo.read()
            imagem_montada = cabecalho_foto + dados_pixel

        foto = QPixmap()
        # Se selecionar um arquivo inválido é exibido uma mensagem de erro.
        if foto.loadFromData(imagem_montada):
            self.l_pg_novo_ad_foto.setPixmap(foto)
            self.binario_foto = imagem_montada
        else:
            self.exibir_mensagem(
                titulo='Erro no carregamento imagem',
                mensagem='Imagem não suportada, formatos aceitos: BMP, JPG, JPEG e PNG',
            )

    def tratamento_dados(self):
        if not self.le_pg_novo_nome.text().replace(' ', '').isalpha():
            self.exibir_mensagem('Nome inválido', 'Digite novamente o nome')
        elif not self.le_pg_novo_cpf.text().isnumeric():
            self.exibir_mensagem('CPF inválido', 'Digite novamente o CPF')
        elif not self.le_pg_novo_celular.text().isnumeric():
            self.exibir_mensagem(
                'Número inválido', 'Digite novamente o número do celular'
            )
        elif self.le_pg_novo_email.text().replace(' ', '').count('@') != 1:
            self.exibir_mensagem(
                'E-mail inválido', 'Digite novamente o e-mail'
            )
        elif not self.le_pg_novo_cidade.text().replace(' ', '').isalpha():
            self.exibir_mensagem(
                'Cidade inválida', 'Digite novamente o nome da cidade'
            )
        elif not self.le_pg_novo_bairro.text().replace(' ', '').isalpha():
            self.exibir_mensagem(
                'Bairro inválido', 'Digite novamente o nome do bairro'
            )
        elif not self.le_pg_novo_cep.text().isnumeric():
            self.exibir_mensagem('CEP inválido', 'Digite novamente o CEP')
        elif not self.combobox_novo_formacao.currentIndex() >= 0:
            self.exibir_mensagem(
                'Formação acadêmica inválido', 'Selecione uma das opções'
            )
        else:
            # Retira os espaços em branco.
            nome = self.le_pg_novo_nome.text().replace(' ', '')
            email = self.le_pg_novo_email.text().replace(' ', '')
            cidade = self.le_pg_novo_cidade.text().replace(' ', '')
            bairro = self.le_pg_novo_bairro.text().replace(' ', '')

            # Verifica se o número é whatsapp.
            if self.checkbox_pg_novo_whatsapp.isChecked():
                whatsapp = 1
            else:
                whatsapp = 0

            dados = [
                nome,
                self.de_novo_data_nascimento.text(),
                self.le_pg_novo_cpf.text(),
                self.le_pg_novo_celular.text(),
                whatsapp,
                email,
                cidade,
                bairro,
                self.le_pg_novo_cep.text(),
                self.combobox_novo_formacao.currentText(),
                self.sb_pg_novo_salario.value(),
                self.sb_pg_novo_pagamento.value(),
                self.binario_foto,
                self.DATA_HOJE,
            ]
            self.salvar_dados(dados)

    # *
    def salvar_dados(self, dados_tratados: list):
        matricula = self.vgymsystem_db.get_nova_matricula_professor()

        # Inserindo a matrícula na primeira posição.
        dados_tratados.insert(0, matricula)
        self.vgymsystem_db.set_novo_professor(*dados_tratados)

    # Exibi uma mensagem passada por parâmetro.
    def exibir_mensagem(self, titulo, mensagem) -> None:
        erro = QMessageBox(self)
        erro.setWindowTitle(titulo)
        erro.setText(mensagem)
        erro.open()
