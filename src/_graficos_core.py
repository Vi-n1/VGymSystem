# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import QEasingCurve, QPoint
from PySide6.QtCharts import (
    QChart,
    QChartView,
    QPieSlice,
    QPieSeries,
    QBarSeries,
    QBarSet,
    QBarCategoryAxis,
    QLineSeries,
    QValueAxis,
    QAbstractBarSeries,
)
from PySide6.QtGui import QPainter


class _GraficosCore:
    """
    Classe que contém a implementação dos gráficos.
    """

    def __init__(self):
        self._CORES = [
            '#4a1564',  # Magenta escuro
            '#a492ff',  # Magenta claro
            '#aaaaff',  # Azul magenta claro
            '#88c4a5',  # Verde limão
            '#ffffff',  # Branco
        ]

    def pizza(
        self,
        titulo: str,
        nome_fatia: list[str],
        valores: list[int | float],
        widget: QVBoxLayout,
    ) -> None:
        """
        Cria um gráfico de pizza/rosca e adiciona no widget informado.
        Args:
            titulo (str): Titulo do gráfico.
            nome_fatia (str): Nomes das fatias.
            valores (list): Valores das fatias.
            widget (QVBoxLayout): Instância de QVBoxLayout.
        """
        # Janela do gráfico.
        grafico = self._janela_grafico()
        grafico.setTitle(titulo)

        # Gráfico de pizza.
        pizza = QPieSeries()
        pizza.setHoleSize(0.40)

        total = sum(valores)
        for index in range(0, len(nome_fatia)):

            # Porcentagem da fatia.
            porcentagem = int((valores[index] * 100) / total)

            # Atributos únicos das fatias.
            nome = nome_fatia[index] + f': {porcentagem}%'
            pizza.append(QPieSlice(nome, valores[index]))
            pizza.slices()[index].setColor(self._CORES[index])
            pizza.slices()[index].setLabelColor(self._CORES[index])

        # Método que faz as Modificações no gráfico de pizza.
        pizza.hovered.connect(self._pizza_hover)

        # Adicionando o gráfico de pizza na janela.
        grafico.addSeries(pizza)

        # Janela de visualização do gráfico.
        visualizacao_grafico = QChartView(grafico)
        visualizacao_grafico.setRenderHint(QPainter.Antialiasing)

        # Exibição do gráfico.
        widget.addWidget(visualizacao_grafico)

    def barra(
        self,
        titulo: str,
        titulo_y: str,
        titulo_x: str,
        categoria: list[str],
        valores: list[int | float],
        widget: QVBoxLayout,
    ) -> None:
        """
        Cria um gráfico de barra/linha e adiciona no widget informado.
        Args:
            titulo (str): Titulo do gráfico.
            titulo_y (str): Titulo vertical.
            titulo_x (str): Titulo horizontal.
            categoria (str): Categorias.
            valores (str): Valores das categorias.
            widget (QVBoxLayout): Instância de QVBoxLayout.
        """
        # Janela do gráfico.
        grafico = self._janela_grafico()
        grafico.setTitle(titulo)

        # Criação da barra
        barra_set = QBarSet(titulo)
        barra_set.append(valores)
        barra_set.setColor(self._CORES[0])

        # Gráfico de barra.
        barra = QBarSeries()
        barra.append(barra_set)
        barra.setLabelsVisible(True)
        barra.setLabelsFormat('R$: @value')
        barra.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)

        # Gráfico de linha.
        linha = QLineSeries()
        linha.setName('tendência')

        # Adicionando valores no gráfico de linha.
        for index in range(0, len(valores)):
            linha.append(QPoint(index, valores[index]))

        # Adicionando os gráficos na janela.
        grafico.addSeries(linha)
        grafico.addSeries(barra)

        # Valores da horizontal.
        valor_x = QBarCategoryAxis()
        valor_x.append(categoria)
        valor_x.setTitleText(titulo_x)
        linha.attachAxis(valor_x)
        grafico.setAxisX(valor_x, barra)

        # Valores da vertical.
        valor_max = max(valores) * 2
        valor_y = QValueAxis()
        valor_y.setRange(0, valor_max)
        valor_y.setLabelFormat('%i')
        valor_y.setGridLineColor(self._CORES[2])
        valor_y.setTitleText(titulo_y)
        valor_y.setLabelsVisible(True)
        linha.attachAxis(valor_y)
        grafico.setAxisY(valor_y, barra)

        # Janela de visualização do gráfico.
        visualizacao_grafico = QChartView(grafico)
        visualizacao_grafico.setRenderHint(QPainter.Antialiasing)

        # Método que faz as Modificações no gráfico de barra.
        barra.hovered.connect(self._barra_hover)

        # Exibição do gráfico.
        widget.addWidget(visualizacao_grafico)

    @staticmethod
    def _janela_grafico() -> QChart:
        """
        Janela que gerencia os gráficos.
        Returns:
            QChart: Instância de QChart.
        """
        grafico = QChart()
        grafico.legend().setVisible(True)
        grafico.setTheme(QChart.ChartThemeDark)
        grafico.setAnimationOptions(QChart.AllAnimations)
        grafico.setAnimationEasingCurve(QEasingCurve.OutInElastic)
        grafico.setBackgroundVisible(False)
        return grafico

    def _pizza_hover(self, fatia: QPieSlice):
        """
        Transforma o gráfico de pizza em rosca e vice-versa.
        """
        fatia.setExploded(not fatia.isExploded())
        fatia.setLabelVisible(not fatia.isLabelVisible())
        if fatia.parent().holeSize() == 0:
            fatia.parent().setHoleSize(0.45)
        else:
            fatia.parent().setHoleSize(-0.45)
        if fatia.borderWidth() < 5:
            fatia.setBorderWidth(5)
            fatia.setBorderColor(self._CORES[3])
        else:
            fatia.setBorderWidth(0)
            fatia.setBorderColor(self._CORES[4])

    def _barra_hover(self, select, index, barra_set):
        """
        Altera a cor da barra selecionada.
        """
        barra_set.setBarSelected(index, select)
        barra_set.setSelectedColor(self._CORES[3])
