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
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
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
        self.pb_pagina_pagamento.setGeometry(QRect(10, 10, 50, 50))
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
        self.pb_pagina_ad_aluno.setGeometry(QRect(90, 10, 50, 50))
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
        self.pb_pagina_excluir_aluno.setGeometry(QRect(170, 10, 50, 50))
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
        self.pb_pagina_pesquisar_aluno.setGeometry(QRect(250, 15, 52, 47))
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
            'QLabel, QCheckBox{\n'
            '	color: rgb(255, 255, 255);\n'
            '	font: 10pt "Arial";\n'
            '	color: rgb(80, 250, 123);\n'
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
            'QLineEdit{\n'
            '	font: 700 10pt "Arial";\n'
            '	color: rgb(98, 114, 164);\n'
            '	border: none;\n'
            '	border-bottom: 2px solid  rgb(189, 147, 249);\n'
            '	background-color: rgba(189, 147, 249, 0.1);\n'
            '}\n'
            'QLineEdit::hover{\n'
            '	border-bottom: 2px solid  rgb(208, 99, 162);\n'
            '}\n'
            'QDateEdit{\n'
            '	color: rgb(98, 114, 164);\n'
            '}'
        )
        self.page = QWidget()
        self.page.setObjectName('page')
        self.label_21 = QLabel(self.page)
        self.label_21.setObjectName('label_21')
        self.label_21.setGeometry(QRect(465, 250, 350, 61))
        self.label_21.setStyleSheet(
            'font: 600 italic 36pt "Sitka Small Semibold";\n'
            'color: rgb(255, 184, 108);'
        )
        self.label_21.setAlignment(Qt.AlignCenter)
        self.le_pagamentos = QLineEdit(self.page)
        self.le_pagamentos.setObjectName('le_pagamentos')
        self.le_pagamentos.setGeometry(QRect(465, 320, 351, 22))
        self.le_pagamentos.setAlignment(Qt.AlignCenter)
        self.pb_pesquisar_pagamentos = QPushButton(self.page)
        self.pb_pesquisar_pagamentos.setObjectName('pb_pesquisar_pagamentos')
        self.pb_pesquisar_pagamentos.setGeometry(QRect(790, 320, 21, 16))
        self.pb_pesquisar_pagamentos.setStyleSheet(
            'background-color: rgba(255, 255, 255, 0);\n'
            'border-image: url(:/cadastro/img/lupa.png);'
        )
        self.tw_pagamentos = QTableWidget(self.page)
        self.tw_pagamentos.setObjectName('tw_pagamentos')
        self.tw_pagamentos.setGeometry(QRect(34, 350, 1211, 75))
        self.tw_pagamentos.setStyleSheet('border:0;')
        self.pb_imprimir_boleto = QPushButton(self.page)
        self.pb_imprimir_boleto.setObjectName('pb_imprimir_boleto')
        self.pb_imprimir_boleto.setGeometry(QRect(510, 430, 111, 24))
        icon = QIcon()
        icon.addFile(
            ':/grobal/img/imprimir.png', QSize(), QIcon.Normal, QIcon.Off
        )
        self.pb_imprimir_boleto.setIcon(icon)
        self.pb_pagar_pix = QPushButton(self.page)
        self.pb_pagar_pix.setObjectName('pb_pagar_pix')
        self.pb_pagar_pix.setGeometry(QRect(660, 430, 101, 24))
        icon1 = QIcon()
        icon1.addFile(':/grobal/img/pix.png', QSize(), QIcon.Normal, QIcon.Off)
        self.pb_pagar_pix.setIcon(icon1)
        self.stackedWidget.addWidget(self.page)
        self.page1 = QWidget()
        self.page1.setObjectName('page1')
        self.label = QLabel(self.page1)
        self.label.setObjectName('label')
        self.label.setGeometry(QRect(0, 40, 271, 20))
        self.label.setAlignment(Qt.AlignCenter)
        self.le_nome_aluno = QLineEdit(self.page1)
        self.le_nome_aluno.setObjectName('le_nome_aluno')
        self.le_nome_aluno.setGeometry(QRect(0, 60, 271, 22))
        self.le_nome_aluno.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.page1)
        self.label_2.setObjectName('label_2')
        self.label_2.setGeometry(QRect(300, 40, 151, 20))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.de_data_nascimento = QDateEdit(self.page1)
        self.de_data_nascimento.setObjectName('de_data_nascimento')
        self.de_data_nascimento.setGeometry(QRect(300, 60, 151, 22))
        self.de_data_nascimento.setAlignment(Qt.AlignCenter)
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
        self.label_6 = QLabel(self.page1)
        self.label_6.setObjectName('label_6')
        self.label_6.setGeometry(QRect(0, 110, 271, 20))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.le_endereco_aluno = QLineEdit(self.page1)
        self.le_endereco_aluno.setObjectName('le_endereco_aluno')
        self.le_endereco_aluno.setGeometry(QRect(0, 130, 271, 22))
        self.le_endereco_aluno.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.page1)
        self.label_7.setObjectName('label_7')
        self.label_7.setGeometry(QRect(300, 110, 151, 20))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.le_bairro_aluno = QLineEdit(self.page1)
        self.le_bairro_aluno.setObjectName('le_bairro_aluno')
        self.le_bairro_aluno.setGeometry(QRect(300, 130, 151, 22))
        self.le_bairro_aluno.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.page1)
        self.label_8.setObjectName('label_8')
        self.label_8.setGeometry(QRect(480, 110, 131, 20))
        self.label_8.setAlignment(Qt.AlignCenter)
        self.le_cep_aluno = QLineEdit(self.page1)
        self.le_cep_aluno.setObjectName('le_cep_aluno')
        self.le_cep_aluno.setGeometry(QRect(480, 130, 131, 22))
        self.le_cep_aluno.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.page1)
        self.label_9.setObjectName('label_9')
        self.label_9.setGeometry(QRect(640, 110, 171, 20))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.le_cidade_aluno = QLineEdit(self.page1)
        self.le_cidade_aluno.setObjectName('le_cidade_aluno')
        self.le_cidade_aluno.setGeometry(QRect(640, 130, 171, 22))
        self.le_cidade_aluno.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.page1)
        self.label_10.setObjectName('label_10')
        self.label_10.setGeometry(QRect(0, 170, 271, 20))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.le_email_aluno = QLineEdit(self.page1)
        self.le_email_aluno.setObjectName('le_email_aluno')
        self.le_email_aluno.setGeometry(QRect(0, 190, 271, 22))
        self.le_email_aluno.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.page1)
        self.groupBox.setObjectName('groupBox')
        self.groupBox.setGeometry(QRect(0, 240, 1280, 421))
        font = QFont()
        font.setFamilies(['Arial'])
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox.setFont(font)
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
        self.label_11.setGeometry(QRect(0, 40, 271, 20))
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName('label_12')
        self.label_12.setGeometry(QRect(300, 40, 151, 20))
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName('label_13')
        self.label_13.setGeometry(QRect(480, 40, 131, 20))
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName('label_14')
        self.label_14.setGeometry(QRect(640, 40, 171, 20))
        self.label_14.setAlignment(Qt.AlignCenter)
        self.le_nome_responsavel = QLineEdit(self.groupBox)
        self.le_nome_responsavel.setObjectName('le_nome_responsavel')
        self.le_nome_responsavel.setGeometry(QRect(0, 60, 271, 22))
        self.le_nome_responsavel.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName('label_15')
        self.label_15.setGeometry(QRect(0, 110, 271, 20))
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName('label_16')
        self.label_16.setGeometry(QRect(300, 110, 151, 20))
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName('label_17')
        self.label_17.setGeometry(QRect(480, 110, 131, 20))
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName('label_18')
        self.label_18.setGeometry(QRect(640, 110, 171, 20))
        self.label_18.setAlignment(Qt.AlignCenter)
        self.de_data_nascimento_responsavel = QDateEdit(self.groupBox)
        self.de_data_nascimento_responsavel.setObjectName(
            'de_data_nascimento_responsavel'
        )
        self.de_data_nascimento_responsavel.setGeometry(
            QRect(300, 60, 151, 22)
        )
        self.de_data_nascimento_responsavel.setAlignment(Qt.AlignCenter)
        self.de_data_nascimento_responsavel.setButtonSymbols(
            QAbstractSpinBox.UpDownArrows
        )
        self.de_data_nascimento_responsavel.setCalendarPopup(True)
        self.le_cpf_responsavel = QLineEdit(self.groupBox)
        self.le_cpf_responsavel.setObjectName('le_cpf_responsavel')
        self.le_cpf_responsavel.setGeometry(QRect(480, 60, 131, 22))
        self.le_cpf_responsavel.setAlignment(Qt.AlignCenter)
        self.le_celular_responsavel = QLineEdit(self.groupBox)
        self.le_celular_responsavel.setObjectName('le_celular_responsavel')
        self.le_celular_responsavel.setGeometry(QRect(640, 60, 171, 22))
        self.le_celular_responsavel.setAlignment(Qt.AlignCenter)
        self.le_endereco_responsavel = QLineEdit(self.groupBox)
        self.le_endereco_responsavel.setObjectName('le_endereco_responsavel')
        self.le_endereco_responsavel.setGeometry(QRect(0, 130, 271, 22))
        self.le_endereco_responsavel.setAlignment(Qt.AlignCenter)
        self.le_bairro_responsavel = QLineEdit(self.groupBox)
        self.le_bairro_responsavel.setObjectName('le_bairro_responsavel')
        self.le_bairro_responsavel.setGeometry(QRect(300, 130, 151, 22))
        self.le_bairro_responsavel.setAlignment(Qt.AlignCenter)
        self.le_cep_responsavel = QLineEdit(self.groupBox)
        self.le_cep_responsavel.setObjectName('le_cep_responsavel')
        self.le_cep_responsavel.setGeometry(QRect(480, 130, 131, 22))
        self.le_cep_responsavel.setAlignment(Qt.AlignCenter)
        self.le_cidade_responsavel = QLineEdit(self.groupBox)
        self.le_cidade_responsavel.setObjectName('le_cidade_responsavel')
        self.le_cidade_responsavel.setGeometry(QRect(640, 130, 171, 22))
        self.le_cidade_responsavel.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName('label_19')
        self.label_19.setGeometry(QRect(0, 170, 271, 20))
        self.label_19.setAlignment(Qt.AlignCenter)
        self.le_email_responsavel = QLineEdit(self.groupBox)
        self.le_email_responsavel.setObjectName('le_email_responsavel')
        self.le_email_responsavel.setGeometry(QRect(0, 190, 271, 22))
        self.le_email_responsavel.setAlignment(Qt.AlignCenter)
        self.l_foto_responsavel = QLabel(self.groupBox)
        self.l_foto_responsavel.setObjectName('l_foto_responsavel')
        self.l_foto_responsavel.setGeometry(QRect(940, 90, 271, 211))
        self.pb_ad_foto_responsavel = QPushButton(self.groupBox)
        self.pb_ad_foto_responsavel.setObjectName('pb_ad_foto_responsavel')
        self.pb_ad_foto_responsavel.setGeometry(QRect(940, 90, 271, 211))
        self.pb_ad_foto_responsavel.setStyleSheet(
            'QPushButton{\n'
            '	border-radius: 5%;\n'
            '	border: 2px solid  rgb(208, 99, 162);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            ''
        )
        self.l_foto_responsavel.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.le_nome_responsavel.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.de_data_nascimento_responsavel.raise_()
        self.le_cpf_responsavel.raise_()
        self.le_celular_responsavel.raise_()
        self.le_endereco_responsavel.raise_()
        self.le_bairro_responsavel.raise_()
        self.le_cep_responsavel.raise_()
        self.le_cidade_responsavel.raise_()
        self.label_19.raise_()
        self.le_email_responsavel.raise_()
        self.pb_ad_foto_responsavel.raise_()
        self.stackedWidget.addWidget(self.page1)
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
        self.label_6.raise_()
        self.le_endereco_aluno.raise_()
        self.label_7.raise_()
        self.le_bairro_aluno.raise_()
        self.label_8.raise_()
        self.le_cep_aluno.raise_()
        self.label_9.raise_()
        self.le_cidade_aluno.raise_()
        self.label_10.raise_()
        self.le_email_aluno.raise_()
        self.groupBox.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName('page_3')
        self.label_20 = QLabel(self.page_3)
        self.label_20.setObjectName('label_20')
        self.label_20.setGeometry(QRect(465, 250, 350, 61))
        self.label_20.setStyleSheet(
            'font: 600 italic 36pt "Sitka Small Semibold";\n'
            'color: rgb(255, 184, 108);'
        )
        self.label_20.setAlignment(Qt.AlignCenter)
        self.le_excluir_aluno = QLineEdit(self.page_3)
        self.le_excluir_aluno.setObjectName('le_excluir_aluno')
        self.le_excluir_aluno.setGeometry(QRect(466, 319, 351, 22))
        self.le_excluir_aluno.setAlignment(Qt.AlignCenter)
        self.tw_exibir_excluir_aluno = QTableWidget(self.page_3)
        self.tw_exibir_excluir_aluno.setObjectName('tw_exibir_excluir_aluno')
        self.tw_exibir_excluir_aluno.setGeometry(QRect(34, 350, 1211, 75))
        self.tw_exibir_excluir_aluno.setStyleSheet('border:0;')
        self.pb_excluir_aluno = QPushButton(self.page_3)
        self.pb_excluir_aluno.setObjectName('pb_excluir_aluno')
        self.pb_excluir_aluno.setGeometry(QRect(602, 430, 75, 24))
        icon2 = QIcon()
        icon2.addFile(
            ':/cadastro/img/excluir-aluno.png',
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.pb_excluir_aluno.setIcon(icon2)
        self.pb_pesquisar_excluir = QPushButton(self.page_3)
        self.pb_pesquisar_excluir.setObjectName('pb_pesquisar_excluir')
        self.pb_pesquisar_excluir.setGeometry(QRect(790, 320, 21, 16))
        self.pb_pesquisar_excluir.setStyleSheet(
            'background-color: rgba(255, 255, 255, 0);\n'
            'border-image: url(:/cadastro/img/lupa.png);'
        )
        self.stackedWidget.addWidget(self.page_3)
        self.le_excluir_aluno.raise_()
        self.label_20.raise_()
        self.tw_exibir_excluir_aluno.raise_()
        self.pb_excluir_aluno.raise_()
        self.pb_pesquisar_excluir.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName('page_2')
        self.le_pesquisar_aluno = QLineEdit(self.page_2)
        self.le_pesquisar_aluno.setObjectName('le_pesquisar_aluno')
        self.le_pesquisar_aluno.setGeometry(QRect(445, 319, 390, 22))
        self.le_pesquisar_aluno.setStyleSheet('')
        self.le_pesquisar_aluno.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName('label_5')
        self.label_5.setGeometry(QRect(435, 250, 411, 61))
        font1 = QFont()
        font1.setFamilies(['Sitka Small Semibold'])
        font1.setPointSize(36)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(
            'font: 600 italic 36pt "Sitka Small Semibold";\n'
            'color: rgb(255, 184, 108);'
        )
        self.label_5.setAlignment(Qt.AlignCenter)
        self.tw_exibir_pesquisar_aluno = QTableWidget(self.page_2)
        self.tw_exibir_pesquisar_aluno.setObjectName(
            'tw_exibir_pesquisar_aluno'
        )
        self.tw_exibir_pesquisar_aluno.setGeometry(QRect(34, 350, 1211, 75))
        self.tw_exibir_pesquisar_aluno.setStyleSheet('border:0;')
        self.pb_presquisar_aluno = QPushButton(self.page_2)
        self.pb_presquisar_aluno.setObjectName('pb_presquisar_aluno')
        self.pb_presquisar_aluno.setGeometry(QRect(810, 320, 21, 16))
        self.pb_presquisar_aluno.setStyleSheet(
            'background-color: rgba(255, 255, 255, 0);\n'
            'border-image: url(:/cadastro/img/lupa.png);'
        )
        self.stackedWidget.addWidget(self.page_2)
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
        self.pb_pesquisar_pagamentos.setText('')
        self.pb_imprimir_boleto.setText(
            QCoreApplication.translate('JanelaAluno', 'Imprimir boleto', None)
        )
        self.pb_pagar_pix.setText(
            QCoreApplication.translate('JanelaAluno', 'Pagar com Pix', None)
        )
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
            QCoreApplication.translate('JanelaAluno', '(99)9999999-99', None)
        )
        self.cb_whatsapp_aluno.setText(
            QCoreApplication.translate('JanelaAluno', 'Whatsapp', None)
        )
        self.cb_responsavel.setText(
            QCoreApplication.translate('JanelaAluno', 'Respons\u00e1vel', None)
        )
        self.pb_ad_foto_aluno.setText('')
        self.l_foto_aluno.setText('')
        self.label_6.setText(
            QCoreApplication.translate('JanelaAluno', 'Endere\u00e7o', None)
        )
        self.label_7.setText(
            QCoreApplication.translate('JanelaAluno', 'Bairro', None)
        )
        self.label_8.setText(
            QCoreApplication.translate('JanelaAluno', 'CEP', None)
        )
        self.label_9.setText(
            QCoreApplication.translate('JanelaAluno', 'Cidade', None)
        )
        self.label_10.setText(
            QCoreApplication.translate('JanelaAluno', 'E-mail', None)
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
        self.label_15.setText(
            QCoreApplication.translate('JanelaAluno', 'Endere\u00e7o', None)
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
        self.pb_ad_foto_responsavel.setText('')
        self.label_20.setText(
            QCoreApplication.translate('JanelaAluno', 'Excluir aluno', None)
        )
        self.le_excluir_aluno.setPlaceholderText(
            QCoreApplication.translate('JanelaAluno', 'Matr\u00edcula', None)
        )
        self.pb_excluir_aluno.setText(
            QCoreApplication.translate('JanelaAluno', 'Excluir', None)
        )
        self.pb_pesquisar_excluir.setText('')
        self.le_pesquisar_aluno.setPlaceholderText(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula/Nome completo', None
            )
        )
        self.label_5.setText(
            QCoreApplication.translate('JanelaAluno', 'Pesquisar aluno', None)
        )
        self.pb_presquisar_aluno.setText('')

    # retranslateUi
