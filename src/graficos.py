from _graficos_core import _GraficosCore


class Graficos(_GraficosCore):
    """
    Classe que manipula os dados para a exibição de gráficos.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
