# -*- coding: utf-8 -*-
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QTableWidgetItem,
)
from PySide6.QtGui import QPixmap
from ui.aluno_ui import Ui_JanelaAluno
from con_db.vgymsystem_db import VGymSystemDB


class Aluno(QMainWindow, Ui_JanelaAluno):
    """
    Classe com funcionalidades da janela aluno.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # binário das fotos
        self.binario_foto_aluno = ''
        self.binario_foto_responsavel = ''

        # números máximo de valores aceitos
        self.NUM_MAXIMO_VALOR_ACEITO = 14
        self.NUM_MAXIMO_CEP = 8

        # instância do banco
        self.vgymsystem_db = VGymSystemDB()

        # atribuindo as funções para trocar de página
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

        # atribuindo os métodos de adicionar imagem
        self.pb_ad_foto_aluno.clicked.connect(self.adicionar_foto_aluno)
        self.pb_ad_foto_responsavel.clicked.connect(
            self.adicionar_foto_responsavel
        )

        # se o estado do  ComboBox for alterado é chamado o método
        self.cb_responsavel.stateChanged.connect(self.aluno_independente)

        # chama o método que salva os dados no banco de dados
        self.pb_salvar_dados.clicked.connect(self.tratamento_dados)

    # Converte a foto do aluno para binário e mostra uma visualização.
    def adicionar_foto_aluno(self):
        caminho_foto_aluno = QFileDialog.getOpenFileName()[0]

        # obtendo o binário da foto
        with open(caminho_foto_aluno, 'rb') as file:
            cabecalho_foto = file.read(53)
            dados_pixel = file.read()
            imagem_montada = cabecalho_foto + dados_pixel

        foto = QPixmap()
        # se selecionar um arquivo inválido é exibido uma mensagem de erro
        if foto.loadFromData(imagem_montada):
            self.l_foto_aluno.setPixmap(foto)
            self.binario_foto_aluno = imagem_montada
        else:
            self.exibir_mensagem(
                titulo='Erro no carregamento imagem',
                mensagem='Imagem não suportada, formatos aceitos: BMP, JPG, JPEG e PNG',
            )

    # Converte a foto do responsável para binário e mostra uma visualização.
    def adicionar_foto_responsavel(self):
        caminho_foto_responsavel = QFileDialog.getOpenFileName()[0]

        # obtendo o binário da foto
        with open(caminho_foto_responsavel, 'rb') as file:
            cabecalho_foto = file.read(53)
            dados_pixel = file.read()
            imagem_montada = cabecalho_foto + dados_pixel

        foto = QPixmap()
        # se selecionar um arquivo inválido e exibido uma mensagem de erro
        if foto.loadFromData(imagem_montada):
            self.l_foto_responsavel.setPixmap(foto)
            self.binario_foto_responsavel = imagem_montada
        else:
            self.exibir_mensagem(
                titulo='Erro no carregamento imagem',
                mensagem='Imagem não suportada, formatos aceitos: BMP, JPG, JPEG e PNG',
            )

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

    # Verifica se os dados estão corretos e retorna os dados tratados
    def tratamento_dados(self):

        # verifica se tem algum número no nome
        if not self.le_nome_aluno.text().replace(' ', '').isalpha():
            self.exibir_mensagem(
                'Nome inválido', 'Digite novamente o nome do aluno'
            )

        # verifica a quantidade de valores digitado
        elif len(self.le_cpf_aluno.text()) < self.NUM_MAXIMO_VALOR_ACEITO:
            self.exibir_mensagem(
                'Cpf inválido', 'Digite novamente o cpf do aluno'
            )
        elif len(self.le_celular_aluno.text()) < self.NUM_MAXIMO_VALOR_ACEITO:
            self.exibir_mensagem(
                'Número inválido',
                'Digite novamente o número de celular do aluno',
            )

        # verifica se tem algum número no nome
        elif not self.le_bairro_aluno.text().replace(' ', '').isalpha():
            self.exibir_mensagem(
                'Bairro inválido', 'Digite novamente o nome do bairro do aluno'
            )

        # verifica a quantidade de valores digitado
        elif len(self.le_cep_aluno.text()) < self.NUM_MAXIMO_CEP:
            self.exibir_mensagem(
                'CEP inválido', 'Digite novamente o CEP do aluno'
            )

        # verifica se tem algum número no nome
        elif not self.le_cidade_aluno.text().replace(' ', '').isalpha():
            self.exibir_mensagem(
                'Cidade inválida', 'Digite novamente o nome da cidade do aluno'
            )

        # verifica se tem algum arroba no nome
        elif self.le_email_aluno.text().count('@') != 1:
            self.exibir_mensagem(
                'E-mail inválido', 'Digite novamente o e-mail do aluno'
            )

        else:
            # retira os espaços em branco
            nome_aluno = self.le_nome_aluno.text().replace(' ', '')
            bairro_aluno = self.le_bairro_aluno.text().replace(' ', '')
            cidade_aluno = self.le_cidade_aluno.text().replace(' ', '')
            email_aluno = self.le_email_aluno.text().replace(' ', '')

            # de xxx.xxx.xxx-xx para xxxxxxxxxxx
            cpf_aluno = self.le_cpf_aluno.text().replace('.', '')
            cpf_aluno = cpf_aluno.replace('-', '')

            # de (xx)xxxxx-xxxx para xxxxxxxxxxx
            num_celular_aluno = self.le_celular_aluno.text().replace('(', '')
            num_celular_aluno = num_celular_aluno.replace(')', '')
            num_celular_aluno = num_celular_aluno.replace('-', '')

            # de xxxxx-xxx para xxxxxxxx
            cep_aluno = self.le_cep_aluno.text().replace('-', '')

            # verifica se o número é whatsapp
            if self.cb_whatsapp_aluno.isChecked():
                whatsapp = 1
            else:
                whatsapp = 0

            # obtem os dados digitados
            dados_aluno = [
                nome_aluno,
                self.de_data_nascimento.text(),
                cpf_aluno,
                num_celular_aluno,
                whatsapp,
                bairro_aluno,
                cep_aluno,
                cidade_aluno,
                email_aluno,
                self.sb_data_pagamento.value(),
                self.sb_valor_pagamento.value(),
                str(self.binario_foto_aluno),
            ]
            if not self.cb_responsavel.isChecked():

                # verifica se tem algum número no nome
                if (
                    not self.le_nome_responsavel.text()
                    .replace(' ', '')
                    .isalpha()
                ):
                    self.exibir_mensagem(
                        'Nome inválido',
                        'Digite novamente o nome do responsável',
                    )

                # verifica a quantidade de valores digitado
                elif (
                    len(self.le_cpf_responsavel.text())
                    < self.NUM_MAXIMO_VALOR_ACEITO
                ):
                    self.exibir_mensagem(
                        'Cpf inválido', 'Digite novamente o cpf do responsável'
                    )
                elif (
                    len(self.le_celular_responsavel.text())
                    < self.NUM_MAXIMO_VALOR_ACEITO
                ):
                    self.exibir_mensagem(
                        'Número inválido',
                        'Digite novamente o número de celular do responsável',
                    )

                # verifica se tem algum número no nome
                elif (
                    not self.le_bairro_responsavel.text()
                    .replace(' ', '')
                    .isalpha()
                ):
                    self.exibir_mensagem(
                        'Bairro inválido',
                        'Digite novamente o nome do bairro do responsável',
                    )

                # verifica a quantidade de valores digitado
                elif len(self.le_cep_responsavel.text()) < self.NUM_MAXIMO_CEP:
                    self.exibir_mensagem(
                        'CEP inválido', 'Digite novamente o CEP do responsável'
                    )

                # verifica se tem algum número no nome
                elif (
                    not self.le_cidade_responsavel.text()
                    .replace(' ', '')
                    .isalpha()
                ):
                    self.exibir_mensagem(
                        'Cidade inválida',
                        'Digite novamente o nome da cidade do responsável',
                    )

                # verifica se tem algum arroba no nome
                elif self.le_email_responsavel.text().count('@') != 1:
                    self.exibir_mensagem(
                        'E-mail inválido',
                        'Digite novamente o e-mail do responsável',
                    )

                else:
                    # retira os espaços em branco
                    nome_responsavel = self.le_nome_responsavel.text().replace(
                        ' ', ''
                    )
                    bairro_responsavel = (
                        self.le_bairro_responsavel.text().replace(' ', '')
                    )
                    cidade_responsavel = (
                        self.le_cidade_responsavel.text().replace(' ', '')
                    )
                    email_responsavel = (
                        self.le_email_responsavel.text().replace(' ', '')
                    )

                    # de xxx.xxx.xxx-xx para xxxxxxxxxxx
                    cpf_responsavel = self.le_cpf_responsavel.text().replace(
                        '.', ''
                    )
                    cpf_responsavel = cpf_responsavel.replace('-', '')

                    # de (xx)xxxxx-xxxx para xxxxxxxxxxx
                    num_celular_responsavel = (
                        self.le_celular_responsavel.text().replace('(', '')
                    )
                    num_celular_responsavel = num_celular_responsavel.replace(
                        ')', ''
                    )
                    num_celular_responsavel = num_celular_responsavel.replace(
                        '-', ''
                    )

                    # de xxxxx-xxx para xxxxxxxx
                    cep_responsavel = self.le_cep_responsavel.text().replace(
                        '-', ''
                    )

                    # obtem os dados digitados
                    dados_responsavel = [
                        nome_responsavel,
                        self.de_data_nascimento_responsavel.text(),
                        cpf_responsavel,
                        num_celular_responsavel,
                        whatsapp,
                        bairro_responsavel,
                        cep_responsavel,
                        cidade_responsavel,
                        email_responsavel,
                        str(self.binario_foto_responsavel)
                    ]
                    dados = [dados_aluno, dados_responsavel]
                    self.salvar_dados(dados)
            else:
                self.salvar_dados(dados_aluno)

    def salvar_dados(self, dados_tratados):
        contem_responsavel = 2

        # se o tamanho de :dados_tratados: for 2 o aluno é dependente
        if len(dados_tratados) == contem_responsavel:
            matricula_aluno = self.vgymsystem_db.get_nova_matricula_aluno()
            matricula_responsavel = (
                self.vgymsystem_db.get_nova_matricula_responsavel()
            )

            # insere a matrícula do aluno na primeira posição
            dados_tratados[0].insert(0, matricula_aluno)

            # insere a matrícula do responsável na última posição
            dados_tratados[0].insert(
                len(dados_tratados[0]), matricula_responsavel
            )

            # inserindo dados do aluno dependente e obtendo o resultado da transação
            commit_aluno = self.vgymsystem_db.set_novo_aluno(
                *dados_tratados[0]
            )

            # inserindo dados do responsável primeira posição
            dados_tratados[1].insert(0, matricula_responsavel)

            # inserindo dados do responsável e obtendo o resultado da transação
            commit_responsavel = self.vgymsystem_db.set_novo_responsavel(
                *dados_tratados[1]
            )

            # verifica se ocorreu algum erro na transação
            if not commit_aluno and commit_responsavel:
                self.exibir_mensagem(
                    'Dados inválido', 'Digite novamente os dados'
                )
            else:
                self.exibir_mensagem('Sucesso', 'Dados salvos com sucesso')

        else:
            matricula_aluno = self.vgymsystem_db.get_nova_matricula_aluno()

            # insere a matrícula do aluno na primeira posição
            dados_tratados.insert(0, matricula_aluno)

            # insere a matrícula do aluno na última posição
            dados_tratados.insert(len(dados_tratados), matricula_aluno)

            # inserindo dados do aluno independente e obtendo o resultado da transação
            commit_aluno = self.vgymsystem_db.set_novo_aluno(*dados_tratados)
            if not commit_aluno:
                self.exibir_mensagem(
                    'Dados inválido', 'Digite novamente os dados'
                )
            else:
                self.exibir_mensagem('Sucesso', 'Dados salvos com sucesso')

    # se a janela for fechada a instância do banco de dados é fechado
    def closeEvent(self, event):
        self.vgymsystem_db.fechar_db()

    # Exibi uma mensagem passada por parâmetro.
    def exibir_mensagem(self, titulo, mensagem) -> None:
        erro = QMessageBox(self)
        erro.setWindowTitle(titulo)
        erro.setText(mensagem)
        erro.open()
