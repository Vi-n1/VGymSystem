# -*- coding: utf-8 -*-
from datetime import datetime
from PySide6.QtWidgets import QMainWindow
from _graficos_core import _GraficosCore as Core
from ui.graficos_ui import Ui_Graficos
from con_db.vgymsystem_db import VGymSystemDB


class Graficos(QMainWindow, Core, Ui_Graficos):
    """
    Classe que manipula os dados para a exibição de gráficos.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Dados dos alunos.
        self.alunos = []
        self.pagamentos_alunos = []

        # Dados dos professores.
        self.professores = []
        self.pagamentos_professores = []

        self.DATA = datetime.now().strftime('%d/%m/%y')

        # Instância do banco.
        self.vgymsystem_db = VGymSystemDB()

        # Busca de dados.
        self.buscar_dados_alunos()
        self.buscar_dados_professores()

        # Plotando.
        self.plt_ganhos_mensais()
        self.plt_matriculas_pagas()
        self.plt_salarios_pagos()

    # Plot de ganhos mensais.
    def plt_ganhos_mensais(self):
        # Dicionário com as categorias e valores dos alunos.
        dados_alunos = self.tratamento_categorias(
            self.pagamentos_alunos, self.alunos
        )

        # Verifica se tem algum aluno no banco de dados.
        if dados_alunos:

            # Dicionário com as categorias e valores dos professores.
            dados_professores = self.tratamento_categorias(
                self.pagamentos_professores, self.professores
            )

            # Dicionário que vai conter todas as categorias e valores.
            categorias = {}

            # A quantidade de alunos sempre deverá ser maior que a de professores.
            quantidade_alunos = len(dados_alunos)
            for index in range(0, quantidade_alunos):

                # categoria dos alunos.
                categoria = list(dados_alunos.keys())[index]

                # categorias dos professores.
                categorias_professores = list(dados_professores.keys())

                # Se a categoria dos alunos estar contido em categorias dos professores -
                # é somado os valores das categorias.
                if categoria in categorias_professores:
                    novo_valor = (
                        dados_alunos[categoria] - dados_professores[categoria]
                    )
                    categorias.update({categoria: novo_valor})

                # Adiciona uma nova categoria.
                else:
                    categorias.update({categoria: dados_alunos[categoria]})

            categorias_ordenadas = []
            quantidade_categorias = len(categorias)
            # Adiciona as categorias na lista para ordenação.
            for i in range(0, quantidade_categorias):
                categorias_ordenadas.append(categorias.popitem())

            # Ordena a lista e transforma em dicionário.
            categorias_ordenadas.sort()
            categorias_ordenadas = dict(categorias_ordenadas)

            titulo = 'Ganhos'
            titulo_vertical = 'Total ganhos R$'
            titulo_horizontal = 'Meses'

            # Plot.
            self.barra(
                titulo,
                titulo_vertical,
                titulo_horizontal,
                list(categorias_ordenadas.keys()),
                list(categorias_ordenadas.values()),
                self.vl_grafico_barra,
            )

    # Plot de salários pagos.
    def plt_salarios_pagos(self):
        # Quantidade de salários pagos e não pagos.
        pago, nao_pago = self.pagamento_mes_atual(self.pagamentos_professores)

        # Verifica se tem algum pagamento.
        if pago:
            titulo = f'Salários do Mês {self.DATA[3:]}'
            nomes_fatias = [f'Pago [{pago}]', f'Não Pago [{nao_pago}]']
            valores = [pago, nao_pago]

            # Plot.
            self.pizza(titulo, nomes_fatias, valores, self.vl_grafico_pizza1)

    # Plot de matrículas pagas.
    def plt_matriculas_pagas(self):
        # Quantidade de matrículas pagas e não pagas.
        paga, nao_paga = self.pagamento_mes_atual(self.pagamentos_alunos)

        # Verifica se tem algum pagamento.
        if paga:
            titulo = f'Matrículas do Mês {self.DATA[3:]}'
            nomes_fatias = [f'Pagas [{paga}]', f'Não Pagas [{nao_paga}]']
            valores = [paga, nao_paga]

            # Plot.
            self.pizza(titulo, nomes_fatias, valores, self.vl_grafico_pizza2)

    @staticmethod
    def tratamento_categorias(
        pagamentos: list[tuple], dados: list[any]
    ) -> dict:
        """
        Faz o tratamento dos dados separando por categorias e valores.
        Args:
            pagamentos (list[tuple]): Lista com matrículas e meses de pagamentos.
            dados: Dados dos professores/alunos.
        Returns:
            dict: Dicionario contedo as categorias e os valores. Ex: {categoria: valor, ...}.
        """
        index_valor_pagamento = 11
        quantidade_pagamentos = len(pagamentos)
        categorias = {}

        for index in range(0, quantidade_pagamentos):

            # Verifica se o campo de mes_ano_pago não estar vazio.
            if not dados[1] == '\x20':
                matricula = pagamentos[index][0]
                data_pagamentos = pagamentos[index][1].split()

                # Data pagamento ex: 00/00.
                for data_pagamento in data_pagamentos:

                    # Para evitar a seleção da pessoa errada é necessário verifica o número da matrícula.
                    if matricula in pagamentos[index]:

                        # Se a chave já existir no dicionário é somado o valor atual com o valor de pagamento.
                        if data_pagamento in list(categorias.keys()):

                            # Soma do valor atual com o valor do pagamento.
                            novo_valor = (
                                categorias[data_pagamento]
                                + dados[index][index_valor_pagamento]
                            )

                            # Atualizando a chave para um novo valor.
                            categorias.update({data_pagamento: novo_valor})

                        # Adiciona uma nova chave/valor.
                        else:
                            categorias.update(
                                {
                                    data_pagamento: dados[index][
                                        index_valor_pagamento
                                    ]
                                }
                            )

        return categorias

    def pagamento_mes_atual(self, pagamentos: list[tuple]) -> list[int]:
        """
        Calcula a quantidade de pagamentos feitos no mês atual.
        Args:
            pagamentos (list[tuple]): Pagamentos dos professores/alunos.
        Returns:
            list[int]: A quantidade de pagamentos realizados e não realizados. Ex: [10, 5].
        """

        # Quantidade de pagamentos.
        quantidade_pagamentos = len(pagamentos)

        if quantidade_pagamentos > 0:
            pago = 0
            nao_pago = 0

            # Mês e ano atual.
            mes_ano_atual = self.DATA[3:]

            # Índice do mês.
            index_mes = 1

            for index in range(0, quantidade_pagamentos):

                # Extrai o mês e ano dos pagamentos e coloca numa lista.
                mes_ano = pagamentos[index][index_mes].split()
                if mes_ano_atual in mes_ano:
                    pago += 1
                else:
                    nao_pago += 1
            return [pago, nao_pago]

        return [0, 0]

    def buscar_dados_professores(self):
        """
        Busca os dados dos professores e atribui os resultados nas variáveis de pagamentos e dados.
        """
        # Índice da foto.
        index_foto = 13

        # Dados dos professores.
        professores = self.vgymsystem_db.get_professores()

        for professor in professores:
            # Transforma tupla em lista.
            professor = list(professor)

            # Apaga a foto da lista.
            professor.pop(index_foto)

            # Adiciona o professor na lista de professores.
            self.professores.append(professor)

        # Dados dos pagamentos.
        self.pagamentos_professores = (
            self.vgymsystem_db.get_pagamentos_professores()
        )

    def buscar_dados_alunos(self):
        """
        Busca os dados dos alunos e atribui os resultados nas variáveis de pagamentos e dados.
        """
        # Dados dos alunos.
        alunos = self.vgymsystem_db.get_alunos()

        # Índice da foto.
        index_foto = 12

        for aluno in alunos:
            # Transforma tupla em lista.
            aluno = list(aluno)

            # Apaga a foto da lista.
            aluno.pop(index_foto)

            # Adiciona o aluno na lista de alunos.
            self.alunos.append(aluno)

        # Dados dos pagamentos.
        self.pagamentos_alunos = self.vgymsystem_db.get_pagamentos_alunos()

    # Se a janela for fechada é fechado o banco de dados.
    def closeEvent(self, event):
        self.vgymsystem_db.fechar_db()
