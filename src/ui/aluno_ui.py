# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aluno.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QCheckBox,
    QDateEdit,
    QFrame,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QStackedWidget,
    QWidget,
)
from .img_rc import *


class Ui_JanelaAluno(object):
    def setupUi(self, JanelaAluno):
        if not JanelaAluno.objectName():
            JanelaAluno.setObjectName('JanelaAluno')
        JanelaAluno.resize(1280, 720)
        JanelaAluno.setMinimumSize(QSize(1280, 720))
        JanelaAluno.setMaximumSize(QSize(1280, 720))
        icon = QIcon()
        icon.addFile(':/icon/icon/aluno.ico', QSize(), QIcon.Normal, QIcon.Off)
        JanelaAluno.setWindowIcon(icon)
        JanelaAluno.setStyleSheet(
            'QMessageBox{\n'
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.341, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}\n'
            'QMessageBox QLabel{\n'
            '	font: 900 10pt "Arial Black";\n'
            '	color: rgb(255, 255, 255);\n'
            '}'
        )
        self.centralwidget = QWidget(JanelaAluno)
        self.centralwidget.setObjectName('centralwidget')
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName('frame')
        self.frame.setGeometry(QRect(0, 0, 1280, 60))
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setMaximumSize(QSize(1280, 60))
        self.frame.setStyleSheet(
            'QFrame{\n'
            '	background-color: rgb(40, 42, 54);\n'
            '}\n'
            'QPushButton{\n'
            '	border-radius: 5%;\n'
            '	color: rgb(248, 248, 242);\n'
            '	border: 1px solid  rgb(40, 42, 54);\n'
            '	background-color: rgb(189, 147, 249);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	background-color: rgb(208, 99, 162);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border: 2px solid rgb(40, 42, 54);\n'
            '	background-color: rgb(173, 82, 135);\n'
            '}'
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pb_pagina_pagamento = QPushButton(self.frame)
        self.pb_pagina_pagamento.setObjectName('pb_pagina_pagamento')
        self.pb_pagina_pagamento.setGeometry(QRect(510, 10, 50, 50))
        self.pb_pagina_pagamento.setMinimumSize(QSize(50, 50))
        self.pb_pagina_pagamento.setMaximumSize(QSize(50, 50))
        self.pb_pagina_pagamento.setStyleSheet(
            'QPushButton{\n'
            '	border-image: url(:/cadastro/img/dinheiro.png);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	border-image: url(:/cadastro/img/dinheiro-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border-image: url(:/cadastro/img/dinheiro-press.png);\n'
            '}'
        )
        self.pb_pagina_ad_aluno = QPushButton(self.frame)
        self.pb_pagina_ad_aluno.setObjectName('pb_pagina_ad_aluno')
        self.pb_pagina_ad_aluno.setGeometry(QRect(580, 10, 50, 50))
        self.pb_pagina_ad_aluno.setMinimumSize(QSize(50, 50))
        self.pb_pagina_ad_aluno.setMaximumSize(QSize(50, 50))
        self.pb_pagina_ad_aluno.setStyleSheet(
            'QPushButton{\n'
            '	border-image: url(:/cadastro/img/ad-aluno.png);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	border-image: url(:/cadastro/img/ad-aluno-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border-image: url(:/cadastro/img/ad-aluno-press.png);\n'
            '}'
        )
        self.pb_pagina_excluir_aluno = QPushButton(self.frame)
        self.pb_pagina_excluir_aluno.setObjectName('pb_pagina_excluir_aluno')
        self.pb_pagina_excluir_aluno.setGeometry(QRect(650, 10, 50, 50))
        self.pb_pagina_excluir_aluno.setMinimumSize(QSize(50, 50))
        self.pb_pagina_excluir_aluno.setStyleSheet(
            'QPushButton{\n'
            '	border-image: url(:/cadastro/img/remove-aluno.png);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	border-image: url(:/cadastro/img/remove-aluno-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border-image: url(:/cadastro/img/remove-aluno-press.png);\n'
            '}'
        )
        self.pb_pagina_pesquisar_aluno = QPushButton(self.frame)
        self.pb_pagina_pesquisar_aluno.setObjectName(
            'pb_pagina_pesquisar_aluno'
        )
        self.pb_pagina_pesquisar_aluno.setGeometry(QRect(720, 15, 52, 47))
        self.pb_pagina_pesquisar_aluno.setMinimumSize(QSize(52, 47))
        self.pb_pagina_pesquisar_aluno.setStyleSheet(
            'QPushButton{\n'
            '	border-image: url(:/cadastro/img/procurar-aluno.png);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	border-image: url(:/cadastro/img/procurar-aluno-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border-image: url(:/cadastro/img/procurar-aluno-press.png);\n'
            '}'
        )
        self.pb_pagina_pagamento.raise_()
        self.pb_pagina_excluir_aluno.raise_()
        self.pb_pagina_pesquisar_aluno.raise_()
        self.pb_pagina_ad_aluno.raise_()
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName('frame_2')
        self.frame_2.setGeometry(QRect(0, 59, 1280, 660))
        self.frame_2.setStyleSheet(
            'QFrame{\n' '	background-color: rgb(68, 71, 90);\n' '}\n' ''
        )
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName('stackedWidget')
        self.stackedWidget.setGeometry(QRect(0, 0, 1280, 660))
        self.stackedWidget.setStyleSheet(
            'QFrame{\n'
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.341, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}\n'
            'QLabel, QCheckBox, QTableWidget{\n'
            '	font: 10pt "Arial";\n'
            '	color: rgb(80, 250, 123);\n'
            '	background-color: rgba(255, 255, 255, 0);\n'
            '}\n'
            'QPushButton{\n'
            '	border-radius: 5%;\n'
            '	color: rgb(248, 248, 242);\n'
            '	border: 1px solid  rgb(40, 42, 54);\n'
            '	background-color: rgb(189, 147, 249);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	background-color: rgb(208, 99, 162);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border: 2px solid rgb(40, 42, 54);\n'
            '	background-color: rgb(173, 82, 135);\n'
            '}\n'
            'QLineEdit, QSpinBox{\n'
            '	font: 700 10pt "Arial";\n'
            '	color: rgb(98, 114, 164);\n'
            '	border: none;\n'
            '	border-bottom: 2px solid  rgb(189, 147, 249);\n'
            '	background-color: rgba(189, 147, 249, 0.1);\n'
            '}\n'
            'QLineEdit::hover, QSpinBox::hover{\n'
            '	border-bottom: 2px solid  rgb(208, 99, 162);\n'
            '}\n'
            'QDateEdit{\n'
            '	color: rgb(98, 114, 164);\n'
            '}\n'
            'QToolTi'
            'p{\n'
            '	background-color: rgb(0, 0, 0);\n'
            '}'
        )
        self.page = QWidget()
        self.page.setObjectName('page')
        self.label_21 = QLabel(self.page)
        self.label_21.setObjectName('label_21')
        self.label_21.setGeometry(QRect(465, 20, 350, 61))
        self.label_21.setStyleSheet(
            'font: 600 italic 36pt "Sitka Small Semibold";\n'
            'color: rgb(255, 184, 108);'
        )
        self.label_21.setAlignment(Qt.AlignCenter)
        self.le_pagamentos = QLineEdit(self.page)
        self.le_pagamentos.setObjectName('le_pagamentos')
        self.le_pagamentos.setGeometry(QRect(465, 90, 351, 22))
        self.le_pagamentos.setAlignment(Qt.AlignCenter)
        self.pb_pg_pagamentos_pesquisar = QPushButton(self.page)
        self.pb_pg_pagamentos_pesquisar.setObjectName(
            'pb_pg_pagamentos_pesquisar'
        )
        self.pb_pg_pagamentos_pesquisar.setGeometry(QRect(790, 90, 21, 16))
        self.pb_pg_pagamentos_pesquisar.setStyleSheet(
            'background-color: rgba(255, 255, 255, 0);\n'
            'border-image: url(:/cadastro/img/lupa.png);'
        )
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName('frame_3')
        self.frame_3.setGeometry(QRect(460, 130, 361, 521))
        self.frame_3.setStyleSheet(
            'QFrame{\n'
            'background-color: rgb(53, 58, 75);\n'
            'border-radius: 30px;\n'
            '}\n'
            'QFrame::hover{\n'
            '	border: 1px solid  rgb(173, 82, 135);\n'
            '	color: rgb(189, 147, 249);\n'
            '}\n'
            'QLabel{\n'
            '	color: rgb(80, 250, 123);\n'
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.42, x2:0, y2:1, stop:0 rgba(53, 58, 75, 255), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}'
        )
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.l_pg_pagamentos_nome = QLabel(self.frame_3)
        self.l_pg_pagamentos_nome.setObjectName('l_pg_pagamentos_nome')
        self.l_pg_pagamentos_nome.setGeometry(QRect(1, 200, 131, 20))
        font = QFont()
        font.setFamilies(['Arial'])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.l_pg_pagamentos_nome.setFont(font)
        self.l_pg_pagamentos_nome.setStyleSheet('')
        self.l_pg_pagamentos_nome.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_foto = QLabel(self.frame_3)
        self.l_pg_pagamentos_foto.setObjectName('l_pg_pagamentos_foto')
        self.l_pg_pagamentos_foto.setGeometry(QRect(111, 20, 140, 140))
        self.l_pg_pagamentos_foto.setStyleSheet(
            'background-color: rgb(255, 255, 255);'
        )
        self.l_pg_pagamentos_foto.setScaledContents(True)
        self.l_pg_pagamentos_matricula = QLabel(self.frame_3)
        self.l_pg_pagamentos_matricula.setObjectName(
            'l_pg_pagamentos_matricula'
        )
        self.l_pg_pagamentos_matricula.setGeometry(QRect(115, 170, 131, 20))
        self.l_pg_pagamentos_matricula.setStyleSheet('')
        self.l_pg_pagamentos_matricula.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_matricula.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse
        )
        self.l_pg_pagamentos_data_nascimento = QLabel(self.frame_3)
        self.l_pg_pagamentos_data_nascimento.setObjectName(
            'l_pg_pagamentos_data_nascimento'
        )
        self.l_pg_pagamentos_data_nascimento.setGeometry(
            QRect(135, 200, 131, 20)
        )
        self.l_pg_pagamentos_data_nascimento.setStyleSheet('')
        self.l_pg_pagamentos_data_nascimento.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_cpf = QLabel(self.frame_3)
        self.l_pg_pagamentos_cpf.setObjectName('l_pg_pagamentos_cpf')
        self.l_pg_pagamentos_cpf.setGeometry(QRect(270, 200, 81, 20))
        self.l_pg_pagamentos_cpf.setStyleSheet('')
        self.l_pg_pagamentos_cpf.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_celular = QLabel(self.frame_3)
        self.l_pg_pagamentos_celular.setObjectName('l_pg_pagamentos_celular')
        self.l_pg_pagamentos_celular.setGeometry(QRect(1, 240, 131, 20))
        self.l_pg_pagamentos_celular.setStyleSheet('')
        self.l_pg_pagamentos_celular.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_email = QLabel(self.frame_3)
        self.l_pg_pagamentos_email.setObjectName('l_pg_pagamentos_email')
        self.l_pg_pagamentos_email.setGeometry(QRect(135, 240, 216, 20))
        self.l_pg_pagamentos_email.setStyleSheet('')
        self.l_pg_pagamentos_email.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_cidade = QLabel(self.frame_3)
        self.l_pg_pagamentos_cidade.setObjectName('l_pg_pagamentos_cidade')
        self.l_pg_pagamentos_cidade.setGeometry(QRect(1, 280, 131, 20))
        self.l_pg_pagamentos_cidade.setStyleSheet('')
        self.l_pg_pagamentos_cidade.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_bairro = QLabel(self.frame_3)
        self.l_pg_pagamentos_bairro.setObjectName('l_pg_pagamentos_bairro')
        self.l_pg_pagamentos_bairro.setGeometry(QRect(135, 280, 131, 20))
        self.l_pg_pagamentos_bairro.setStyleSheet('')
        self.l_pg_pagamentos_bairro.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_cep = QLabel(self.frame_3)
        self.l_pg_pagamentos_cep.setObjectName('l_pg_pagamentos_cep')
        self.l_pg_pagamentos_cep.setGeometry(QRect(270, 280, 81, 20))
        self.l_pg_pagamentos_cep.setStyleSheet('')
        self.l_pg_pagamentos_cep.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_data_pagamento = QLabel(self.frame_3)
        self.l_pg_pagamentos_data_pagamento.setObjectName(
            'l_pg_pagamentos_data_pagamento'
        )
        self.l_pg_pagamentos_data_pagamento.setGeometry(QRect(1, 320, 181, 20))
        self.l_pg_pagamentos_data_pagamento.setStyleSheet('')
        self.l_pg_pagamentos_data_pagamento.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_data_pagamento.setIndent(-1)
        self.l_pg_pagamentos_valor = QLabel(self.frame_3)
        self.l_pg_pagamentos_valor.setObjectName('l_pg_pagamentos_valor')
        self.l_pg_pagamentos_valor.setGeometry(QRect(190, 320, 161, 20))
        self.l_pg_pagamentos_valor.setStyleSheet('')
        self.l_pg_pagamentos_valor.setAlignment(Qt.AlignCenter)
        self.l_pg_pagamentos_responsavel = QLabel(self.frame_3)
        self.l_pg_pagamentos_responsavel.setObjectName(
            'l_pg_pagamentos_responsavel'
        )
        self.l_pg_pagamentos_responsavel.setGeometry(QRect(114, 370, 131, 20))
        self.l_pg_pagamentos_responsavel.setStyleSheet('')
        self.l_pg_pagamentos_responsavel.setAlignment(Qt.AlignCenter)
        self.pb_pagar_pix = QPushButton(self.frame_3)
        self.pb_pagar_pix.setObjectName('pb_pagar_pix')
        self.pb_pagar_pix.setGeometry(QRect(190, 460, 101, 24))
        icon1 = QIcon()
        icon1.addFile(':/grobal/img/pix.png', QSize(), QIcon.Normal, QIcon.Off)
        self.pb_pagar_pix.setIcon(icon1)
        self.pb_imprimir_boleto = QPushButton(self.frame_3)
        self.pb_imprimir_boleto.setObjectName('pb_imprimir_boleto')
        self.pb_imprimir_boleto.setGeometry(QRect(70, 460, 111, 24))
        icon2 = QIcon()
        icon2.addFile(
            ':/grobal/img/imprimir.png', QSize(), QIcon.Normal, QIcon.Off
        )
        self.pb_imprimir_boleto.setIcon(icon2)
        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName('label_24')
        self.label_24.setGeometry(QRect(0, 130, 111, 4))
        self.label_24.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName('label_25')
        self.label_25.setGeometry(QRect(250, 50, 111, 4))
        self.label_25.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_24.raise_()
        self.label_25.raise_()
        self.l_pg_pagamentos_nome.raise_()
        self.l_pg_pagamentos_foto.raise_()
        self.l_pg_pagamentos_matricula.raise_()
        self.l_pg_pagamentos_data_nascimento.raise_()
        self.l_pg_pagamentos_cpf.raise_()
        self.l_pg_pagamentos_celular.raise_()
        self.l_pg_pagamentos_email.raise_()
        self.l_pg_pagamentos_cidade.raise_()
        self.l_pg_pagamentos_bairro.raise_()
        self.l_pg_pagamentos_cep.raise_()
        self.l_pg_pagamentos_data_pagamento.raise_()
        self.l_pg_pagamentos_valor.raise_()
        self.l_pg_pagamentos_responsavel.raise_()
        self.pb_pagar_pix.raise_()
        self.pb_imprimir_boleto.raise_()
        self.label_34 = QLabel(self.page)
        self.label_34.setObjectName('label_34')
        self.label_34.setGeometry(QRect(710, 220, 111, 4))
        self.label_34.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_35 = QLabel(self.page)
        self.label_35.setObjectName('label_35')
        self.label_35.setGeometry(QRect(820, 610, 261, 16))
        self.label_35.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_36 = QLabel(self.page)
        self.label_36.setObjectName('label_36')
        self.label_36.setGeometry(QRect(900, 640, 381, 16))
        self.label_36.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_37 = QLabel(self.page)
        self.label_37.setObjectName('label_37')
        self.label_37.setGeometry(QRect(920, 590, 361, 16))
        self.label_37.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_38 = QLabel(self.page)
        self.label_38.setObjectName('label_38')
        self.label_38.setGeometry(QRect(820, 570, 381, 16))
        self.label_38.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_39 = QLabel(self.page)
        self.label_39.setObjectName('label_39')
        self.label_39.setGeometry(QRect(980, 540, 301, 16))
        self.label_39.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_40 = QLabel(self.page)
        self.label_40.setObjectName('label_40')
        self.label_40.setGeometry(QRect(0, 40, 381, 16))
        self.label_40.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_41 = QLabel(self.page)
        self.label_41.setObjectName('label_41')
        self.label_41.setGeometry(QRect(160, 20, 311, 16))
        self.label_41.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_43 = QLabel(self.page)
        self.label_43.setObjectName('label_43')
        self.label_43.setGeometry(QRect(0, 80, 261, 16))
        self.label_43.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_44 = QLabel(self.page)
        self.label_44.setObjectName('label_44')
        self.label_44.setGeometry(QRect(55, 60, 411, 16))
        self.label_44.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.stackedWidget.addWidget(self.page)
        self.label_36.raise_()
        self.label_35.raise_()
        self.label_38.raise_()
        self.label_44.raise_()
        self.label_41.raise_()
        self.label_21.raise_()
        self.le_pagamentos.raise_()
        self.pb_pg_pagamentos_pesquisar.raise_()
        self.frame_3.raise_()
        self.label_34.raise_()
        self.label_37.raise_()
        self.label_39.raise_()
        self.label_40.raise_()
        self.label_43.raise_()
        self.page1 = QWidget()
        self.page1.setObjectName('page1')
        self.label = QLabel(self.page1)
        self.label.setObjectName('label')
        self.label.setGeometry(QRect(1, 40, 271, 20))
        self.label.setAlignment(Qt.AlignCenter)
        self.le_nome_aluno = QLineEdit(self.page1)
        self.le_nome_aluno.setObjectName('le_nome_aluno')
        self.le_nome_aluno.setGeometry(QRect(1, 60, 271, 22))
        self.le_nome_aluno.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.page1)
        self.label_2.setObjectName('label_2')
        self.label_2.setGeometry(QRect(300, 40, 151, 20))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.de_data_nascimento = QDateEdit(self.page1)
        self.de_data_nascimento.setObjectName('de_data_nascimento')
        self.de_data_nascimento.setGeometry(QRect(300, 60, 151, 22))
        self.de_data_nascimento.setAlignment(Qt.AlignCenter)
        self.de_data_nascimento.setMaximumDate(QDate(2013, 12, 30))
        self.de_data_nascimento.setMinimumDate(QDate(1900, 1, 1))
        self.de_data_nascimento.setCalendarPopup(True)
        self.label_3 = QLabel(self.page1)
        self.label_3.setObjectName('label_3')
        self.label_3.setGeometry(QRect(480, 40, 131, 20))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.le_cpf_aluno = QLineEdit(self.page1)
        self.le_cpf_aluno.setObjectName('le_cpf_aluno')
        self.le_cpf_aluno.setGeometry(QRect(480, 60, 131, 22))
        self.le_cpf_aluno.setMaxLength(14)
        self.le_cpf_aluno.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.page1)
        self.label_4.setObjectName('label_4')
        self.label_4.setGeometry(QRect(640, 40, 171, 20))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.le_celular_aluno = QLineEdit(self.page1)
        self.le_celular_aluno.setObjectName('le_celular_aluno')
        self.le_celular_aluno.setGeometry(QRect(640, 60, 171, 22))
        self.le_celular_aluno.setText('()-')
        self.le_celular_aluno.setFrame(True)
        self.le_celular_aluno.setEchoMode(QLineEdit.Normal)
        self.le_celular_aluno.setCursorPosition(14)
        self.le_celular_aluno.setAlignment(Qt.AlignCenter)
        self.cb_whatsapp_aluno = QCheckBox(self.page1)
        self.cb_whatsapp_aluno.setObjectName('cb_whatsapp_aluno')
        self.cb_whatsapp_aluno.setGeometry(QRect(830, 66, 81, 20))
        self.cb_responsavel = QCheckBox(self.page1)
        self.cb_responsavel.setObjectName('cb_responsavel')
        self.cb_responsavel.setGeometry(QRect(830, 46, 91, 20))
        self.pb_ad_foto_aluno = QPushButton(self.page1)
        self.pb_ad_foto_aluno.setObjectName('pb_ad_foto_aluno')
        self.pb_ad_foto_aluno.setGeometry(QRect(940, 20, 271, 211))
        self.pb_ad_foto_aluno.setStyleSheet(
            'QPushButton{\n'
            '	border-radius: 5%;\n'
            '	border: 2px solid  rgb(208, 99, 162);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            ''
        )
        self.l_foto_aluno = QLabel(self.page1)
        self.l_foto_aluno.setObjectName('l_foto_aluno')
        self.l_foto_aluno.setGeometry(QRect(940, 20, 271, 211))
        self.l_foto_aluno.setScaledContents(True)
        self.label_7 = QLabel(self.page1)
        self.label_7.setObjectName('label_7')
        self.label_7.setGeometry(QRect(1, 110, 151, 20))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.le_bairro_aluno = QLineEdit(self.page1)
        self.le_bairro_aluno.setObjectName('le_bairro_aluno')
        self.le_bairro_aluno.setGeometry(QRect(1, 130, 151, 22))
        self.le_bairro_aluno.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.page1)
        self.label_8.setObjectName('label_8')
        self.label_8.setGeometry(QRect(180, 110, 131, 20))
        self.label_8.setAlignment(Qt.AlignCenter)
        self.le_cep_aluno = QLineEdit(self.page1)
        self.le_cep_aluno.setObjectName('le_cep_aluno')
        self.le_cep_aluno.setGeometry(QRect(180, 130, 131, 22))
        self.le_cep_aluno.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.page1)
        self.label_9.setObjectName('label_9')
        self.label_9.setGeometry(QRect(340, 110, 171, 20))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.le_cidade_aluno = QLineEdit(self.page1)
        self.le_cidade_aluno.setObjectName('le_cidade_aluno')
        self.le_cidade_aluno.setGeometry(QRect(340, 130, 171, 22))
        self.le_cidade_aluno.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.page1)
        self.label_10.setObjectName('label_10')
        self.label_10.setGeometry(QRect(540, 110, 271, 20))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.le_email_aluno = QLineEdit(self.page1)
        self.le_email_aluno.setObjectName('le_email_aluno')
        self.le_email_aluno.setGeometry(QRect(540, 130, 271, 22))
        self.le_email_aluno.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.page1)
        self.groupBox.setObjectName('groupBox')
        self.groupBox.setGeometry(QRect(0, 240, 1280, 422))
        font1 = QFont()
        font1.setFamilies(['Arial'])
        font1.setPointSize(10)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(
            'QGroupBox::title {\n'
            '	color: rgb(255, 255, 255);\n'
            '    subcontrol-origin: margin;\n'
            '    subcontrol-position: top center;\n'
            '	border-radius: 5px;\n'
            '}'
        )
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName('label_11')
        self.label_11.setGeometry(QRect(1, 90, 271, 20))
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName('label_12')
        self.label_12.setGeometry(QRect(300, 90, 151, 20))
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName('label_13')
        self.label_13.setGeometry(QRect(480, 90, 131, 20))
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName('label_14')
        self.label_14.setGeometry(QRect(640, 90, 171, 20))
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName('label_16')
        self.label_16.setGeometry(QRect(1, 160, 151, 20))
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName('label_17')
        self.label_17.setGeometry(QRect(180, 160, 131, 20))
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName('label_18')
        self.label_18.setGeometry(QRect(340, 160, 171, 20))
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName('label_19')
        self.label_19.setGeometry(QRect(540, 160, 271, 20))
        self.label_19.setAlignment(Qt.AlignCenter)
        self.l_foto_responsavel = QLabel(self.groupBox)
        self.l_foto_responsavel.setObjectName('l_foto_responsavel')
        self.l_foto_responsavel.setGeometry(QRect(940, 20, 271, 211))
        self.l_foto_responsavel.setScaledContents(True)
        self.pb_ad_foto_responsavel = QPushButton(self.groupBox)
        self.pb_ad_foto_responsavel.setObjectName('pb_ad_foto_responsavel')
        self.pb_ad_foto_responsavel.setEnabled(True)
        self.pb_ad_foto_responsavel.setGeometry(QRect(940, 20, 271, 211))
        self.pb_ad_foto_responsavel.setStyleSheet(
            'QPushButton{\n'
            '	border-radius: 5%;\n'
            '	border: 2px solid  rgb(208, 99, 162);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            ''
        )
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName('label_15')
        self.label_15.setGeometry(QRect(1020, 6, 111, 16))
        self.le_nome_responsavel = QLineEdit(self.groupBox)
        self.le_nome_responsavel.setObjectName('le_nome_responsavel')
        self.le_nome_responsavel.setGeometry(QRect(1, 110, 271, 22))
        self.le_nome_responsavel.setAlignment(Qt.AlignCenter)
        self.de_data_nascimento_responsavel = QDateEdit(self.groupBox)
        self.de_data_nascimento_responsavel.setObjectName(
            'de_data_nascimento_responsavel'
        )
        self.de_data_nascimento_responsavel.setGeometry(
            QRect(300, 110, 151, 22)
        )
        self.de_data_nascimento_responsavel.setAlignment(Qt.AlignCenter)
        self.de_data_nascimento_responsavel.setAccelerated(False)
        self.de_data_nascimento_responsavel.setMaximumDate(QDate(2013, 12, 30))
        self.de_data_nascimento_responsavel.setMinimumDate(QDate(1900, 1, 1))
        self.de_data_nascimento_responsavel.setCalendarPopup(True)
        self.le_cpf_responsavel = QLineEdit(self.groupBox)
        self.le_cpf_responsavel.setObjectName('le_cpf_responsavel')
        self.le_cpf_responsavel.setGeometry(QRect(480, 110, 131, 22))
        self.le_cpf_responsavel.setAlignment(Qt.AlignCenter)
        self.le_celular_responsavel = QLineEdit(self.groupBox)
        self.le_celular_responsavel.setObjectName('le_celular_responsavel')
        self.le_celular_responsavel.setGeometry(QRect(640, 110, 171, 22))
        self.le_celular_responsavel.setAlignment(Qt.AlignCenter)
        self.le_bairro_responsavel = QLineEdit(self.groupBox)
        self.le_bairro_responsavel.setObjectName('le_bairro_responsavel')
        self.le_bairro_responsavel.setGeometry(QRect(1, 180, 151, 22))
        self.le_bairro_responsavel.setAlignment(Qt.AlignCenter)
        self.le_cep_responsavel = QLineEdit(self.groupBox)
        self.le_cep_responsavel.setObjectName('le_cep_responsavel')
        self.le_cep_responsavel.setGeometry(QRect(180, 180, 131, 22))
        self.le_cep_responsavel.setAlignment(Qt.AlignCenter)
        self.le_cidade_responsavel = QLineEdit(self.groupBox)
        self.le_cidade_responsavel.setObjectName('le_cidade_responsavel')
        self.le_cidade_responsavel.setGeometry(QRect(340, 180, 171, 22))
        self.le_cidade_responsavel.setAlignment(Qt.AlignCenter)
        self.le_email_responsavel = QLineEdit(self.groupBox)
        self.le_email_responsavel.setObjectName('le_email_responsavel')
        self.le_email_responsavel.setGeometry(QRect(540, 180, 271, 22))
        self.le_email_responsavel.setAlignment(Qt.AlignCenter)
        self.pb_salvar_dados = QPushButton(self.groupBox)
        self.pb_salvar_dados.setObjectName('pb_salvar_dados')
        self.pb_salvar_dados.setGeometry(QRect(602, 340, 75, 24))
        font2 = QFont()
        font2.setFamilies(['Arial'])
        font2.setPointSize(10)
        self.pb_salvar_dados.setFont(font2)
        self.label_62 = QLabel(self.groupBox)
        self.label_62.setObjectName('label_62')
        self.label_62.setGeometry(QRect(10, 280, 16, 141))
        self.label_62.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_63 = QLabel(self.groupBox)
        self.label_63.setObjectName('label_63')
        self.label_63.setGeometry(QRect(50, 370, 10, 51))
        self.label_63.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_64 = QLabel(self.groupBox)
        self.label_64.setObjectName('label_64')
        self.label_64.setGeometry(QRect(120, 300, 10, 120))
        self.label_64.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_65 = QLabel(self.groupBox)
        self.label_65.setObjectName('label_65')
        self.label_65.setGeometry(QRect(390, 366, 20, 61))
        self.label_65.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_66 = QLabel(self.groupBox)
        self.label_66.setObjectName('label_66')
        self.label_66.setGeometry(QRect(130, 240, 10, 120))
        self.label_66.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_67 = QLabel(self.groupBox)
        self.label_67.setObjectName('label_67')
        self.label_67.setGeometry(QRect(395, 250, 10, 120))
        self.label_67.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_68 = QLabel(self.groupBox)
        self.label_68.setObjectName('label_68')
        self.label_68.setGeometry(QRect(770, 300, 10, 120))
        self.label_68.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_69 = QLabel(self.groupBox)
        self.label_69.setObjectName('label_69')
        self.label_69.setGeometry(QRect(780, 270, 10, 50))
        self.label_69.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_70 = QLabel(self.groupBox)
        self.label_70.setObjectName('label_70')
        self.label_70.setGeometry(QRect(790, 300, 10, 50))
        self.label_70.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_71 = QLabel(self.groupBox)
        self.label_71.setObjectName('label_71')
        self.label_71.setGeometry(QRect(800, 240, 10, 70))
        self.label_71.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_72 = QLabel(self.groupBox)
        self.label_72.setObjectName('label_72')
        self.label_72.setGeometry(QRect(920, 370, 10, 50))
        self.label_72.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_73 = QLabel(self.groupBox)
        self.label_73.setObjectName('label_73')
        self.label_73.setGeometry(QRect(930, 330, 10, 50))
        self.label_73.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_74 = QLabel(self.groupBox)
        self.label_74.setObjectName('label_74')
        self.label_74.setGeometry(QRect(920, 300, 10, 50))
        self.label_74.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_75 = QLabel(self.groupBox)
        self.label_75.setObjectName('label_75')
        self.label_75.setGeometry(QRect(850, 370, 10, 50))
        self.label_75.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_76 = QLabel(self.groupBox)
        self.label_76.setObjectName('label_76')
        self.label_76.setGeometry(QRect(860, 350, 10, 50))
        self.label_76.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_77 = QLabel(self.groupBox)
        self.label_77.setObjectName('label_77')
        self.label_77.setGeometry(QRect(870, 320, 10, 50))
        self.label_77.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_78 = QLabel(self.groupBox)
        self.label_78.setObjectName('label_78')
        self.label_78.setGeometry(QRect(860, 280, 10, 50))
        self.label_78.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_79 = QLabel(self.groupBox)
        self.label_79.setObjectName('label_79')
        self.label_79.setGeometry(QRect(880, 300, 10, 50))
        self.label_79.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_80 = QLabel(self.groupBox)
        self.label_80.setObjectName('label_80')
        self.label_80.setGeometry(QRect(1250, 220, 10, 200))
        self.label_80.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_81 = QLabel(self.groupBox)
        self.label_81.setObjectName('label_81')
        self.label_81.setGeometry(QRect(1180, 230, 10, 50))
        self.label_81.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_82 = QLabel(self.groupBox)
        self.label_82.setObjectName('label_82')
        self.label_82.setGeometry(QRect(1190, 270, 10, 50))
        self.label_82.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_83 = QLabel(self.groupBox)
        self.label_83.setObjectName('label_83')
        self.label_83.setGeometry(QRect(1090, 230, 10, 50))
        self.label_83.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_84 = QLabel(self.groupBox)
        self.label_84.setObjectName('label_84')
        self.label_84.setGeometry(QRect(1110, 230, 10, 30))
        self.label_84.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_85 = QLabel(self.groupBox)
        self.label_85.setObjectName('label_85')
        self.label_85.setGeometry(QRect(1010, 230, 10, 50))
        self.label_85.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_86 = QLabel(self.groupBox)
        self.label_86.setObjectName('label_86')
        self.label_86.setGeometry(QRect(1020, 270, 10, 50))
        self.label_86.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_87 = QLabel(self.groupBox)
        self.label_87.setObjectName('label_87')
        self.label_87.setGeometry(QRect(1030, 290, 10, 50))
        self.label_87.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_88 = QLabel(self.groupBox)
        self.label_88.setObjectName('label_88')
        self.label_88.setGeometry(QRect(1040, 310, 10, 50))
        self.label_88.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_89 = QLabel(self.groupBox)
        self.label_89.setObjectName('label_89')
        self.label_89.setGeometry(QRect(1030, 350, 10, 50))
        self.label_89.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_90 = QLabel(self.groupBox)
        self.label_90.setObjectName('label_90')
        self.label_90.setGeometry(QRect(390, 280, 10, 50))
        self.label_90.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_91 = QLabel(self.groupBox)
        self.label_91.setObjectName('label_91')
        self.label_91.setGeometry(QRect(140, 290, 10, 50))
        self.label_91.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_92 = QLabel(self.groupBox)
        self.label_92.setObjectName('label_92')
        self.label_92.setGeometry(QRect(270, 370, 10, 50))
        self.label_92.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_93 = QLabel(self.groupBox)
        self.label_93.setObjectName('label_93')
        self.label_93.setGeometry(QRect(230, 200, 10, 50))
        self.label_93.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_94 = QLabel(self.groupBox)
        self.label_94.setObjectName('label_94')
        self.label_94.setGeometry(QRect(610, 290, 10, 50))
        self.label_94.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_95 = QLabel(self.groupBox)
        self.label_95.setObjectName('label_95')
        self.label_95.setGeometry(QRect(620, 360, 10, 50))
        self.label_95.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_96 = QLabel(self.groupBox)
        self.label_96.setObjectName('label_96')
        self.label_96.setGeometry(QRect(690, 200, 21, 50))
        self.label_96.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_97 = QLabel(self.groupBox)
        self.label_97.setObjectName('label_97')
        self.label_97.setGeometry(QRect(696, 250, 10, 50))
        self.label_97.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_90.raise_()
        self.label_96.raise_()
        self.label_95.raise_()
        self.label_94.raise_()
        self.label_93.raise_()
        self.label_65.raise_()
        self.l_foto_responsavel.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.pb_ad_foto_responsavel.raise_()
        self.label_15.raise_()
        self.le_nome_responsavel.raise_()
        self.de_data_nascimento_responsavel.raise_()
        self.le_cpf_responsavel.raise_()
        self.le_celular_responsavel.raise_()
        self.le_bairro_responsavel.raise_()
        self.le_cep_responsavel.raise_()
        self.le_cidade_responsavel.raise_()
        self.le_email_responsavel.raise_()
        self.pb_salvar_dados.raise_()
        self.label_62.raise_()
        self.label_63.raise_()
        self.label_64.raise_()
        self.label_66.raise_()
        self.label_67.raise_()
        self.label_68.raise_()
        self.label_69.raise_()
        self.label_70.raise_()
        self.label_71.raise_()
        self.label_72.raise_()
        self.label_73.raise_()
        self.label_74.raise_()
        self.label_75.raise_()
        self.label_76.raise_()
        self.label_77.raise_()
        self.label_78.raise_()
        self.label_79.raise_()
        self.label_80.raise_()
        self.label_81.raise_()
        self.label_82.raise_()
        self.label_83.raise_()
        self.label_84.raise_()
        self.label_85.raise_()
        self.label_86.raise_()
        self.label_87.raise_()
        self.label_88.raise_()
        self.label_89.raise_()
        self.label_91.raise_()
        self.label_92.raise_()
        self.label_97.raise_()
        self.label_6 = QLabel(self.page1)
        self.label_6.setObjectName('label_6')
        self.label_6.setGeometry(QRect(1020, 0, 111, 20))
        self.label_22 = QLabel(self.page1)
        self.label_22.setObjectName('label_22')
        self.label_22.setGeometry(QRect(1, 180, 151, 20))
        self.label_22.setAlignment(Qt.AlignCenter)
        self.sb_data_pagamento = QSpinBox(self.page1)
        self.sb_data_pagamento.setObjectName('sb_data_pagamento')
        self.sb_data_pagamento.setGeometry(QRect(1, 200, 151, 22))
        self.sb_data_pagamento.setAlignment(Qt.AlignCenter)
        self.sb_data_pagamento.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_data_pagamento.setMinimum(1)
        self.sb_data_pagamento.setMaximum(30)
        self.label_23 = QLabel(self.page1)
        self.label_23.setObjectName('label_23')
        self.label_23.setGeometry(QRect(190, 180, 121, 20))
        self.label_23.setAlignment(Qt.AlignCenter)
        self.sb_valor_pagamento = QSpinBox(self.page1)
        self.sb_valor_pagamento.setObjectName('sb_valor_pagamento')
        self.sb_valor_pagamento.setGeometry(QRect(190, 200, 121, 22))
        self.sb_valor_pagamento.setAlignment(Qt.AlignCenter)
        self.sb_valor_pagamento.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_valor_pagamento.setMaximum(9999999)
        self.label_98 = QLabel(self.page1)
        self.label_98.setObjectName('label_98')
        self.label_98.setGeometry(QRect(1210, 90, 10, 50))
        self.label_98.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_99 = QLabel(self.page1)
        self.label_99.setObjectName('label_99')
        self.label_99.setGeometry(QRect(930, 150, 10, 50))
        self.label_99.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_100 = QLabel(self.page1)
        self.label_100.setObjectName('label_100')
        self.label_100.setGeometry(QRect(930, 30, 10, 50))
        self.label_100.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_101 = QLabel(self.page1)
        self.label_101.setObjectName('label_101')
        self.label_101.setGeometry(QRect(1210, 250, 10, 50))
        self.label_101.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_102 = QLabel(self.page1)
        self.label_102.setObjectName('label_102')
        self.label_102.setGeometry(QRect(930, 390, 10, 50))
        self.label_102.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.stackedWidget.addWidget(self.page1)
        self.label_99.raise_()
        self.label_98.raise_()
        self.label_101.raise_()
        self.label_102.raise_()
        self.label_100.raise_()
        self.label.raise_()
        self.le_nome_aluno.raise_()
        self.label_2.raise_()
        self.de_data_nascimento.raise_()
        self.label_3.raise_()
        self.le_cpf_aluno.raise_()
        self.label_4.raise_()
        self.le_celular_aluno.raise_()
        self.cb_whatsapp_aluno.raise_()
        self.cb_responsavel.raise_()
        self.l_foto_aluno.raise_()
        self.pb_ad_foto_aluno.raise_()
        self.label_7.raise_()
        self.le_bairro_aluno.raise_()
        self.label_8.raise_()
        self.le_cep_aluno.raise_()
        self.label_9.raise_()
        self.le_cidade_aluno.raise_()
        self.label_10.raise_()
        self.le_email_aluno.raise_()
        self.groupBox.raise_()
        self.label_6.raise_()
        self.label_22.raise_()
        self.sb_data_pagamento.raise_()
        self.label_23.raise_()
        self.sb_valor_pagamento.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName('page_3')
        self.label_20 = QLabel(self.page_3)
        self.label_20.setObjectName('label_20')
        self.label_20.setGeometry(QRect(465, 20, 350, 61))
        self.label_20.setStyleSheet(
            'font: 600 italic 36pt "Sitka Small Semibold";\n'
            'color: rgb(255, 184, 108);'
        )
        self.label_20.setAlignment(Qt.AlignCenter)
        self.le_excluir_aluno = QLineEdit(self.page_3)
        self.le_excluir_aluno.setObjectName('le_excluir_aluno')
        self.le_excluir_aluno.setGeometry(QRect(466, 90, 351, 22))
        self.le_excluir_aluno.setAlignment(Qt.AlignCenter)
        self.pb_pg_excluir_pesquisar = QPushButton(self.page_3)
        self.pb_pg_excluir_pesquisar.setObjectName('pb_pg_excluir_pesquisar')
        self.pb_pg_excluir_pesquisar.setGeometry(QRect(790, 90, 21, 16))
        self.pb_pg_excluir_pesquisar.setStyleSheet(
            'background-color: rgba(255, 255, 255, 0);\n'
            'border-image: url(:/cadastro/img/lupa.png);'
        )
        self.frame_5 = QFrame(self.page_3)
        self.frame_5.setObjectName('frame_5')
        self.frame_5.setGeometry(QRect(460, 130, 361, 521))
        self.frame_5.setStyleSheet(
            'QFrame{\n'
            'background-color: rgb(53, 58, 75);\n'
            'border-radius: 30px;\n'
            '}\n'
            'QFrame::hover{\n'
            '	border: 1px solid  rgb(173, 82, 135);\n'
            '	color: rgb(189, 147, 249);\n'
            '}\n'
            'QLabel{\n'
            '	color: rgb(80, 250, 123);\n'
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.42, x2:0, y2:1, stop:0 rgba(53, 58, 75, 255), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}\n'
            'Line{\n'
            '	background-color: rgb(173, 82, 135);\n'
            '}'
        )
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.l_pg_excluir_nome = QLabel(self.frame_5)
        self.l_pg_excluir_nome.setObjectName('l_pg_excluir_nome')
        self.l_pg_excluir_nome.setGeometry(QRect(1, 200, 131, 20))
        self.l_pg_excluir_nome.setFont(font)
        self.l_pg_excluir_nome.setStyleSheet('')
        self.l_pg_excluir_nome.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_foto = QLabel(self.frame_5)
        self.l_pg_excluir_foto.setObjectName('l_pg_excluir_foto')
        self.l_pg_excluir_foto.setGeometry(QRect(111, 20, 140, 140))
        self.l_pg_excluir_foto.setStyleSheet(
            'background-color: rgb(255, 255, 255);'
        )
        self.l_pg_excluir_foto.setScaledContents(True)
        self.l_pg_excluir_matricula = QLabel(self.frame_5)
        self.l_pg_excluir_matricula.setObjectName('l_pg_excluir_matricula')
        self.l_pg_excluir_matricula.setGeometry(QRect(115, 170, 131, 20))
        self.l_pg_excluir_matricula.setStyleSheet('')
        self.l_pg_excluir_matricula.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_matricula.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse
        )
        self.l_pg_excluir_data_nascimento = QLabel(self.frame_5)
        self.l_pg_excluir_data_nascimento.setObjectName(
            'l_pg_excluir_data_nascimento'
        )
        self.l_pg_excluir_data_nascimento.setGeometry(QRect(135, 200, 131, 20))
        self.l_pg_excluir_data_nascimento.setStyleSheet('')
        self.l_pg_excluir_data_nascimento.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_cpf = QLabel(self.frame_5)
        self.l_pg_excluir_cpf.setObjectName('l_pg_excluir_cpf')
        self.l_pg_excluir_cpf.setGeometry(QRect(270, 200, 81, 20))
        self.l_pg_excluir_cpf.setStyleSheet('')
        self.l_pg_excluir_cpf.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_celular = QLabel(self.frame_5)
        self.l_pg_excluir_celular.setObjectName('l_pg_excluir_celular')
        self.l_pg_excluir_celular.setGeometry(QRect(1, 240, 131, 20))
        self.l_pg_excluir_celular.setStyleSheet('')
        self.l_pg_excluir_celular.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_email = QLabel(self.frame_5)
        self.l_pg_excluir_email.setObjectName('l_pg_excluir_email')
        self.l_pg_excluir_email.setGeometry(QRect(135, 240, 216, 20))
        self.l_pg_excluir_email.setStyleSheet('')
        self.l_pg_excluir_email.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_cidade = QLabel(self.frame_5)
        self.l_pg_excluir_cidade.setObjectName('l_pg_excluir_cidade')
        self.l_pg_excluir_cidade.setGeometry(QRect(1, 280, 131, 20))
        self.l_pg_excluir_cidade.setStyleSheet('')
        self.l_pg_excluir_cidade.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_bairro = QLabel(self.frame_5)
        self.l_pg_excluir_bairro.setObjectName('l_pg_excluir_bairro')
        self.l_pg_excluir_bairro.setGeometry(QRect(135, 280, 131, 20))
        self.l_pg_excluir_bairro.setStyleSheet('')
        self.l_pg_excluir_bairro.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_cep = QLabel(self.frame_5)
        self.l_pg_excluir_cep.setObjectName('l_pg_excluir_cep')
        self.l_pg_excluir_cep.setGeometry(QRect(270, 280, 81, 20))
        self.l_pg_excluir_cep.setStyleSheet('')
        self.l_pg_excluir_cep.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_data_pagamento = QLabel(self.frame_5)
        self.l_pg_excluir_data_pagamento.setObjectName(
            'l_pg_excluir_data_pagamento'
        )
        self.l_pg_excluir_data_pagamento.setGeometry(QRect(1, 320, 181, 20))
        self.l_pg_excluir_data_pagamento.setStyleSheet('')
        self.l_pg_excluir_data_pagamento.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_data_pagamento.setIndent(-1)
        self.l_pg_excluir_valor = QLabel(self.frame_5)
        self.l_pg_excluir_valor.setObjectName('l_pg_excluir_valor')
        self.l_pg_excluir_valor.setGeometry(QRect(190, 320, 161, 20))
        self.l_pg_excluir_valor.setStyleSheet('')
        self.l_pg_excluir_valor.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_responsavel = QLabel(self.frame_5)
        self.l_pg_excluir_responsavel.setObjectName('l_pg_excluir_responsavel')
        self.l_pg_excluir_responsavel.setGeometry(QRect(114, 370, 131, 20))
        self.l_pg_excluir_responsavel.setStyleSheet('')
        self.l_pg_excluir_responsavel.setAlignment(Qt.AlignCenter)
        self.pb_excluir_aluno = QPushButton(self.frame_5)
        self.pb_excluir_aluno.setObjectName('pb_excluir_aluno')
        self.pb_excluir_aluno.setGeometry(QRect(143, 440, 75, 24))
        icon3 = QIcon()
        icon3.addFile(
            ':/cadastro/img/excluir-aluno.png',
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.pb_excluir_aluno.setIcon(icon3)
        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName('label_31')
        self.label_31.setGeometry(QRect(0, 50, 111, 4))
        self.label_31.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_32 = QLabel(self.frame_5)
        self.label_32.setObjectName('label_32')
        self.label_32.setGeometry(QRect(250, 130, 111, 4))
        self.label_32.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_33 = QLabel(self.frame_5)
        self.label_33.setObjectName('label_33')
        self.label_33.setGeometry(QRect(0, 90, 111, 4))
        self.label_33.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_49 = QLabel(self.page_3)
        self.label_49.setObjectName('label_49')
        self.label_49.setGeometry(QRect(900, 10, 381, 16))
        self.label_49.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_50 = QLabel(self.page_3)
        self.label_50.setObjectName('label_50')
        self.label_50.setGeometry(QRect(0, 640, 381, 16))
        self.label_50.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_51 = QLabel(self.page_3)
        self.label_51.setObjectName('label_51')
        self.label_51.setGeometry(QRect(250, 440, 211, 16))
        self.label_51.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_52 = QLabel(self.page_3)
        self.label_52.setObjectName('label_52')
        self.label_52.setGeometry(QRect(820, 290, 31, 16))
        self.label_52.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_53 = QLabel(self.page_3)
        self.label_53.setObjectName('label_53')
        self.label_53.setGeometry(QRect(820, 160, 71, 16))
        self.label_53.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_54 = QLabel(self.page_3)
        self.label_54.setObjectName('label_54')
        self.label_54.setGeometry(QRect(310, 370, 151, 10))
        self.label_54.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_55 = QLabel(self.page_3)
        self.label_55.setObjectName('label_55')
        self.label_55.setGeometry(QRect(840, 282, 151, 10))
        self.label_55.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_56 = QLabel(self.page_3)
        self.label_56.setObjectName('label_56')
        self.label_56.setGeometry(QRect(970, 290, 151, 10))
        self.label_56.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_57 = QLabel(self.page_3)
        self.label_57.setObjectName('label_57')
        self.label_57.setGeometry(QRect(280, 430, 151, 10))
        self.label_57.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.stackedWidget.addWidget(self.page_3)
        self.label_55.raise_()
        self.label_57.raise_()
        self.label_53.raise_()
        self.label_52.raise_()
        self.label_51.raise_()
        self.le_excluir_aluno.raise_()
        self.label_20.raise_()
        self.pb_pg_excluir_pesquisar.raise_()
        self.frame_5.raise_()
        self.label_49.raise_()
        self.label_50.raise_()
        self.label_54.raise_()
        self.label_56.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName('page_2')
        self.le_pg_informacoes_pesquisar_aluno = QLineEdit(self.page_2)
        self.le_pg_informacoes_pesquisar_aluno.setObjectName(
            'le_pg_informacoes_pesquisar_aluno'
        )
        self.le_pg_informacoes_pesquisar_aluno.setGeometry(
            QRect(445, 90, 390, 22)
        )
        self.le_pg_informacoes_pesquisar_aluno.setStyleSheet('')
        self.le_pg_informacoes_pesquisar_aluno.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName('label_5')
        self.label_5.setGeometry(QRect(370, 20, 541, 61))
        font3 = QFont()
        font3.setFamilies(['Sitka Small Semibold'])
        font3.setPointSize(36)
        font3.setBold(True)
        font3.setItalic(True)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(
            'font: 600 italic 36pt "Sitka Small Semibold";\n'
            'color: rgb(255, 184, 108);'
        )
        self.label_5.setAlignment(Qt.AlignCenter)
        self.pb_pg_informacoes_pesquisar = QPushButton(self.page_2)
        self.pb_pg_informacoes_pesquisar.setObjectName(
            'pb_pg_informacoes_pesquisar'
        )
        self.pb_pg_informacoes_pesquisar.setGeometry(QRect(810, 90, 21, 16))
        self.pb_pg_informacoes_pesquisar.setStyleSheet(
            'background-color: rgba(255, 255, 255, 0);\n'
            'border-image: url(:/cadastro/img/lupa.png);'
        )
        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName('frame_4')
        self.frame_4.setGeometry(QRect(460, 130, 361, 521))
        self.frame_4.setStyleSheet(
            'QFrame{\n'
            'background-color: rgb(53, 58, 75);\n'
            'border-radius: 30px;\n'
            '}\n'
            'QFrame::hover{\n'
            '	border: 1px solid  rgb(173, 82, 135);\n'
            '	color: rgb(189, 147, 249);\n'
            '}\n'
            'QLabel{\n'
            '	color: rgb(80, 250, 123);\n'
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.42, x2:0, y2:1, stop:0 rgba(53, 58, 75, 255), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}\n'
            'Line{\n'
            '	background-color: rgb(173, 82, 135);\n'
            '}'
        )
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.l_pg_informacoes_nome = QLabel(self.frame_4)
        self.l_pg_informacoes_nome.setObjectName('l_pg_informacoes_nome')
        self.l_pg_informacoes_nome.setGeometry(QRect(1, 200, 131, 20))
        self.l_pg_informacoes_nome.setFont(font)
        self.l_pg_informacoes_nome.setStyleSheet('')
        self.l_pg_informacoes_nome.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_foto = QLabel(self.frame_4)
        self.l_pg_informacoes_foto.setObjectName('l_pg_informacoes_foto')
        self.l_pg_informacoes_foto.setGeometry(QRect(111, 20, 140, 140))
        self.l_pg_informacoes_foto.setStyleSheet(
            'background-color: rgb(255, 255, 255);'
        )
        self.l_pg_informacoes_foto.setScaledContents(True)
        self.l_pg_informacoes_matricula = QLabel(self.frame_4)
        self.l_pg_informacoes_matricula.setObjectName(
            'l_pg_informacoes_matricula'
        )
        self.l_pg_informacoes_matricula.setGeometry(QRect(115, 170, 131, 20))
        self.l_pg_informacoes_matricula.setStyleSheet('')
        self.l_pg_informacoes_matricula.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_matricula.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse
        )
        self.l_pg_informacoes_data_nascimento = QLabel(self.frame_4)
        self.l_pg_informacoes_data_nascimento.setObjectName(
            'l_pg_informacoes_data_nascimento'
        )
        self.l_pg_informacoes_data_nascimento.setGeometry(
            QRect(135, 200, 131, 20)
        )
        self.l_pg_informacoes_data_nascimento.setStyleSheet('')
        self.l_pg_informacoes_data_nascimento.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_cpf = QLabel(self.frame_4)
        self.l_pg_informacoes_cpf.setObjectName('l_pg_informacoes_cpf')
        self.l_pg_informacoes_cpf.setGeometry(QRect(270, 200, 81, 20))
        self.l_pg_informacoes_cpf.setStyleSheet('')
        self.l_pg_informacoes_cpf.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_celular = QLabel(self.frame_4)
        self.l_pg_informacoes_celular.setObjectName('l_pg_informacoes_celular')
        self.l_pg_informacoes_celular.setGeometry(QRect(1, 240, 131, 20))
        self.l_pg_informacoes_celular.setStyleSheet('')
        self.l_pg_informacoes_celular.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_email = QLabel(self.frame_4)
        self.l_pg_informacoes_email.setObjectName('l_pg_informacoes_email')
        self.l_pg_informacoes_email.setGeometry(QRect(135, 240, 216, 20))
        self.l_pg_informacoes_email.setStyleSheet('')
        self.l_pg_informacoes_email.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_cidade = QLabel(self.frame_4)
        self.l_pg_informacoes_cidade.setObjectName('l_pg_informacoes_cidade')
        self.l_pg_informacoes_cidade.setGeometry(QRect(1, 280, 131, 20))
        self.l_pg_informacoes_cidade.setStyleSheet('')
        self.l_pg_informacoes_cidade.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_bairro = QLabel(self.frame_4)
        self.l_pg_informacoes_bairro.setObjectName('l_pg_informacoes_bairro')
        self.l_pg_informacoes_bairro.setGeometry(QRect(135, 280, 131, 20))
        self.l_pg_informacoes_bairro.setStyleSheet('')
        self.l_pg_informacoes_bairro.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_cep = QLabel(self.frame_4)
        self.l_pg_informacoes_cep.setObjectName('l_pg_informacoes_cep')
        self.l_pg_informacoes_cep.setGeometry(QRect(270, 280, 81, 20))
        self.l_pg_informacoes_cep.setStyleSheet('')
        self.l_pg_informacoes_cep.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_data_pagamento = QLabel(self.frame_4)
        self.l_pg_informacoes_data_pagamento.setObjectName(
            'l_pg_informacoes_data_pagamento'
        )
        self.l_pg_informacoes_data_pagamento.setGeometry(
            QRect(1, 320, 181, 20)
        )
        self.l_pg_informacoes_data_pagamento.setStyleSheet('')
        self.l_pg_informacoes_data_pagamento.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_data_pagamento.setIndent(-1)
        self.l_pg_informacoes_valor = QLabel(self.frame_4)
        self.l_pg_informacoes_valor.setObjectName('l_pg_informacoes_valor')
        self.l_pg_informacoes_valor.setGeometry(QRect(190, 320, 161, 20))
        self.l_pg_informacoes_valor.setStyleSheet('')
        self.l_pg_informacoes_valor.setAlignment(Qt.AlignCenter)
        self.l_pg_informacoes_responsavel = QLabel(self.frame_4)
        self.l_pg_informacoes_responsavel.setObjectName(
            'l_pg_informacoes_responsavel'
        )
        self.l_pg_informacoes_responsavel.setGeometry(QRect(114, 370, 131, 20))
        self.l_pg_informacoes_responsavel.setStyleSheet('')
        self.l_pg_informacoes_responsavel.setAlignment(Qt.AlignCenter)
        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName('label_26')
        self.label_26.setGeometry(QRect(0, 130, 111, 4))
        self.label_26.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_27 = QLabel(self.frame_4)
        self.label_27.setObjectName('label_27')
        self.label_27.setGeometry(QRect(250, 110, 111, 4))
        self.label_27.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName('label_28')
        self.label_28.setGeometry(QRect(250, 90, 111, 4))
        self.label_28.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_29 = QLabel(self.frame_4)
        self.label_29.setObjectName('label_29')
        self.label_29.setGeometry(QRect(250, 70, 111, 4))
        self.label_29.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_30 = QLabel(self.frame_4)
        self.label_30.setObjectName('label_30')
        self.label_30.setGeometry(QRect(0, 40, 111, 4))
        self.label_30.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_29.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.l_pg_informacoes_nome.raise_()
        self.l_pg_informacoes_foto.raise_()
        self.l_pg_informacoes_matricula.raise_()
        self.l_pg_informacoes_data_nascimento.raise_()
        self.l_pg_informacoes_cpf.raise_()
        self.l_pg_informacoes_celular.raise_()
        self.l_pg_informacoes_email.raise_()
        self.l_pg_informacoes_cidade.raise_()
        self.l_pg_informacoes_bairro.raise_()
        self.l_pg_informacoes_cep.raise_()
        self.l_pg_informacoes_data_pagamento.raise_()
        self.l_pg_informacoes_valor.raise_()
        self.l_pg_informacoes_responsavel.raise_()
        self.label_26.raise_()
        self.label_30.raise_()
        self.label_42 = QLabel(self.page_2)
        self.label_42.setObjectName('label_42')
        self.label_42.setGeometry(QRect(820, 560, 381, 16))
        self.label_42.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_45 = QLabel(self.page_2)
        self.label_45.setObjectName('label_45')
        self.label_45.setGeometry(QRect(270, 530, 191, 16))
        self.label_45.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_46 = QLabel(self.page_2)
        self.label_46.setObjectName('label_46')
        self.label_46.setGeometry(QRect(820, 500, 381, 16))
        self.label_46.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_47 = QLabel(self.page_2)
        self.label_47.setObjectName('label_47')
        self.label_47.setGeometry(QRect(820, 600, 261, 16))
        self.label_47.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_48 = QLabel(self.page_2)
        self.label_48.setObjectName('label_48')
        self.label_48.setGeometry(QRect(100, 450, 361, 16))
        self.label_48.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_58 = QLabel(self.page_2)
        self.label_58.setObjectName('label_58')
        self.label_58.setGeometry(QRect(1170, 510, 100, 10))
        self.label_58.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_59 = QLabel(self.page_2)
        self.label_59.setObjectName('label_59')
        self.label_59.setGeometry(QRect(940, 490, 151, 10))
        self.label_59.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_60 = QLabel(self.page_2)
        self.label_60.setObjectName('label_60')
        self.label_60.setGeometry(QRect(240, 460, 151, 10))
        self.label_60.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.label_61 = QLabel(self.page_2)
        self.label_61.setObjectName('label_61')
        self.label_61.setGeometry(QRect(130, 535, 151, 5))
        self.label_61.setStyleSheet(
            'background-color: rgb(173, 82, 135);\n'
            'border: none;\n'
            'border-bottom: 2px solid  rgb(189, 147, 249);'
        )
        self.stackedWidget.addWidget(self.page_2)
        self.label_61.raise_()
        self.label_46.raise_()
        self.label_60.raise_()
        self.label_58.raise_()
        self.label_48.raise_()
        self.label_45.raise_()
        self.label_47.raise_()
        self.label_42.raise_()
        self.le_pg_informacoes_pesquisar_aluno.raise_()
        self.label_5.raise_()
        self.pb_pg_informacoes_pesquisar.raise_()
        self.frame_4.raise_()
        self.label_59.raise_()
        JanelaAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaAluno)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(JanelaAluno)

    # setupUi

    def retranslateUi(self, JanelaAluno):
        JanelaAluno.setWindowTitle(
            QCoreApplication.translate('JanelaAluno', 'Aluno', None)
        )
        self.pb_pagina_pagamento.setText('')
        self.pb_pagina_ad_aluno.setText('')
        self.pb_pagina_excluir_aluno.setText('')
        self.pb_pagina_pesquisar_aluno.setText('')
        self.label_21.setText(
            QCoreApplication.translate('JanelaAluno', 'Pagamentos', None)
        )
        self.le_pagamentos.setPlaceholderText(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula/CPF', None
            )
        )
        self.pb_pg_pagamentos_pesquisar.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_nome.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Nome', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_nome.setText('')
        self.l_pg_pagamentos_foto.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_matricula.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Matr\u00edcula', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_matricula.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_data_nascimento.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Data de nascimento', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_data_nascimento.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_cpf.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'CPF', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_cpf.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_celular.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'N\u00famero do celular', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_celular.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_email.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'E-mail', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_email.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_cidade.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Cidade', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_cidade.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_bairro.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Bairro', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_bairro.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_cep.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'CEP', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_cep.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_data_pagamento.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Data pagamento', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_data_pagamento.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_valor.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Valor do pagamento', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_valor.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_pagamentos_responsavel.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula do respons\u00e1vel', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_pagamentos_responsavel.setText('')
        self.pb_pagar_pix.setText(
            QCoreApplication.translate('JanelaAluno', 'Pagar com Pix', None)
        )
        self.pb_imprimir_boleto.setText(
            QCoreApplication.translate('JanelaAluno', 'Imprimir boleto', None)
        )
        self.label_24.setText('')
        self.label_25.setText('')
        self.label_34.setText('')
        self.label_35.setText('')
        self.label_36.setText('')
        self.label_37.setText('')
        self.label_38.setText('')
        self.label_39.setText('')
        self.label_40.setText('')
        self.label_41.setText('')
        self.label_43.setText('')
        self.label_44.setText('')
        self.label.setText(
            QCoreApplication.translate('JanelaAluno', 'Nome do aluno', None)
        )
        self.label_2.setText(
            QCoreApplication.translate('JanelaAluno', 'Data nascimento', None)
        )
        self.label_3.setText(
            QCoreApplication.translate('JanelaAluno', 'CPF', None)
        )
        self.le_cpf_aluno.setInputMask(
            QCoreApplication.translate('JanelaAluno', '999.999.999-99', None)
        )
        self.label_4.setText(
            QCoreApplication.translate('JanelaAluno', 'Celular', None)
        )
        self.le_celular_aluno.setInputMask(
            QCoreApplication.translate('JanelaAluno', '(99)99999-9999', None)
        )
        self.cb_whatsapp_aluno.setText(
            QCoreApplication.translate('JanelaAluno', 'Whatsapp', None)
        )
        self.cb_responsavel.setText(
            QCoreApplication.translate('JanelaAluno', 'Respons\u00e1vel', None)
        )
        # if QT_CONFIG(tooltip)
        self.pb_ad_foto_aluno.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Click para adicionar uma foto', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.pb_ad_foto_aluno.setText('')
        self.l_foto_aluno.setText('')
        self.label_7.setText(
            QCoreApplication.translate('JanelaAluno', 'Bairro', None)
        )
        self.label_8.setText(
            QCoreApplication.translate('JanelaAluno', 'CEP', None)
        )
        self.le_cep_aluno.setInputMask(
            QCoreApplication.translate('JanelaAluno', '99999-999', None)
        )
        self.label_9.setText(
            QCoreApplication.translate('JanelaAluno', 'Cidade', None)
        )
        self.label_10.setText(
            QCoreApplication.translate('JanelaAluno', 'E-mail', None)
        )
        self.le_email_aluno.setPlaceholderText(
            QCoreApplication.translate(
                'JanelaAluno', 'exemplo123@gmail.com', None
            )
        )
        self.groupBox.setTitle(
            QCoreApplication.translate('JanelaAluno', 'Respons\u00e1vel', None)
        )
        self.label_11.setText(
            QCoreApplication.translate(
                'JanelaAluno', 'Nome do respons\u00e1vel', None
            )
        )
        self.label_12.setText(
            QCoreApplication.translate('JanelaAluno', 'Data nascimento', None)
        )
        self.label_13.setText(
            QCoreApplication.translate('JanelaAluno', 'CPF', None)
        )
        self.label_14.setText(
            QCoreApplication.translate('JanelaAluno', 'Celular', None)
        )
        self.label_16.setText(
            QCoreApplication.translate('JanelaAluno', 'Bairro', None)
        )
        self.label_17.setText(
            QCoreApplication.translate('JanelaAluno', 'CEP', None)
        )
        self.label_18.setText(
            QCoreApplication.translate('JanelaAluno', 'Cidade', None)
        )
        self.label_19.setText(
            QCoreApplication.translate('JanelaAluno', 'E-mail', None)
        )
        self.l_foto_responsavel.setText('')
        # if QT_CONFIG(tooltip)
        self.pb_ad_foto_responsavel.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Click para adicionar uma foto', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.pb_ad_foto_responsavel.setText('')
        self.label_15.setText(
            QCoreApplication.translate(
                'JanelaAluno', 'Adicione uma foto', None
            )
        )
        self.le_cpf_responsavel.setInputMask(
            QCoreApplication.translate('JanelaAluno', '999.999.999-99', None)
        )
        self.le_celular_responsavel.setInputMask(
            QCoreApplication.translate('JanelaAluno', '(99)99999-9999', None)
        )
        self.le_cep_responsavel.setInputMask(
            QCoreApplication.translate('JanelaAluno', '99999-999', None)
        )
        self.le_email_responsavel.setPlaceholderText(
            QCoreApplication.translate(
                'JanelaAluno', 'exemplo123@gmail.com', None
            )
        )
        self.pb_salvar_dados.setText(
            QCoreApplication.translate('JanelaAluno', 'Salvar', None)
        )
        self.label_62.setText('')
        self.label_63.setText('')
        self.label_64.setText('')
        self.label_65.setText('')
        self.label_66.setText('')
        self.label_67.setText('')
        self.label_68.setText('')
        self.label_69.setText('')
        self.label_70.setText('')
        self.label_71.setText('')
        self.label_72.setText('')
        self.label_73.setText('')
        self.label_74.setText('')
        self.label_75.setText('')
        self.label_76.setText('')
        self.label_77.setText('')
        self.label_78.setText('')
        self.label_79.setText('')
        self.label_80.setText('')
        self.label_81.setText('')
        self.label_82.setText('')
        self.label_83.setText('')
        self.label_84.setText('')
        self.label_85.setText('')
        self.label_86.setText('')
        self.label_87.setText('')
        self.label_88.setText('')
        self.label_89.setText('')
        self.label_90.setText('')
        self.label_91.setText('')
        self.label_92.setText('')
        self.label_93.setText('')
        self.label_94.setText('')
        self.label_95.setText('')
        self.label_96.setText('')
        self.label_97.setText('')
        self.label_6.setText(
            QCoreApplication.translate(
                'JanelaAluno', 'Adicione uma foto', None
            )
        )
        self.label_22.setText(
            QCoreApplication.translate(
                'JanelaAluno', 'Data do pagamento', None
            )
        )
        self.label_23.setText(
            QCoreApplication.translate(
                'JanelaAluno', 'Valor do pagamento', None
            )
        )
        self.sb_valor_pagamento.setPrefix(
            QCoreApplication.translate('JanelaAluno', 'R$', None)
        )
        self.label_98.setText('')
        self.label_99.setText('')
        self.label_100.setText('')
        self.label_101.setText('')
        self.label_102.setText('')
        self.label_20.setText(
            QCoreApplication.translate('JanelaAluno', 'Excluir aluno', None)
        )
        self.le_excluir_aluno.setPlaceholderText(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula do respons\u00e1vel', None
            )
        )
        self.pb_pg_excluir_pesquisar.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_nome.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Nome', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_nome.setText('')
        self.l_pg_excluir_foto.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_matricula.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Matr\u00edcula', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_matricula.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_data_nascimento.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Data de nascimento', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_data_nascimento.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_cpf.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'CPF', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_cpf.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_celular.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'N\u00famero do celular', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_celular.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_email.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'E-mail', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_email.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_cidade.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Cidade', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_cidade.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_bairro.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Bairro', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_bairro.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_cep.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'CEP', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_cep.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_data_pagamento.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Data pagamento', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_data_pagamento.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_valor.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Valor do pagamento', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_valor.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_excluir_responsavel.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula do respons\u00e1vel', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_excluir_responsavel.setText('')
        self.pb_excluir_aluno.setText(
            QCoreApplication.translate('JanelaAluno', 'Excluir', None)
        )
        self.label_31.setText('')
        self.label_32.setText('')
        self.label_33.setText('')
        self.label_49.setText('')
        self.label_50.setText('')
        self.label_51.setText('')
        self.label_52.setText('')
        self.label_53.setText('')
        self.label_54.setText('')
        self.label_55.setText('')
        self.label_56.setText('')
        self.label_57.setText('')
        self.le_pg_informacoes_pesquisar_aluno.setPlaceholderText(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula/CPF', None
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                'JanelaAluno', 'Informa\u00e7\u00f5es do aluno', None
            )
        )
        self.pb_pg_informacoes_pesquisar.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_nome.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Nome', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_nome.setText('')
        self.l_pg_informacoes_foto.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_matricula.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Matr\u00edcula', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_matricula.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_data_nascimento.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Data de nascimento', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_data_nascimento.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_cpf.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'CPF', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_cpf.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_celular.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'N\u00famero do celular', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_celular.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_email.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'E-mail', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_email.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_cidade.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Cidade', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_cidade.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_bairro.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Bairro', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_bairro.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_cep.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'CEP', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_cep.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_data_pagamento.setToolTip(
            QCoreApplication.translate('JanelaAluno', 'Data pagamento', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_data_pagamento.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_valor.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Valor do pagamento', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_valor.setText('')
        # if QT_CONFIG(tooltip)
        self.l_pg_informacoes_responsavel.setToolTip(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula do respons\u00e1vel', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.l_pg_informacoes_responsavel.setText('')
        self.label_26.setText('')
        self.label_27.setText('')
        self.label_28.setText('')
        self.label_29.setText('')
        self.label_30.setText('')
        self.label_42.setText('')
        self.label_45.setText('')
        self.label_46.setText('')
        self.label_47.setText('')
        self.label_48.setText('')
        self.label_58.setText('')
        self.label_59.setText('')
        self.label_60.setText('')
        self.label_61.setText('')

    # retranslateUi
