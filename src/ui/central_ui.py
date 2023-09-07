# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'central.ui'
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
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from .img_rc import *


class Ui_JanelaCentral(object):
    def setupUi(self, JanelaCentral):
        if not JanelaCentral.objectName():
            JanelaCentral.setObjectName('JanelaCentral')
        JanelaCentral.resize(800, 600)
        icon = QIcon()
        icon.addFile(
            ':/icon/icon/principal.ico', QSize(), QIcon.Normal, QIcon.Off
        )
        JanelaCentral.setWindowIcon(icon)
        JanelaCentral.setStyleSheet('')
        JanelaCentral.setDockOptions(
            QMainWindow.AllowTabbedDocks | QMainWindow.AnimatedDocks
        )
        self.centralwidget = QWidget(JanelaCentral)
        self.centralwidget.setObjectName('centralwidget')
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.f_opcoes_vertical = QFrame(self.centralwidget)
        self.f_opcoes_vertical.setObjectName('f_opcoes_vertical')
        self.f_opcoes_vertical.setMinimumSize(QSize(30, 0))
        self.f_opcoes_vertical.setMaximumSize(QSize(30, 16777215))
        self.f_opcoes_vertical.setStyleSheet(
            'QFrame{\n' '	background-color: rgb(40, 42, 54);\n' '}'
        )
        self.f_opcoes_vertical.setFrameShape(QFrame.NoFrame)
        self.f_opcoes_vertical.setFrameShadow(QFrame.Raised)
        self.f_opcoes_vertical.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.f_opcoes_vertical)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_pagina_login = QPushButton(self.f_opcoes_vertical)
        self.pb_pagina_login.setObjectName('pb_pagina_login')
        self.pb_pagina_login.setMinimumSize(QSize(10, 0))
        self.pb_pagina_login.setStyleSheet(
            'QPushButton{\n'
            '	image: url(:/central/img/logar.png);\n'
            '	background-color: rgba(255, 255, 255, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	image: url(:/central/img/logar-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	image: url(:/central/img/logar-press.png);\n'
            '}'
        )

        self.verticalLayout_2.addWidget(self.pb_pagina_login)

        self.verticalSpacer_2 = QSpacerItem(
            30, 200, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pb_pagina_graficos = QPushButton(self.f_opcoes_vertical)
        self.pb_pagina_graficos.setObjectName('pb_pagina_graficos')
        self.pb_pagina_graficos.setStyleSheet(
            'QPushButton{\n'
            '	image: url(:/grobal/img/grafico.png);\n'
            '	background-color: rgba(255, 255, 255, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	image: url(:/grobal/img/grafico-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	image: url(:/grobal/img/grafico-press.png);\n'
            '}'
        )

        self.verticalLayout_2.addWidget(self.pb_pagina_graficos)

        self.verticalSpacer_3 = QSpacerItem(
            20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.pb_pagina_cadastro = QPushButton(self.f_opcoes_vertical)
        self.pb_pagina_cadastro.setObjectName('pb_pagina_cadastro')
        self.pb_pagina_cadastro.setStyleSheet(
            'QPushButton{\n'
            '	image: url(:/central/img/cadastro.png);\n'
            '	background-color: rgba(255, 255, 255, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	image: url(:/central/img/cadastro-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	image: url(:/central/img/cadastro-press.png);\n'
            '}'
        )

        self.verticalLayout_2.addWidget(self.pb_pagina_cadastro)

        self.verticalSpacer = QSpacerItem(
            20, 549, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pb_pagina_configuracao = QPushButton(self.f_opcoes_vertical)
        self.pb_pagina_configuracao.setObjectName('pb_pagina_configuracao')
        self.pb_pagina_configuracao.setStyleSheet(
            'QPushButton{\n'
            '	image: url(:/grobal/img/config.png);\n'
            '	background-color: rgba(255, 255, 255, 0);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	image: url(:/grobal/img/config-hover.png);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	image: url(:/grobal/img/config-press.png);\n'
            '}'
        )

        self.verticalLayout_2.addWidget(self.pb_pagina_configuracao)

        self.horizontalLayout.addWidget(self.f_opcoes_vertical)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName('frame')
        self.frame.setStyleSheet('')
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.f_principal = QFrame(self.frame)
        self.f_principal.setObjectName('f_principal')
        self.f_principal.setStyleSheet('')
        self.f_principal.setFrameShape(QFrame.NoFrame)
        self.f_principal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f_principal)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.f_principal)
        self.stackedWidget.setObjectName('stackedWidget')
        self.stackedWidget.setStyleSheet(
            'QStackedWidget{\n'
            '	background-color: rgb(68, 71, 90);\n'
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
        self.page = QWidget()
        self.page.setObjectName('page')
        self.horizontalLayout_5 = QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName('horizontalLayout_5')
        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.l_link_github = QLabel(self.page)
        self.l_link_github.setObjectName('l_link_github')
        self.l_link_github.setStyleSheet(
            'QLabel{\n' '	font: 700 48pt "Segoe Script";\n' '}'
        )
        self.l_link_github.setAlignment(Qt.AlignCenter)
        self.l_link_github.setOpenExternalLinks(True)

        self.horizontalLayout_5.addWidget(self.l_link_github, 0, Qt.AlignLeft)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName('page_3')
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName('page_2')
        self.page_2.setStyleSheet('')
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName('horizontalLayout_4')
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(
            200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)

        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName('frame_2')
        self.frame_2.setMaximumSize(QSize(300, 300))
        self.frame_2.setStyleSheet(
            'QFrame{\n'
            '	background-color: rgb(22, 33, 62);\n'
            '	border: 2px solid  rgb(173, 82, 135) ;\n'
            '	border-radius: 50%;\n'
            '}'
        )
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.le_usuario = QLineEdit(self.frame_2)
        self.le_usuario.setObjectName('le_usuario')
        self.le_usuario.setGeometry(QRect(75, 100, 150, 22))
        self.le_usuario.setAlignment(Qt.AlignCenter)
        self.le_senha = QLineEdit(self.frame_2)
        self.le_senha.setObjectName('le_senha')
        self.le_senha.setGeometry(QRect(75, 150, 150, 22))
        self.le_senha.setAlignment(Qt.AlignCenter)
        self.pb_confirmar_usuario = QPushButton(self.frame_2)
        self.pb_confirmar_usuario.setObjectName('pb_confirmar_usuario')
        self.pb_confirmar_usuario.setGeometry(QRect(112, 200, 75, 24))

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.horizontalSpacer_13 = QSpacerItem(
            200, 30, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_13)

        self.stackedWidget.addWidget(self.page_2)
        self.page1 = QWidget()
        self.page1.setObjectName('page1')
        self.gridLayout_2 = QGridLayout(self.page1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName('gridLayout_2')
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_professor = QPushButton(self.page1)
        self.pb_professor.setObjectName('pb_professor')
        self.pb_professor.setMinimumSize(QSize(100, 50))
        self.pb_professor.setMaximumSize(QSize(100, 50))
        self.pb_professor.setStyleSheet(
            'QPushButton{\n'
            '	border-image: url(:/central/img/professor.png);\n'
            '	background-color: rgba(255, 255, 255, 0);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border-image: url(:/central/img/professor-hover.png);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	border-image: url(:/central/img/professor-press.png);\n'
            '}'
        )

        self.gridLayout_2.addWidget(self.pb_professor, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.pb_aluno = QPushButton(self.page1)
        self.pb_aluno.setObjectName('pb_aluno')
        self.pb_aluno.setMinimumSize(QSize(100, 50))
        self.pb_aluno.setMaximumSize(QSize(100, 50))
        self.pb_aluno.setStyleSheet(
            'QPushButton{\n'
            '	border-image: url(:/central/img/aluno.png);\n'
            '	background-color: rgba(255, 255, 255, 0);\n'
            '}\n'
            'QPushButton::pressed{\n'
            '	border-image: url(:/central/img/aluno-hover.png);\n'
            '}\n'
            'QPushButton::hover{\n'
            '	border-image: url(:/central/img/aluno-press.png);\n'
            '}'
        )

        self.gridLayout_2.addWidget(self.pb_aluno, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.page1)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.verticalLayout.addWidget(self.f_principal)

        self.f_status_horizontal = QFrame(self.frame)
        self.f_status_horizontal.setObjectName('f_status_horizontal')
        self.f_status_horizontal.setMinimumSize(QSize(0, 30))
        self.f_status_horizontal.setMaximumSize(QSize(16777215, 30))
        self.f_status_horizontal.setStyleSheet(
            'QFrame{\n'
            '	background-color: rgb(40, 42, 54);\n'
            '}\n'
            'QLabel{\n'
            '	font: 700 italic 10pt "Verdana";\n'
            '	color: rgb(98, 114, 164);\n'
            '}\n'
            'QProgressBar {\n'
            '    border: 2px solid rgb(68, 71, 90);\n'
            '    border-radius: 5px;\n'
            '}\n'
            'QProgressBar::chunk {\n'
            '	background-color: rgb(208, 99, 162);\n'
            '    border-radius: 2px;\n'
            '    width: 5px;\n'
            '    margin: 0.5px;\n'
            '}'
        )
        self.f_status_horizontal.setFrameShape(QFrame.NoFrame)
        self.f_status_horizontal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.f_status_horizontal)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(
            15, 10, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.label_3 = QLabel(self.f_status_horizontal)
        self.label_3.setObjectName('label_3')
        self.label_3.setOpenExternalLinks(True)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.l_status_login = QLabel(self.f_status_horizontal)
        self.l_status_login.setObjectName('l_status_login')
        self.l_status_login.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.l_status_login)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.f_status_horizontal)
        self.label_2.setObjectName('label_2')
        font = QFont()
        font.setFamilies(['Verdana'])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(
            10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.progress_bar_memoria = QProgressBar(self.f_status_horizontal)
        self.progress_bar_memoria.setObjectName('progress_bar_memoria')
        self.progress_bar_memoria.setMaximumSize(QSize(50, 30))
        font1 = QFont()
        font1.setFamilies(['Arial Black'])
        font1.setPointSize(10)
        font1.setBold(True)
        self.progress_bar_memoria.setFont(font1)
        self.progress_bar_memoria.setValue(0)
        self.progress_bar_memoria.setAlignment(Qt.AlignCenter)
        self.progress_bar_memoria.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.progress_bar_memoria)

        self.horizontalSpacer_4 = QSpacerItem(
            30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.f_status_horizontal)
        self.label.setObjectName('label')
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(
            10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.progress_bar_armazenamento = QProgressBar(
            self.f_status_horizontal
        )
        self.progress_bar_armazenamento.setObjectName(
            'progress_bar_armazenamento'
        )
        self.progress_bar_armazenamento.setMinimumSize(QSize(0, 30))
        self.progress_bar_armazenamento.setMaximumSize(QSize(50, 30))
        self.progress_bar_armazenamento.setFont(font1)
        self.progress_bar_armazenamento.setValue(0)
        self.progress_bar_armazenamento.setAlignment(Qt.AlignCenter)
        self.progress_bar_armazenamento.setOrientation(Qt.Horizontal)
        self.progress_bar_armazenamento.setTextDirection(
            QProgressBar.TopToBottom
        )

        self.horizontalLayout_3.addWidget(self.progress_bar_armazenamento)

        self.verticalLayout.addWidget(self.f_status_horizontal)

        self.horizontalLayout.addWidget(self.frame)

        JanelaCentral.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaCentral)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(JanelaCentral)

    # setupUi

    def retranslateUi(self, JanelaCentral):
        JanelaCentral.setWindowTitle(
            QCoreApplication.translate('JanelaCentral', 'VGymSystem', None)
        )
        self.pb_pagina_login.setText('')
        self.pb_pagina_graficos.setText('')
        self.pb_pagina_cadastro.setText('')
        self.pb_pagina_configuracao.setText('')
        self.l_link_github.setText(
            QCoreApplication.translate(
                'JanelaCentral',
                '<html><head/><body><p><a href="https://github.com/Vi-n1/VGymSystem"><span style=" text-decoration: underline; color:#d063a2;">Developed by Vi-n1</span></a></p></body></html>',
                None,
            )
        )
        self.le_usuario.setPlaceholderText(
            QCoreApplication.translate('JanelaCentral', 'Us\u00faario', None)
        )
        self.le_senha.setPlaceholderText(
            QCoreApplication.translate('JanelaCentral', 'Senha', None)
        )
        self.pb_confirmar_usuario.setText(
            QCoreApplication.translate('JanelaCentral', 'Confirmar', None)
        )
        self.pb_professor.setText('')
        self.pb_aluno.setText('')
        self.label_3.setText(
            QCoreApplication.translate(
                'JanelaCentral',
                '<html><head/><body><p><a href="https://icons8.com.br/"><span style=" text-decoration: underline; color:#d063a2;">Icons by: icons8</span></a></p></body></html>',
                None,
            )
        )
        self.l_status_login.setText(
            QCoreApplication.translate('JanelaCentral', '{}', None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                'JanelaCentral', 'Mem\u00f3ria  ->', None
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                'JanelaCentral', 'Armazenamento ->', None
            )
        )
        self.progress_bar_armazenamento.setFormat(
            QCoreApplication.translate('JanelaCentral', '%p%', None)
        )

    # retranslateUi
