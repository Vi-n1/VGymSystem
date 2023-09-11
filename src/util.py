from datetime import datetime
from PySide6.QtWidgets import QMessageBox, QMainWindow

# Data de hoje.
DATA_HOJE = datetime.now().strftime('%d%m%y')


def exibir_mensagem(
    instancia_janela: QMainWindow, titulo: str, mensagem: str
) -> None:
    """
    Exibi uma mensagem.
    Args:
        instancia_janela (QMainWindow): Instância da janela.
        titulo (str): Título da mensagem.
        mensagem (str): Mensagem.
    """
    msg = QMessageBox(instancia_janela)
    msg.setWindowTitle(titulo)
    msg.setText(mensagem)
    msg.open()
