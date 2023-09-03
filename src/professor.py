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

        # Data de hoje.
        self.DATA_HOJE = datetime.now().strftime('%d/%m/%y')

        # Constantes utilizadas para verificação de tamanho.
        self.QUANTIDADE_NUM_MATRICULA = 5
        self.INDEX_WHATSAPP = 5

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

        # Atribuindo o método que faz o pagamento.
        self.pb_pg_pagamentos_pagar.clicked.connect(self.efetuar_pagamento)

        self.pb_pg_pesquisar.clicked.connect(self.exibir_dados_pg_pesquisar)
        self.pb_pg_excluir_pesquisar.clicked.connect(
            self.exibir_dados_pg_excluir
        )

        # Exclui os dados.
        self.pb_pg_excluir_excluir_dados.clicked.connect(
            self.excluir_professor
        )

    # Converte a foto para binário e mostra uma visualização.
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

    # Verifica se os dados estão corretos e salva no banco.
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

    # Efetua o pagamento do salário.
    def efetuar_pagamento(self):
        matricula = self.le_pg_pagamentos.text()
        if len(matricula) == self.QUANTIDADE_NUM_MATRICULA:
            data_pagamento = self.DATA_HOJE[3:]
            transacao_aceita = self.vgymsystem_db.set_novo_pagamento_professor(
                matricula, data_pagamento
            )
            if transacao_aceita:
                self.exibir_mensagem(
                    'Pagamento efetuado', 'Pagamento efetuado com sucesso'
                )
            else:
                self.exibir_mensagem(
                    'Erro no pagamento', 'Digite novamente a matrícula'
                )
        else:
            self.exibir_mensagem(
                'Matrícula inválida', 'Digite novamente a matrícula'
            )

    # Exibi dados na página de 'pesquisar'.
    def exibir_dados_pg_pesquisar(self):
        identificador = self.le_pg_pesquisar.text()
        dados = self.pesquisar_dados(identificador)
        dados.pop(self.INDEX_WHATSAPP)
        self.l_pg_pesquisar_matricula.setText(f'{dados[0]}')
        self.l_pg_pesquisar_nome.setText(dados[1])
        self.l_pg_pesquisar_nascimento.setText(dados[2])
        self.l_pg_pesquisar_cpf.setText(dados[3])
        self.l_pg_pesquisar_celular.setText(dados[4])
        self.l_pg_pesquisar_email.setText(dados[5])
        self.l_pg_pesquisar_cidade.setText(dados[6])
        self.l_pg_pesquisar_bairro.setText(dados[7])
        self.l_pg_pesquisar_cep.setText(f'{dados[8]}')
        self.l_pg_pesquisar_formacao.setText(dados[9])
        self.l_pg_pesquisar_salario.setText(f'{dados[10]}')
        self.l_pg_pesquisar_pagamento.setText(f'{dados[11]}')
        foto = QPixmap()
        foto.loadFromData(dados[12])
        self.l_pg_pesquisar_foto.setPixmap(foto)

    # Exibi dados na página de 'excluir'.
    def exibir_dados_pg_excluir(self):
        identificador = self.le_pg_excluir_pesquisar.text()
        dados = self.pesquisar_dados(identificador)
        dados.pop(self.INDEX_WHATSAPP)
        self.l_pg_excluir_matricula.setText(f'{dados[0]}')
        self.l_pg_excluir_nome.setText(dados[1])
        self.l_pg_excluir_nascimento.setText(dados[2])
        self.l_pg_excluir_cpf.setText(dados[3])
        self.l_pg_excluir_celular.setText(dados[4])
        self.l_pg_excluir_email.setText(dados[5])
        self.l_pg_excluir_cidade.setText(dados[6])
        self.l_pg_excluir_bairro.setText(dados[7])
        self.l_pg_excluir_cep.setText(f'{dados[8]}')
        self.l_pg_excluir_formacao.setText(dados[9])
        self.l_pg_excluir_salario.setText(f'{dados[10]}')
        self.l_pg_excluir_pagamento.setText(f'{dados[11]}')
        foto = QPixmap()
        foto.loadFromData(dados[12])
        self.l_pg_excluir_foto.setPixmap(foto)

    # Excluí o professor do banco de dados.
    def excluir_professor(self):
        matricula = self.le_pg_excluir_pesquisar.text()
        if matricula.isnumeric():
            if len(matricula) == self.QUANTIDADE_NUM_MATRICULA:
                self.vgymsystem_db.excluir_professor(matricula)

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

            # Se a quantidade de números do identificador for igual a 11 é CPF.
            if quantidade_num_identificador == quantidade_num_cpf:
                dados = self.vgymsystem_db.get_professor_por_cpf(
                    identificador_unico
                )

            # Se a quantidade de números do identificador for igual a 5 é matrícula.
            elif quantidade_num_identificador == self.QUANTIDADE_NUM_MATRICULA:
                dados = self.vgymsystem_db.get_professor_por_matricula(
                    identificador_unico
                )

        # Se não tiver nenhum cadastro é exibido uma mensagem de erro.
        if dados is None:
            self.exibir_mensagem(
                'Dados inexistente', 'Nenhum aluno cadastrado'
            )
            return []
        else:
            return dados

    def salvar_dados(self, dados_tratados: list):
        """
        Salva os dados.
        Args:
            dados_tratados (list): Dados do professor.
        """
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
