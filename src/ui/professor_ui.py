# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'professor.ui'
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
    QComboBox,
    QDateEdit,
    QFrame,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from .img_rc import *


class Ui_Professor(object):
    def setupUi(self, Professor):
        if not Professor.objectName():
            Professor.setObjectName('Professor')
        Professor.resize(800, 600)
        Professor.setMinimumSize(QSize(800, 600))
        Professor.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(
            ':/icon/icon/professor.ico', QSize(), QIcon.Normal, QIcon.Off
        )
        Professor.setWindowIcon(icon)
        Professor.setStyleSheet(
            'QMessageBox{\n'
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.341, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}\n'
            'QMessageBox QLabel{\n'
            '	font: 900 10pt "Arial Black";\n'
            '	color: rgb(255, 255, 255);\n'
            '}'
        )
        self.centralwidget = QWidget(Professor)
        self.centralwidget.setObjectName('centralwidget')
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName('frame')
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setMaximumSize(QSize(16777215, 60))
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
        self.pb_pagina_pagamento.setGeometry(QRect(240, 10, 52, 47))
        self.pb_pagina_pagamento.setMinimumSize(QSize(0, 0))
        self.pb_pagina_pagamento.setMaximumSize(QSize(16777215, 16777215))
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
        self.pb_pagina_ad_prof = QPushButton(self.frame)
        self.pb_pagina_ad_prof.setObjectName('pb_pagina_ad_prof')
        self.pb_pagina_ad_prof.setGeometry(QRect(330, 10, 52, 47))
        self.pb_pagina_ad_prof.setMinimumSize(QSize(0, 0))
        self.pb_pagina_ad_prof.setMaximumSize(QSize(16777215, 16777215))
        self.pb_pagina_ad_prof.setStyleSheet(
            'QPushButton{\n'
            '	border-image: url(:/cadastro/img/prof.png);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	border-image: url(:/cadastro/img/prof-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border-image: url(:/cadastro/img/prof-press.png);\n'
            '}'
        )
        self.pb_pagina_excluir_prof = QPushButton(self.frame)
        self.pb_pagina_excluir_prof.setObjectName('pb_pagina_excluir_prof')
        self.pb_pagina_excluir_prof.setGeometry(QRect(420, 10, 52, 47))
        self.pb_pagina_excluir_prof.setMinimumSize(QSize(0, 0))
        self.pb_pagina_excluir_prof.setStyleSheet(
            'QPushButton{\n'
            '	border-image: url(:/cadastro/img/remove-prof.png);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	border-image: url(:/cadastro/img/remove-prof-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border-image: url(:/cadastro/img/remove-prof-press.png);\n'
            '}'
        )
        self.pb_pagina_pesquisar_prof = QPushButton(self.frame)
        self.pb_pagina_pesquisar_prof.setObjectName('pb_pagina_pesquisar_prof')
        self.pb_pagina_pesquisar_prof.setGeometry(QRect(510, 10, 52, 47))
        self.pb_pagina_pesquisar_prof.setMinimumSize(QSize(52, 47))
        self.pb_pagina_pesquisar_prof.setStyleSheet(
            'QPushButton{\n'
            '	border-image: url(:/central/img/procurar-prof.png);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	border-image: url(:/central/img/procurar-prof-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border-image: url(:/central/img/procurar-prof-press.png);\n'
            '}'
        )

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName('frame_2')
        self.frame_2.setStyleSheet(
            'QFrame{\n'
            '	background-color: rgb(68, 71, 90);\n'
            '}\n'
            'QLabel{\n'
            '	font: 700 9pt "Arial";\n'
            '	color: rgb(98, 114, 164);\n'
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
            'QLineEdit, QSpinBox, QCheckBox, QComboBox, QDateEdit, QToolTip{\n'
            '	font: 700 9pt "Arial";\n'
            '	color: rgb(98, 114, 164);\n'
            '	border: none;\n'
            '	border-bottom: 2px solid  rgb(189, 147, 249);\n'
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.42, x2:0, y2:1, stop:0 rgba(53, 58, 75, 255), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}\n'
            'QLineEdit::hover, QSpinBox::hover{\n'
            '	border-bottom: 2px solid  rgb(208, 99, 162);\n'
            '}\n'
            'QDateEdit{\n'
            '	color: rgb(98, 114, 164);\n'
            '}\n'
            'QToolTip{\n'
            '	background-color: rgb(0,'
            ' 0, 0);\n'
            '}'
        )
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName('stackedWidget')
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 540))
        self.stackedWidget.setStyleSheet(
            'QFrame{\n'
            'background-color: qlineargradient(spread:pad, x1:0, y1:0.341, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}'
        )
        self.pagina_ad_prof = QWidget()
        self.pagina_ad_prof.setObjectName('pagina_ad_prof')
        self.frame_3 = QFrame(self.pagina_ad_prof)
        self.frame_3.setObjectName('frame_3')
        self.frame_3.setGeometry(QRect(219, 10, 361, 521))
        self.frame_3.setStyleSheet(
            'QFrame{\n'
            'background-color: rgb(53, 58, 75);\n'
            'border-radius: 30px;\n'
            '}\n'
            'QFrame::hover{\n'
            '	border: 1px solid  rgb(173, 82, 135);\n'
            '	color: rgb(189, 147, 249);\n'
            '}'
        )
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName('label_24')
        self.label_24.setGeometry(QRect(0, 88, 80, 4))
        self.label_24.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName('label_25')
        self.label_25.setGeometry(QRect(300, 60, 60, 4))
        self.label_25.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.le_pg_novo_nome = QLineEdit(self.frame_3)
        self.le_pg_novo_nome.setObjectName('le_pg_novo_nome')
        self.le_pg_novo_nome.setGeometry(QRect(1, 160, 181, 22))
        self.le_pg_novo_nome.setMaxLength(32)
        self.le_pg_novo_nome.setAlignment(Qt.AlignCenter)
        self.de_novo_data_nascimento = QDateEdit(self.frame_3)
        self.de_novo_data_nascimento.setObjectName('de_novo_data_nascimento')
        self.de_novo_data_nascimento.setGeometry(QRect(200, 160, 151, 22))
        font = QFont()
        font.setFamilies(['Arial'])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.de_novo_data_nascimento.setFont(font)
        self.de_novo_data_nascimento.setAlignment(Qt.AlignCenter)
        self.de_novo_data_nascimento.setButtonSymbols(
            QAbstractSpinBox.UpDownArrows
        )
        self.de_novo_data_nascimento.setAccelerated(True)
        self.de_novo_data_nascimento.setMaximumDate(QDate(2005, 12, 31))
        self.de_novo_data_nascimento.setCalendarPopup(True)
        self.de_novo_data_nascimento.setTimeSpec(Qt.LocalTime)
        self.le_pg_novo_cpf = QLineEdit(self.frame_3)
        self.le_pg_novo_cpf.setObjectName('le_pg_novo_cpf')
        self.le_pg_novo_cpf.setGeometry(QRect(1, 210, 131, 22))
        self.le_pg_novo_cpf.setMaxLength(11)
        self.le_pg_novo_cpf.setAlignment(Qt.AlignCenter)
        self.le_pg_novo_celular = QLineEdit(self.frame_3)
        self.le_pg_novo_celular.setObjectName('le_pg_novo_celular')
        self.le_pg_novo_celular.setGeometry(QRect(140, 210, 131, 22))
        self.le_pg_novo_celular.setMaxLength(11)
        self.le_pg_novo_celular.setAlignment(Qt.AlignCenter)
        self.le_pg_novo_celular.setClearButtonEnabled(False)
        self.checkbox_pg_novo_whatsapp = QCheckBox(self.frame_3)
        self.checkbox_pg_novo_whatsapp.setObjectName(
            'checkbox_pg_novo_whatsapp'
        )
        self.checkbox_pg_novo_whatsapp.setGeometry(QRect(275, 210, 84, 22))
        self.checkbox_pg_novo_whatsapp.setFont(font)
        self.le_pg_novo_email = QLineEdit(self.frame_3)
        self.le_pg_novo_email.setObjectName('le_pg_novo_email')
        self.le_pg_novo_email.setGeometry(QRect(1, 260, 113, 22))
        self.le_pg_novo_email.setMaxLength(32)
        self.le_pg_novo_email.setAlignment(Qt.AlignCenter)
        self.le_pg_novo_cidade = QLineEdit(self.frame_3)
        self.le_pg_novo_cidade.setObjectName('le_pg_novo_cidade')
        self.le_pg_novo_cidade.setGeometry(QRect(120, 260, 101, 22))
        self.le_pg_novo_cidade.setMaxLength(28)
        self.le_pg_novo_cidade.setAlignment(Qt.AlignCenter)
        self.le_pg_novo_bairro = QLineEdit(self.frame_3)
        self.le_pg_novo_bairro.setObjectName('le_pg_novo_bairro')
        self.le_pg_novo_bairro.setGeometry(QRect(230, 260, 121, 22))
        self.le_pg_novo_bairro.setMaxLength(28)
        self.le_pg_novo_bairro.setAlignment(Qt.AlignCenter)
        self.le_pg_novo_cep = QLineEdit(self.frame_3)
        self.le_pg_novo_cep.setObjectName('le_pg_novo_cep')
        self.le_pg_novo_cep.setGeometry(QRect(1, 310, 181, 22))
        self.le_pg_novo_cep.setMaxLength(8)
        self.le_pg_novo_cep.setAlignment(Qt.AlignCenter)
        self.combobox_novo_formacao = QComboBox(self.frame_3)
        self.combobox_novo_formacao.addItem('')
        self.combobox_novo_formacao.addItem('')
        self.combobox_novo_formacao.setObjectName('combobox_novo_formacao')
        self.combobox_novo_formacao.setGeometry(QRect(190, 310, 161, 22))
        self.combobox_novo_formacao.setInsertPolicy(QComboBox.InsertAtTop)
        self.combobox_novo_formacao.setModelColumn(0)
        self.l_pg_novo_ad_foto = QLabel(self.frame_3)
        self.l_pg_novo_ad_foto.setObjectName('l_pg_novo_ad_foto')
        self.l_pg_novo_ad_foto.setGeometry(QRect(108, 34, 145, 101))
        self.l_pg_novo_ad_foto.setStyleSheet(
            'background-color: rgb(255, 255, 255);'
        )
        self.l_pg_novo_ad_foto.setScaledContents(True)
        self.label_26 = QLabel(self.frame_3)
        self.label_26.setObjectName('label_26')
        self.label_26.setGeometry(QRect(30, 84, 50, 4))
        self.label_26.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName('label_27')
        self.label_27.setGeometry(QRect(30, 80, 79, 4))
        self.label_27.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName('label_28')
        self.label_28.setGeometry(QRect(250, 57, 50, 9))
        self.label_28.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.sb_pg_novo_salario = QSpinBox(self.frame_3)
        self.sb_pg_novo_salario.setObjectName('sb_pg_novo_salario')
        self.sb_pg_novo_salario.setGeometry(QRect(20, 350, 151, 22))
        self.sb_pg_novo_salario.setAlignment(Qt.AlignCenter)
        self.sb_pg_novo_salario.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_pg_novo_salario.setAccelerated(True)
        self.sb_pg_novo_salario.setMaximum(999999)
        self.sb_pg_novo_pagamento = QSpinBox(self.frame_3)
        self.sb_pg_novo_pagamento.setObjectName('sb_pg_novo_pagamento')
        self.sb_pg_novo_pagamento.setGeometry(QRect(190, 350, 151, 22))
        self.sb_pg_novo_pagamento.setAlignment(Qt.AlignCenter)
        self.sb_pg_novo_pagamento.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sb_pg_novo_pagamento.setAccelerated(True)
        self.sb_pg_novo_pagamento.setMinimum(1)
        self.sb_pg_novo_pagamento.setMaximum(31)
        self.pb_pg_novo_salvar_dados = QPushButton(self.frame_3)
        self.pb_pg_novo_salvar_dados.setObjectName('pb_pg_novo_salvar_dados')
        self.pb_pg_novo_salvar_dados.setGeometry(QRect(143, 450, 75, 24))
        self.pb_novo_ad_foto = QPushButton(self.frame_3)
        self.pb_novo_ad_foto.setObjectName('pb_novo_ad_foto')
        self.pb_novo_ad_foto.setGeometry(QRect(108, 34, 145, 101))
        self.pb_novo_ad_foto.setStyleSheet(
            'border:0;\n' 'background-color: rgba(255, 255, 255, 0);'
        )
        self.label_28.raise_()
        self.label_27.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.le_pg_novo_nome.raise_()
        self.de_novo_data_nascimento.raise_()
        self.le_pg_novo_cpf.raise_()
        self.le_pg_novo_celular.raise_()
        self.checkbox_pg_novo_whatsapp.raise_()
        self.le_pg_novo_email.raise_()
        self.le_pg_novo_cidade.raise_()
        self.le_pg_novo_bairro.raise_()
        self.le_pg_novo_cep.raise_()
        self.combobox_novo_formacao.raise_()
        self.l_pg_novo_ad_foto.raise_()
        self.label_26.raise_()
        self.sb_pg_novo_salario.raise_()
        self.sb_pg_novo_pagamento.raise_()
        self.pb_pg_novo_salvar_dados.raise_()
        self.pb_novo_ad_foto.raise_()
        self.label = QLabel(self.pagina_ad_prof)
        self.label.setObjectName('label')
        self.label.setGeometry(QRect(354, 0, 4, 10))
        self.label.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.stackedWidget.addWidget(self.pagina_ad_prof)
        self.label.raise_()
        self.frame_3.raise_()
        self.pagina_pesquisar_prof = QWidget()
        self.pagina_pesquisar_prof.setObjectName('pagina_pesquisar_prof')
        self.frame_4 = QFrame(self.pagina_pesquisar_prof)
        self.frame_4.setObjectName('frame_4')
        self.frame_4.setGeometry(QRect(219, 10, 361, 521))
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
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.42, x2:0, y2:1, stop:0 rgba(53, 58, 75, 255), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}'
        )
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_59 = QLabel(self.frame_4)
        self.label_59.setObjectName('label_59')
        self.label_59.setGeometry(QRect(0, 88, 80, 4))
        self.label_59.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_60 = QLabel(self.frame_4)
        self.label_60.setObjectName('label_60')
        self.label_60.setGeometry(QRect(300, 60, 60, 4))
        self.label_60.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.l_pg_pesquisar_foto = QLabel(self.frame_4)
        self.l_pg_pesquisar_foto.setObjectName('l_pg_pesquisar_foto')
        self.l_pg_pesquisar_foto.setGeometry(QRect(108, 34, 145, 101))
        self.l_pg_pesquisar_foto.setStyleSheet(
            'background-color: rgb(255, 255, 255);'
        )
        self.l_pg_pesquisar_foto.setScaledContents(True)
        self.label_61 = QLabel(self.frame_4)
        self.label_61.setObjectName('label_61')
        self.label_61.setGeometry(QRect(30, 84, 50, 4))
        self.label_61.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_62 = QLabel(self.frame_4)
        self.label_62.setObjectName('label_62')
        self.label_62.setGeometry(QRect(30, 80, 79, 4))
        self.label_62.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_63 = QLabel(self.frame_4)
        self.label_63.setObjectName('label_63')
        self.label_63.setGeometry(QRect(250, 57, 50, 9))
        self.label_63.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.l_pg_pesquisar_nome = QLabel(self.frame_4)
        self.l_pg_pesquisar_nome.setObjectName('l_pg_pesquisar_nome')
        self.l_pg_pesquisar_nome.setGeometry(QRect(1, 160, 181, 22))
        self.l_pg_pesquisar_nome.setStyleSheet('')
        self.l_pg_pesquisar_nome.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_nascimento = QLabel(self.frame_4)
        self.l_pg_pesquisar_nascimento.setObjectName(
            'l_pg_pesquisar_nascimento'
        )
        self.l_pg_pesquisar_nascimento.setGeometry(QRect(200, 160, 151, 22))
        self.l_pg_pesquisar_nascimento.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_cpf = QLabel(self.frame_4)
        self.l_pg_pesquisar_cpf.setObjectName('l_pg_pesquisar_cpf')
        self.l_pg_pesquisar_cpf.setGeometry(QRect(1, 210, 181, 22))
        self.l_pg_pesquisar_cpf.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_celular = QLabel(self.frame_4)
        self.l_pg_pesquisar_celular.setObjectName('l_pg_pesquisar_celular')
        self.l_pg_pesquisar_celular.setGeometry(QRect(200, 210, 151, 22))
        self.l_pg_pesquisar_celular.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_email = QLabel(self.frame_4)
        self.l_pg_pesquisar_email.setObjectName('l_pg_pesquisar_email')
        self.l_pg_pesquisar_email.setGeometry(QRect(1, 260, 113, 22))
        self.l_pg_pesquisar_email.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_cidade = QLabel(self.frame_4)
        self.l_pg_pesquisar_cidade.setObjectName('l_pg_pesquisar_cidade')
        self.l_pg_pesquisar_cidade.setGeometry(QRect(120, 260, 101, 22))
        self.l_pg_pesquisar_cidade.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_bairro = QLabel(self.frame_4)
        self.l_pg_pesquisar_bairro.setObjectName('l_pg_pesquisar_bairro')
        self.l_pg_pesquisar_bairro.setGeometry(QRect(230, 260, 121, 22))
        self.l_pg_pesquisar_bairro.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_cep = QLabel(self.frame_4)
        self.l_pg_pesquisar_cep.setObjectName('l_pg_pesquisar_cep')
        self.l_pg_pesquisar_cep.setGeometry(QRect(1, 310, 181, 22))
        self.l_pg_pesquisar_cep.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_formacao = QLabel(self.frame_4)
        self.l_pg_pesquisar_formacao.setObjectName('l_pg_pesquisar_formacao')
        self.l_pg_pesquisar_formacao.setGeometry(QRect(190, 310, 161, 22))
        self.l_pg_pesquisar_formacao.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_salario = QLabel(self.frame_4)
        self.l_pg_pesquisar_salario.setObjectName('l_pg_pesquisar_salario')
        self.l_pg_pesquisar_salario.setGeometry(QRect(20, 350, 151, 22))
        self.l_pg_pesquisar_salario.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_pagamento = QLabel(self.frame_4)
        self.l_pg_pesquisar_pagamento.setObjectName('l_pg_pesquisar_pagamento')
        self.l_pg_pesquisar_pagamento.setGeometry(QRect(190, 350, 151, 22))
        self.l_pg_pesquisar_pagamento.setAlignment(Qt.AlignCenter)
        self.pb_pg_pesquisar = QPushButton(self.frame_4)
        self.pb_pg_pesquisar.setObjectName('pb_pg_pesquisar')
        self.pb_pg_pesquisar.setGeometry(QRect(143, 460, 75, 24))
        self.le_pg_pesquisar = QLineEdit(self.frame_4)
        self.le_pg_pesquisar.setObjectName('le_pg_pesquisar')
        self.le_pg_pesquisar.setGeometry(QRect(105, 420, 151, 22))
        self.le_pg_pesquisar.setMaxLength(11)
        self.le_pg_pesquisar.setAlignment(Qt.AlignCenter)
        self.l_pg_pesquisar_matricula = QLabel(self.frame_4)
        self.l_pg_pesquisar_matricula.setObjectName('l_pg_pesquisar_matricula')
        self.l_pg_pesquisar_matricula.setGeometry(QRect(90, 380, 181, 22))
        self.l_pg_pesquisar_matricula.setStyleSheet('')
        self.l_pg_pesquisar_matricula.setAlignment(Qt.AlignCenter)
        self.label_62.raise_()
        self.label_63.raise_()
        self.label_59.raise_()
        self.label_60.raise_()
        self.l_pg_pesquisar_foto.raise_()
        self.label_61.raise_()
        self.l_pg_pesquisar_nome.raise_()
        self.l_pg_pesquisar_nascimento.raise_()
        self.l_pg_pesquisar_cpf.raise_()
        self.l_pg_pesquisar_celular.raise_()
        self.l_pg_pesquisar_email.raise_()
        self.l_pg_pesquisar_cidade.raise_()
        self.l_pg_pesquisar_bairro.raise_()
        self.l_pg_pesquisar_cep.raise_()
        self.l_pg_pesquisar_formacao.raise_()
        self.l_pg_pesquisar_salario.raise_()
        self.l_pg_pesquisar_pagamento.raise_()
        self.pb_pg_pesquisar.raise_()
        self.le_pg_pesquisar.raise_()
        self.l_pg_pesquisar_matricula.raise_()
        self.label_13 = QLabel(self.pagina_pesquisar_prof)
        self.label_13.setObjectName('label_13')
        self.label_13.setGeometry(QRect(534, 0, 4, 10))
        self.label_13.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.stackedWidget.addWidget(self.pagina_pesquisar_prof)
        self.pagina_excluir = QWidget()
        self.pagina_excluir.setObjectName('pagina_excluir')
        self.frame_5 = QFrame(self.pagina_excluir)
        self.frame_5.setObjectName('frame_5')
        self.frame_5.setGeometry(QRect(219, 10, 361, 521))
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
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.42, x2:0, y2:1, stop:0 rgba(53, 58, 75, 255), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}'
        )
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_64 = QLabel(self.frame_5)
        self.label_64.setObjectName('label_64')
        self.label_64.setGeometry(QRect(0, 88, 80, 4))
        self.label_64.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_65 = QLabel(self.frame_5)
        self.label_65.setObjectName('label_65')
        self.label_65.setGeometry(QRect(300, 60, 60, 4))
        self.label_65.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.l_pg_excluir_foto = QLabel(self.frame_5)
        self.l_pg_excluir_foto.setObjectName('l_pg_excluir_foto')
        self.l_pg_excluir_foto.setGeometry(QRect(108, 34, 145, 101))
        self.l_pg_excluir_foto.setStyleSheet(
            'background-color: rgb(255, 255, 255);'
        )
        self.l_pg_excluir_foto.setScaledContents(True)
        self.label_66 = QLabel(self.frame_5)
        self.label_66.setObjectName('label_66')
        self.label_66.setGeometry(QRect(30, 84, 50, 4))
        self.label_66.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_67 = QLabel(self.frame_5)
        self.label_67.setObjectName('label_67')
        self.label_67.setGeometry(QRect(30, 80, 79, 4))
        self.label_67.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.label_68 = QLabel(self.frame_5)
        self.label_68.setObjectName('label_68')
        self.label_68.setGeometry(QRect(250, 57, 50, 9))
        self.label_68.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.l_pg_excluir_nome = QLabel(self.frame_5)
        self.l_pg_excluir_nome.setObjectName('l_pg_excluir_nome')
        self.l_pg_excluir_nome.setGeometry(QRect(1, 160, 181, 22))
        self.l_pg_excluir_nome.setStyleSheet('')
        self.l_pg_excluir_nome.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_nascimento = QLabel(self.frame_5)
        self.l_pg_excluir_nascimento.setObjectName('l_pg_excluir_nascimento')
        self.l_pg_excluir_nascimento.setGeometry(QRect(200, 160, 151, 22))
        self.l_pg_excluir_nascimento.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_cpf = QLabel(self.frame_5)
        self.l_pg_excluir_cpf.setObjectName('l_pg_excluir_cpf')
        self.l_pg_excluir_cpf.setGeometry(QRect(1, 210, 181, 22))
        self.l_pg_excluir_cpf.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_celular = QLabel(self.frame_5)
        self.l_pg_excluir_celular.setObjectName('l_pg_excluir_celular')
        self.l_pg_excluir_celular.setGeometry(QRect(200, 210, 151, 22))
        self.l_pg_excluir_celular.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_email = QLabel(self.frame_5)
        self.l_pg_excluir_email.setObjectName('l_pg_excluir_email')
        self.l_pg_excluir_email.setGeometry(QRect(1, 260, 113, 22))
        self.l_pg_excluir_email.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_cidade = QLabel(self.frame_5)
        self.l_pg_excluir_cidade.setObjectName('l_pg_excluir_cidade')
        self.l_pg_excluir_cidade.setGeometry(QRect(120, 260, 101, 22))
        self.l_pg_excluir_cidade.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_bairro = QLabel(self.frame_5)
        self.l_pg_excluir_bairro.setObjectName('l_pg_excluir_bairro')
        self.l_pg_excluir_bairro.setGeometry(QRect(230, 260, 121, 22))
        self.l_pg_excluir_bairro.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_cep = QLabel(self.frame_5)
        self.l_pg_excluir_cep.setObjectName('l_pg_excluir_cep')
        self.l_pg_excluir_cep.setGeometry(QRect(1, 310, 181, 22))
        self.l_pg_excluir_cep.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_formacao = QLabel(self.frame_5)
        self.l_pg_excluir_formacao.setObjectName('l_pg_excluir_formacao')
        self.l_pg_excluir_formacao.setGeometry(QRect(190, 310, 161, 22))
        self.l_pg_excluir_formacao.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_salario = QLabel(self.frame_5)
        self.l_pg_excluir_salario.setObjectName('l_pg_excluir_salario')
        self.l_pg_excluir_salario.setGeometry(QRect(20, 350, 151, 22))
        self.l_pg_excluir_salario.setAlignment(Qt.AlignCenter)
        self.l_pg_excluir_pagamento = QLabel(self.frame_5)
        self.l_pg_excluir_pagamento.setObjectName('l_pg_excluir_pagamento')
        self.l_pg_excluir_pagamento.setGeometry(QRect(190, 350, 151, 22))
        self.l_pg_excluir_pagamento.setAlignment(Qt.AlignCenter)
        self.pb_pg_excluir_pesquisar = QPushButton(self.frame_5)
        self.pb_pg_excluir_pesquisar.setObjectName('pb_pg_excluir_pesquisar')
        self.pb_pg_excluir_pesquisar.setGeometry(QRect(143, 440, 75, 24))
        self.le_pg_excluir_pesquisar = QLineEdit(self.frame_5)
        self.le_pg_excluir_pesquisar.setObjectName('le_pg_excluir_pesquisar')
        self.le_pg_excluir_pesquisar.setGeometry(QRect(105, 410, 151, 22))
        self.le_pg_excluir_pesquisar.setMaxLength(11)
        self.le_pg_excluir_pesquisar.setAlignment(Qt.AlignCenter)
        self.pb_pg_excluir_excluir_dados = QPushButton(self.frame_5)
        self.pb_pg_excluir_excluir_dados.setObjectName(
            'pb_pg_excluir_excluir_dados'
        )
        self.pb_pg_excluir_excluir_dados.setGeometry(QRect(143, 470, 75, 24))
        self.l_pg_excluir_matricula = QLabel(self.frame_5)
        self.l_pg_excluir_matricula.setObjectName('l_pg_excluir_matricula')
        self.l_pg_excluir_matricula.setGeometry(QRect(90, 380, 181, 22))
        self.l_pg_excluir_matricula.setStyleSheet('')
        self.l_pg_excluir_matricula.setAlignment(Qt.AlignCenter)
        self.label_67.raise_()
        self.label_68.raise_()
        self.label_64.raise_()
        self.label_65.raise_()
        self.l_pg_excluir_foto.raise_()
        self.label_66.raise_()
        self.l_pg_excluir_nome.raise_()
        self.l_pg_excluir_nascimento.raise_()
        self.l_pg_excluir_cpf.raise_()
        self.l_pg_excluir_celular.raise_()
        self.l_pg_excluir_email.raise_()
        self.l_pg_excluir_cidade.raise_()
        self.l_pg_excluir_bairro.raise_()
        self.l_pg_excluir_cep.raise_()
        self.l_pg_excluir_formacao.raise_()
        self.l_pg_excluir_salario.raise_()
        self.l_pg_excluir_pagamento.raise_()
        self.pb_pg_excluir_pesquisar.raise_()
        self.le_pg_excluir_pesquisar.raise_()
        self.pb_pg_excluir_excluir_dados.raise_()
        self.l_pg_excluir_matricula.raise_()
        self.label_14 = QLabel(self.pagina_excluir)
        self.label_14.setObjectName('label_14')
        self.label_14.setGeometry(QRect(443, 0, 4, 10))
        self.label_14.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.stackedWidget.addWidget(self.pagina_excluir)
        self.page = QWidget()
        self.page.setObjectName('page')
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName('frame_6')
        self.frame_6.setGeometry(QRect(219, 10, 361, 521))
        self.frame_6.setStyleSheet(
            'QFrame{\n'
            'background-color: rgb(53, 58, 75);\n'
            'border-radius: 30px;\n'
            '}\n'
            'QFrame::hover{\n'
            '	border: 1px solid  rgb(173, 82, 135);\n'
            '	color: rgb(189, 147, 249);\n'
            '}\n'
            'QLabel{\n'
            '	background-color: qlineargradient(spread:pad, x1:0, y1:0.42, x2:0, y2:1, stop:0 rgba(53, 58, 75, 255), stop:0.994318 rgba(173, 82, 135, 118));\n'
            '}'
        )
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pb_pg_pagamentos_pagar = QPushButton(self.frame_6)
        self.pb_pg_pagamentos_pagar.setObjectName('pb_pg_pagamentos_pagar')
        self.pb_pg_pagamentos_pagar.setGeometry(QRect(143, 290, 75, 24))
        self.le_pg_pagamentos = QLineEdit(self.frame_6)
        self.le_pg_pagamentos.setObjectName('le_pg_pagamentos')
        self.le_pg_pagamentos.setGeometry(QRect(95, 210, 171, 22))
        self.le_pg_pagamentos.setMaxLength(11)
        self.le_pg_pagamentos.setAlignment(Qt.AlignCenter)
        self.sb_pg_pagamentos_valor = QSpinBox(self.frame_6)
        self.sb_pg_pagamentos_valor.setObjectName('sb_pg_pagamentos_valor')
        self.sb_pg_pagamentos_valor.setGeometry(QRect(95, 250, 171, 22))
        self.sb_pg_pagamentos_valor.setAlignment(Qt.AlignCenter)
        self.sb_pg_pagamentos_valor.setButtonSymbols(
            QAbstractSpinBox.NoButtons
        )
        self.sb_pg_pagamentos_valor.setAccelerated(True)
        self.sb_pg_pagamentos_valor.setMaximum(999999)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName('label_2')
        self.label_2.setGeometry(QRect(263, 0, 4, 10))
        self.label_2.setStyleSheet('background-color: rgb(173, 82, 135);')
        self.stackedWidget.addWidget(self.page)

        self.verticalLayout.addWidget(self.frame_2)

        Professor.setCentralWidget(self.centralwidget)

        self.retranslateUi(Professor)

        self.stackedWidget.setCurrentIndex(0)
        self.combobox_novo_formacao.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(Professor)

    # setupUi

    def retranslateUi(self, Professor):
        Professor.setWindowTitle(
            QCoreApplication.translate('Professor', 'Professor', None)
        )
        self.pb_pagina_pagamento.setText('')
        self.pb_pagina_ad_prof.setText('')
        self.pb_pagina_excluir_prof.setText('')
        self.pb_pagina_pesquisar_prof.setText('')
        self.label_24.setText('')
        self.label_25.setText('')
        self.le_pg_novo_nome.setPlaceholderText(
            QCoreApplication.translate('Professor', 'Nome', None)
        )
        # if QT_CONFIG(tooltip)
        self.de_novo_data_nascimento.setToolTip(
            QCoreApplication.translate('Professor', 'Data nascimento', None)
        )
        # endif // QT_CONFIG(tooltip)
        self.le_pg_novo_cpf.setInputMask('')
        self.le_pg_novo_cpf.setPlaceholderText(
            QCoreApplication.translate('Professor', 'CPF', None)
        )
        self.le_pg_novo_celular.setInputMask('')
        self.le_pg_novo_celular.setPlaceholderText(
            QCoreApplication.translate(
                'Professor', 'N\u00famero do celular', None
            )
        )
        self.checkbox_pg_novo_whatsapp.setText(
            QCoreApplication.translate('Professor', 'Whatsapp', None)
        )
        self.le_pg_novo_email.setPlaceholderText(
            QCoreApplication.translate('Professor', 'E-mail', None)
        )
        self.le_pg_novo_cidade.setPlaceholderText(
            QCoreApplication.translate('Professor', 'Cidade', None)
        )
        self.le_pg_novo_bairro.setPlaceholderText(
            QCoreApplication.translate('Professor', 'Bairro', None)
        )
        self.le_pg_novo_cep.setPlaceholderText(
            QCoreApplication.translate('Professor', 'CEP', None)
        )
        self.combobox_novo_formacao.setItemText(
            0, QCoreApplication.translate('Professor', 'Bacharelado', None)
        )
        self.combobox_novo_formacao.setItemText(
            1, QCoreApplication.translate('Professor', 'Licenciatura', None)
        )

        self.combobox_novo_formacao.setPlaceholderText(
            QCoreApplication.translate(
                'Professor', 'Forma\u00e7\u00e3o acad\u00eamica', None
            )
        )
        self.l_pg_novo_ad_foto.setText('')
        self.label_26.setText('')
        self.label_27.setText('')
        self.label_28.setText('')
        self.sb_pg_novo_salario.setSuffix('')
        self.sb_pg_novo_salario.setPrefix(
            QCoreApplication.translate('Professor', 'Sal\u00e1rio: ', None)
        )
        self.sb_pg_novo_pagamento.setPrefix(
            QCoreApplication.translate('Professor', 'Dia do pagamento: ', None)
        )
        self.pb_pg_novo_salvar_dados.setText(
            QCoreApplication.translate('Professor', 'Salvar', None)
        )
        # if QT_CONFIG(tooltip)
        self.pb_novo_ad_foto.setToolTip(
            QCoreApplication.translate(
                'Professor', 'Click para adicionar uma foto', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.pb_novo_ad_foto.setText('')
        self.label.setText('')
        self.label_59.setText('')
        self.label_60.setText('')
        self.l_pg_pesquisar_foto.setText('')
        self.label_61.setText('')
        self.label_62.setText('')
        self.label_63.setText('')
        self.l_pg_pesquisar_nome.setText('')
        self.l_pg_pesquisar_nascimento.setText('')
        self.l_pg_pesquisar_cpf.setText('')
        self.l_pg_pesquisar_celular.setText('')
        self.l_pg_pesquisar_email.setText('')
        self.l_pg_pesquisar_cidade.setText('')
        self.l_pg_pesquisar_bairro.setText('')
        self.l_pg_pesquisar_cep.setText('')
        self.l_pg_pesquisar_formacao.setText('')
        self.l_pg_pesquisar_salario.setText('')
        self.l_pg_pesquisar_pagamento.setText('')
        self.pb_pg_pesquisar.setText(
            QCoreApplication.translate('Professor', 'Pesquisar', None)
        )
        self.le_pg_pesquisar.setPlaceholderText(
            QCoreApplication.translate('Professor', 'Matr\u00edcula/CPF', None)
        )
        self.l_pg_pesquisar_matricula.setText('')
        self.label_13.setText('')
        self.label_64.setText('')
        self.label_65.setText('')
        self.l_pg_excluir_foto.setText('')
        self.label_66.setText('')
        self.label_67.setText('')
        self.label_68.setText('')
        self.l_pg_excluir_nome.setText('')
        self.l_pg_excluir_nascimento.setText('')
        self.l_pg_excluir_cpf.setText('')
        self.l_pg_excluir_celular.setText('')
        self.l_pg_excluir_email.setText('')
        self.l_pg_excluir_cidade.setText('')
        self.l_pg_excluir_bairro.setText('')
        self.l_pg_excluir_cep.setText('')
        self.l_pg_excluir_formacao.setText('')
        self.l_pg_excluir_salario.setText('')
        self.l_pg_excluir_pagamento.setText('')
        self.pb_pg_excluir_pesquisar.setText(
            QCoreApplication.translate('Professor', 'Pesquisar', None)
        )
        self.le_pg_excluir_pesquisar.setPlaceholderText(
            QCoreApplication.translate('Professor', 'Matr\u00edcula/CPF', None)
        )
        self.pb_pg_excluir_excluir_dados.setText(
            QCoreApplication.translate('Professor', 'Excluir', None)
        )
        self.l_pg_excluir_matricula.setText('')
        self.label_14.setText('')
        self.pb_pg_pagamentos_pagar.setText(
            QCoreApplication.translate('Professor', 'Pagar', None)
        )
        self.le_pg_pagamentos.setPlaceholderText(
            QCoreApplication.translate('Professor', 'Matr\u00edcula/CPF', None)
        )
        self.sb_pg_pagamentos_valor.setPrefix(
            QCoreApplication.translate(
                'Professor', 'Valor do pagamento: ', None
            )
        )
        self.label_2.setText('')

    # retranslateUi
