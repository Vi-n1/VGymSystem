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
    QAbstractItemView,
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
    QSpinBox,
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
            'QLabel, QCheckBox, QTableWidget{\n'
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
        if self.tw_pagamentos.columnCount() < 13:
            self.tw_pagamentos.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_pagamentos.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.tw_pagamentos.setObjectName('tw_pagamentos')
        self.tw_pagamentos.setGeometry(QRect(34, 350, 1211, 75))
        self.tw_pagamentos.setStyleSheet('border:0;')
        self.tw_pagamentos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_pagamentos.setProperty('showDropIndicator', False)
        self.tw_pagamentos.setDragDropOverwriteMode(False)
        self.tw_pagamentos.setSelectionMode(QAbstractItemView.NoSelection)
        self.tw_pagamentos.horizontalHeader().setVisible(True)
        self.tw_pagamentos.verticalHeader().setVisible(False)
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
        self.label_15.setGeometry(QRect(1020, 0, 111, 16))
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
        font1 = QFont()
        font1.setFamilies(['Arial'])
        font1.setPointSize(10)
        self.pb_salvar_dados.setFont(font1)
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
        if self.tw_exibir_excluir_aluno.columnCount() < 13:
            self.tw_exibir_excluir_aluno.setColumnCount(13)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            0, __qtablewidgetitem13
        )
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            1, __qtablewidgetitem14
        )
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            2, __qtablewidgetitem15
        )
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            3, __qtablewidgetitem16
        )
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            4, __qtablewidgetitem17
        )
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            5, __qtablewidgetitem18
        )
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            6, __qtablewidgetitem19
        )
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            7, __qtablewidgetitem20
        )
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            8, __qtablewidgetitem21
        )
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            9, __qtablewidgetitem22
        )
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            10, __qtablewidgetitem23
        )
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            11, __qtablewidgetitem24
        )
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tw_exibir_excluir_aluno.setHorizontalHeaderItem(
            12, __qtablewidgetitem25
        )
        self.tw_exibir_excluir_aluno.setObjectName('tw_exibir_excluir_aluno')
        self.tw_exibir_excluir_aluno.setGeometry(QRect(34, 350, 1211, 75))
        self.tw_exibir_excluir_aluno.setStyleSheet('border:0;')
        self.tw_exibir_excluir_aluno.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.tw_exibir_excluir_aluno.setTabKeyNavigation(False)
        self.tw_exibir_excluir_aluno.setProperty('showDropIndicator', True)
        self.tw_exibir_excluir_aluno.setDragDropOverwriteMode(False)
        self.tw_exibir_excluir_aluno.setSelectionMode(
            QAbstractItemView.NoSelection
        )
        self.tw_exibir_excluir_aluno.verticalHeader().setVisible(False)
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
        font2 = QFont()
        font2.setFamilies(['Sitka Small Semibold'])
        font2.setPointSize(36)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(
            'font: 600 italic 36pt "Sitka Small Semibold";\n'
            'color: rgb(255, 184, 108);'
        )
        self.label_5.setAlignment(Qt.AlignCenter)
        self.tw_exibir_pesquisar_aluno = QTableWidget(self.page_2)
        if self.tw_exibir_pesquisar_aluno.columnCount() < 13:
            self.tw_exibir_pesquisar_aluno.setColumnCount(13)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            0, __qtablewidgetitem26
        )
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            1, __qtablewidgetitem27
        )
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            2, __qtablewidgetitem28
        )
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            3, __qtablewidgetitem29
        )
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            4, __qtablewidgetitem30
        )
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            5, __qtablewidgetitem31
        )
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            6, __qtablewidgetitem32
        )
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            7, __qtablewidgetitem33
        )
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            8, __qtablewidgetitem34
        )
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            9, __qtablewidgetitem35
        )
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            10, __qtablewidgetitem36
        )
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            11, __qtablewidgetitem37
        )
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tw_exibir_pesquisar_aluno.setHorizontalHeaderItem(
            12, __qtablewidgetitem38
        )
        self.tw_exibir_pesquisar_aluno.setObjectName(
            'tw_exibir_pesquisar_aluno'
        )
        self.tw_exibir_pesquisar_aluno.setGeometry(QRect(34, 350, 1211, 75))
        self.tw_exibir_pesquisar_aluno.setStyleSheet('border:0;')
        self.tw_exibir_pesquisar_aluno.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.tw_exibir_pesquisar_aluno.setProperty('showDropIndicator', False)
        self.tw_exibir_pesquisar_aluno.setDragDropOverwriteMode(False)
        self.tw_exibir_pesquisar_aluno.setSelectionMode(
            QAbstractItemView.NoSelection
        )
        self.tw_exibir_pesquisar_aluno.verticalHeader().setVisible(False)
        self.pb_pesquisar_aluno = QPushButton(self.page_2)
        self.pb_pesquisar_aluno.setObjectName('pb_pesquisar_aluno')
        self.pb_pesquisar_aluno.setGeometry(QRect(810, 320, 21, 16))
        self.pb_pesquisar_aluno.setStyleSheet(
            'background-color: rgba(255, 255, 255, 0);\n'
            'border-image: url(:/cadastro/img/lupa.png);'
        )
        self.stackedWidget.addWidget(self.page_2)
        JanelaAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaAluno)

        self.stackedWidget.setCurrentIndex(0)

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
        ___qtablewidgetitem = self.tw_pagamentos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate('JanelaAluno', 'Matr\u00edcula', None)
        )
        ___qtablewidgetitem1 = self.tw_pagamentos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate('JanelaAluno', 'Nome', None)
        )
        ___qtablewidgetitem2 = self.tw_pagamentos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate('JanelaAluno', 'Data nascimento', None)
        )
        ___qtablewidgetitem3 = self.tw_pagamentos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate('JanelaAluno', 'CPF', None)
        )
        ___qtablewidgetitem4 = self.tw_pagamentos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate('JanelaAluno', 'Celular', None)
        )
        ___qtablewidgetitem5 = self.tw_pagamentos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate('JanelaAluno', '\u00c9 Whatsapp', None)
        )
        ___qtablewidgetitem6 = self.tw_pagamentos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate('JanelaAluno', 'Bairro', None)
        )
        ___qtablewidgetitem7 = self.tw_pagamentos.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate('JanelaAluno', 'CEP', None)
        )
        ___qtablewidgetitem8 = self.tw_pagamentos.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate('JanelaAluno', 'Cidade', None)
        )
        ___qtablewidgetitem9 = self.tw_pagamentos.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate('JanelaAluno', 'E-mail', None)
        )
        ___qtablewidgetitem10 = self.tw_pagamentos.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate('JanelaAluno', 'Data pagamento', None)
        )
        ___qtablewidgetitem11 = self.tw_pagamentos.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(
            QCoreApplication.translate('JanelaAluno', 'Valor', None)
        )
        ___qtablewidgetitem12 = self.tw_pagamentos.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula respons\u00e1vel', None
            )
        )
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
        self.pb_salvar_dados.setText(
            QCoreApplication.translate('JanelaAluno', 'Salvar', None)
        )
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
        self.label_20.setText(
            QCoreApplication.translate('JanelaAluno', 'Excluir aluno', None)
        )
        self.le_excluir_aluno.setPlaceholderText(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula/CPF', None
            )
        )
        ___qtablewidgetitem13 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(0)
        )
        ___qtablewidgetitem13.setText(
            QCoreApplication.translate('JanelaAluno', 'Matr\u00edcula', None)
        )
        ___qtablewidgetitem14 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(1)
        )
        ___qtablewidgetitem14.setText(
            QCoreApplication.translate('JanelaAluno', 'Nome', None)
        )
        ___qtablewidgetitem15 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(2)
        )
        ___qtablewidgetitem15.setText(
            QCoreApplication.translate('JanelaAluno', 'Data nascimento', None)
        )
        ___qtablewidgetitem16 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(3)
        )
        ___qtablewidgetitem16.setText(
            QCoreApplication.translate('JanelaAluno', 'CPF', None)
        )
        ___qtablewidgetitem17 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(4)
        )
        ___qtablewidgetitem17.setText(
            QCoreApplication.translate('JanelaAluno', 'Celular', None)
        )
        ___qtablewidgetitem18 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(5)
        )
        ___qtablewidgetitem18.setText(
            QCoreApplication.translate('JanelaAluno', '\u00c9 Whatsapp', None)
        )
        ___qtablewidgetitem19 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(6)
        )
        ___qtablewidgetitem19.setText(
            QCoreApplication.translate('JanelaAluno', 'Bairro', None)
        )
        ___qtablewidgetitem20 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(7)
        )
        ___qtablewidgetitem20.setText(
            QCoreApplication.translate('JanelaAluno', 'CEP', None)
        )
        ___qtablewidgetitem21 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(8)
        )
        ___qtablewidgetitem21.setText(
            QCoreApplication.translate('JanelaAluno', 'Cidade', None)
        )
        ___qtablewidgetitem22 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(9)
        )
        ___qtablewidgetitem22.setText(
            QCoreApplication.translate('JanelaAluno', 'E-mail', None)
        )
        ___qtablewidgetitem23 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(10)
        )
        ___qtablewidgetitem23.setText(
            QCoreApplication.translate('JanelaAluno', 'Data pagamento', None)
        )
        ___qtablewidgetitem24 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(11)
        )
        ___qtablewidgetitem24.setText(
            QCoreApplication.translate('JanelaAluno', 'Valor', None)
        )
        ___qtablewidgetitem25 = (
            self.tw_exibir_excluir_aluno.horizontalHeaderItem(12)
        )
        ___qtablewidgetitem25.setText(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula respons\u00e1vel', None
            )
        )
        self.pb_excluir_aluno.setText(
            QCoreApplication.translate('JanelaAluno', 'Excluir', None)
        )
        self.pb_pesquisar_excluir.setText('')
        self.le_pesquisar_aluno.setPlaceholderText(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula/CPF', None
            )
        )
        self.label_5.setText(
            QCoreApplication.translate('JanelaAluno', 'Pesquisar aluno', None)
        )
        ___qtablewidgetitem26 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(0)
        )
        ___qtablewidgetitem26.setText(
            QCoreApplication.translate('JanelaAluno', 'Matr\u00edcula', None)
        )
        ___qtablewidgetitem27 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(1)
        )
        ___qtablewidgetitem27.setText(
            QCoreApplication.translate('JanelaAluno', 'Nome', None)
        )
        ___qtablewidgetitem28 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(2)
        )
        ___qtablewidgetitem28.setText(
            QCoreApplication.translate('JanelaAluno', 'Data nascimento', None)
        )
        ___qtablewidgetitem29 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(3)
        )
        ___qtablewidgetitem29.setText(
            QCoreApplication.translate('JanelaAluno', 'CPF', None)
        )
        ___qtablewidgetitem30 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(4)
        )
        ___qtablewidgetitem30.setText(
            QCoreApplication.translate('JanelaAluno', 'Celular', None)
        )
        ___qtablewidgetitem31 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(5)
        )
        ___qtablewidgetitem31.setText(
            QCoreApplication.translate('JanelaAluno', '\u00c9 Whatsapp', None)
        )
        ___qtablewidgetitem32 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(6)
        )
        ___qtablewidgetitem32.setText(
            QCoreApplication.translate('JanelaAluno', 'Bairro', None)
        )
        ___qtablewidgetitem33 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(7)
        )
        ___qtablewidgetitem33.setText(
            QCoreApplication.translate('JanelaAluno', 'CEP', None)
        )
        ___qtablewidgetitem34 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(8)
        )
        ___qtablewidgetitem34.setText(
            QCoreApplication.translate('JanelaAluno', 'Cidade', None)
        )
        ___qtablewidgetitem35 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(9)
        )
        ___qtablewidgetitem35.setText(
            QCoreApplication.translate('JanelaAluno', 'E-mail', None)
        )
        ___qtablewidgetitem36 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(10)
        )
        ___qtablewidgetitem36.setText(
            QCoreApplication.translate('JanelaAluno', 'Data pagamento', None)
        )
        ___qtablewidgetitem37 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(11)
        )
        ___qtablewidgetitem37.setText(
            QCoreApplication.translate('JanelaAluno', 'Valor', None)
        )
        ___qtablewidgetitem38 = (
            self.tw_exibir_pesquisar_aluno.horizontalHeaderItem(12)
        )
        ___qtablewidgetitem38.setText(
            QCoreApplication.translate(
                'JanelaAluno', 'Matr\u00edcula respons\u00e1vel', None
            )
        )
        self.pb_pesquisar_aluno.setText('')

    # retranslateUi
