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
        # Binário das fotos.
        self.binario_foto_aluno = ''
        self.binario_foto_responsavel = ''

        # Números máximo de valores aceitos.
        self.NUM_MAXIMO_VALOR_ACEITO = 14
        self.NUM_MAXIMO_CEP = 8

        # Instância do banco.
        self.vgymsystem_db = VGymSystemDB()

        # Atribuindo as funções para trocar de página.
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

        # Atribuindo os métodos de adicionar imagem.
        self.pb_ad_foto_aluno.clicked.connect(self.adicionar_foto_aluno)
        self.pb_ad_foto_responsavel.clicked.connect(
            self.adicionar_foto_responsavel
        )

        # Se o estado do  ComboBox for alterado é chamado o método.
        self.cb_responsavel.stateChanged.connect(self.aluno_independente)

        # Chama o método que salva os dados no banco de dados.
        self.pb_salvar_dados.clicked.connect(self.tratamento_dados)
        self.pb_pesquisar_pagamentos.clicked.connect(self.visualizar_debitos)
        self.pb_pesquisar_aluno.clicked.connect(self.visualizar_aluno)
        self.pb_pesquisar_excluir.clicked.connect(
            self.visualizar_excluir_aluno
        )

    # Converte a foto do aluno para binário e mostra uma visualização.
    def adicionar_foto_aluno(self):
        caminho_foto_aluno = QFileDialog.getOpenFileName()[0]

        # Obtendo o binário da foto.
        with open(caminho_foto_aluno, 'rb') as file:
            cabecalho_foto = file.read(53)
            dados_pixel = file.read()
            imagem_montada = cabecalho_foto + dados_pixel

        foto = QPixmap()
        # Se selecionar um arquivo inválido é exibido uma mensagem de erro.
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

        # Obtendo o binário da foto.
        with open(caminho_foto_responsavel, 'rb') as file:
            cabecalho_foto = file.read(53)
            dados_pixel = file.read()
            imagem_montada = cabecalho_foto + dados_pixel

        foto = QPixmap()
        # Se selecionar um arquivo inválido e exibido uma mensagem de erro.
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

    # Verifica se os dados estão corretos e retorna os dados tratados.
    def tratamento_dados(self):

        # Verifica se tem algum número no nome.
        if not self.le_nome_aluno.text().replace(' ', '').isalpha():
            self.exibir_mensagem(
                'Nome inválido', 'Digite novamente o nome do aluno'
            )

        # Verifica a quantidade de valores digitado.
        elif len(self.le_cpf_aluno.text()) < self.NUM_MAXIMO_VALOR_ACEITO:
            self.exibir_mensagem(
                'Cpf inválido', 'Digite novamente o cpf do aluno'
            )
        elif len(self.le_celular_aluno.text()) < self.NUM_MAXIMO_VALOR_ACEITO:
            self.exibir_mensagem(
                'Número inválido',
                'Digite novamente o número de celular do aluno',
            )

        # Verifica se tem algum número no nome.
        elif not self.le_bairro_aluno.text().replace(' ', '').isalpha():
            self.exibir_mensagem(
                'Bairro inválido', 'Digite novamente o nome do bairro do aluno'
            )

        # Verifica a quantidade de valores digitado.
        elif len(self.le_cep_aluno.text()) < self.NUM_MAXIMO_CEP:
            self.exibir_mensagem(
                'CEP inválido', 'Digite novamente o CEP do aluno'
            )

        # Verifica se tem algum número no nome.
        elif not self.le_cidade_aluno.text().replace(' ', '').isalpha():
            self.exibir_mensagem(
                'Cidade inválida', 'Digite novamente o nome da cidade do aluno'
            )

        # Verifica se tem algum arroba no nome.
        elif self.le_email_aluno.text().count('@') != 1:
            self.exibir_mensagem(
                'E-mail inválido', 'Digite novamente o e-mail do aluno'
            )

        else:
            # Retira os espaços em branco.
            nome_aluno = self.le_nome_aluno.text().replace(' ', '')
            bairro_aluno = self.le_bairro_aluno.text().replace(' ', '')
            cidade_aluno = self.le_cidade_aluno.text().replace(' ', '')
            email_aluno = self.le_email_aluno.text().replace(' ', '')

            # De xxx.xxx.xxx-xx para xxxxxxxxxxx.
            cpf_aluno = self.le_cpf_aluno.text().replace('.', '')
            cpf_aluno = cpf_aluno.replace('-', '')

            # De (xx)xxxxx-xxxx para xxxxxxxxxxx.
            num_celular_aluno = self.le_celular_aluno.text().replace('(', '')
            num_celular_aluno = num_celular_aluno.replace(')', '')
            num_celular_aluno = num_celular_aluno.replace('-', '')

            # De xxxxx-xxx para xxxxxxxx.
            cep_aluno = self.le_cep_aluno.text().replace('-', '')

            # Verifica se o número é whatsapp.
            if self.cb_whatsapp_aluno.isChecked():
                whatsapp = 1
            else:
                whatsapp = 0

            # Obtêm os dados digitados.
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

                # Verifica se tem algum número no nome.
                if (
                    not self.le_nome_responsavel.text()
                    .replace(' ', '')
                    .isalpha()
                ):
                    self.exibir_mensagem(
                        'Nome inválido',
                        'Digite novamente o nome do responsável',
                    )

                # Verifica a quantidade de valores digitado.
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

                # Verifica se tem algum número no nome.
                elif (
                    not self.le_bairro_responsavel.text()
                    .replace(' ', '')
                    .isalpha()
                ):
                    self.exibir_mensagem(
                        'Bairro inválido',
                        'Digite novamente o nome do bairro do responsável',
                    )

                # Verifica a quantidade de valores digitado.
                elif len(self.le_cep_responsavel.text()) < self.NUM_MAXIMO_CEP:
                    self.exibir_mensagem(
                        'CEP inválido', 'Digite novamente o CEP do responsável'
                    )

                # Verifica se tem algum número no nome.
                elif (
                    not self.le_cidade_responsavel.text()
                    .replace(' ', '')
                    .isalpha()
                ):
                    self.exibir_mensagem(
                        'Cidade inválida',
                        'Digite novamente o nome da cidade do responsável',
                    )

                # Verifica se tem algum arroba no nome.
                elif self.le_email_responsavel.text().count('@') != 1:
                    self.exibir_mensagem(
                        'E-mail inválido',
                        'Digite novamente o e-mail do responsável',
                    )

                else:
                    # Retira os espaços em branco.
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

                    # De xxx.xxx.xxx-xx para xxxxxxxxxxx.
                    cpf_responsavel = self.le_cpf_responsavel.text().replace(
                        '.', ''
                    )
                    cpf_responsavel = cpf_responsavel.replace('-', '')

                    # De (xx)xxxxx-xxxx para xxxxxxxxxxx.
                    num_celular_responsavel = (
                        self.le_celular_responsavel.text().replace('(', '')
                    )
                    num_celular_responsavel = num_celular_responsavel.replace(
                        ')', ''
                    )
                    num_celular_responsavel = num_celular_responsavel.replace(
                        '-', ''
                    )

                    # De xxxxx-xxx para xxxxxxxx.
                    cep_responsavel = self.le_cep_responsavel.text().replace(
                        '-', ''
                    )

                    # Obtêm os dados digitados.
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
                        str(self.binario_foto_responsavel),
                    ]
                    dados = [dados_aluno, dados_responsavel]
                    self.salvar_dados(dados)
            else:
                self.salvar_dados(dados_aluno)

    # Exibi dados na tabela da página de 'pagamentos'.
    def visualizar_debitos(self):
        identificador_informado = self.le_pagamentos.text()
        dados = self.pesquisar_dados(identificador_informado)
        self.tw_pagamentos.setRowCount(1)
        linha = 0

        # Adicionando valor na tabela.
        for coluna in range(0, len(dados)):
            valor = QTableWidgetItem(f'{dados[coluna]}')
            self.tw_pagamentos.setItem(linha, coluna, valor)

    # Exibi dados na tabela da página de 'pesquisar alunos'.
    def visualizar_aluno(self):
        identificador_informado = self.le_pesquisar_aluno.text()
        dados = self.pesquisar_dados(identificador_informado)
        self.tw_exibir_pesquisar_aluno.setRowCount(1)
        linha = 0

        # Adicionando valor na tabela.
        for coluna in range(0, len(dados)):
            valor = QTableWidgetItem(f'{dados[coluna]}')
            self.tw_exibir_pesquisar_aluno.setItem(linha, coluna, valor)

    # Exibi dados na tabela da página de 'excluir alunos'.
    def visualizar_excluir_aluno(self):
        identificador_informado = self.le_excluir_aluno.text()
        dados = self.pesquisar_dados(identificador_informado)
        self.tw_exibir_excluir_aluno.setRowCount(1)
        linha = 0

        # Adicionando valor na tabela.
        for coluna in range(0, len(dados)):
            valor = QTableWidgetItem(f'{dados[coluna]}')
            self.tw_exibir_excluir_aluno.setItem(linha, coluna, valor)

    def pesquisar_dados(self, identificador_unico: str) -> list:
        """
        Pesquisa dados do identificador único.
        Args:
            identificador_unico (str): Matrícula ou CPF.
        Returns:
            list: Lista com os dados.
        """
        dados = None
        quantidade_num_identificador = len(identificador_unico)
        if identificador_unico.isnumeric():
            quantidade_num_cpf = 11
            quantidade_num_matricula = 5

            # Se a quantidade de números do identificador for igual a 11 é CPF.
            if quantidade_num_identificador == quantidade_num_cpf:
                dados = self.vgymsystem_db.get_aluno_por_cpf(
                    identificador_unico
                )

            # Se a quantidade de números do identificador for igual a 5 é matrícula.
            elif quantidade_num_identificador == quantidade_num_matricula:
                dados = self.vgymsystem_db.get_aluno_por_matricula(
                    identificador_unico
                )

        # Se não tiver nenhum aluno cadastrado a variável é none.
        if dados is None:
            self.exibir_mensagem(
                'Dados inexistente', 'Nenhum aluno cadastrado'
            )
            return []
        else:
            index_foto = -2
            dados.pop(index_foto)
            return dados

    def salvar_dados(self, dados_tratados: list | list[list, list]):
        """
        Salva dados de aluno e/ou responsável.
        Args:
            dados_tratados (list | list[list, list]): Dados sem erros.
        """
        contem_responsavel = 2

        # Se o tamanho de dados_tratados for 2 o aluno é dependente.
        if len(dados_tratados) == contem_responsavel:
            matricula_aluno = self.vgymsystem_db.get_nova_matricula_aluno()
            matricula_responsavel = (
                self.vgymsystem_db.get_nova_matricula_responsavel()
            )

            # Insere a matrícula do aluno na primeira posição.
            dados_tratados[0].insert(0, matricula_aluno)

            # Insere a matrícula do responsável na última posição.
            dados_tratados[0].insert(
                len(dados_tratados[0]), matricula_responsavel
            )

            # Inserindo dados do aluno dependente e obtendo o resultado da transação.
            commit_aluno = self.vgymsystem_db.set_novo_aluno(
                *dados_tratados[0]
            )

            # Inserindo dados do responsável primeira posição.
            dados_tratados[1].insert(0, matricula_responsavel)

            # Inserindo dados do responsável e obtendo o resultado da transação.
            commit_responsavel = self.vgymsystem_db.set_novo_responsavel(
                *dados_tratados[1]
            )

            # Verifica se ocorreu algum erro na transação.
            if not commit_aluno and commit_responsavel:
                self.exibir_mensagem(
                    'Dados inválido', 'Digite novamente os dados'
                )
            else:
                self.exibir_mensagem('Sucesso', 'Dados salvos com sucesso')

        else:
            matricula_aluno = self.vgymsystem_db.get_nova_matricula_aluno()

            # Insere a matrícula do aluno na primeira posição.
            dados_tratados.insert(0, matricula_aluno)

            # Insere a matrícula do aluno na última posição.
            dados_tratados.insert(len(dados_tratados), matricula_aluno)

            # Inserindo dados do aluno independente e obtendo o resultado da transação.
            commit_aluno = self.vgymsystem_db.set_novo_aluno(*dados_tratados)
            if not commit_aluno:
                self.exibir_mensagem(
                    'Dados inválido', 'Digite novamente os dados'
                )
            else:
                self.exibir_mensagem('Sucesso', 'Dados salvos com sucesso')

    # Se a janela for fechada a instância do banco de dados é fechado.
    def closeEvent(self, event):
        self.vgymsystem_db.fechar_db()

    # Exibi uma mensagem passada por parâmetro.
    def exibir_mensagem(self, titulo, mensagem) -> None:
        erro = QMessageBox(self)
        erro.setWindowTitle(titulo)
        erro.setText(mensagem)
        erro.open()
