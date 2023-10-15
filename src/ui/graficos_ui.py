# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graficos.ui'
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
    QHBoxLayout,
    QLayout,
    QMainWindow,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from .img_rc import *


class Ui_Graficos(object):
    def setupUi(self, Graficos):
        if not Graficos.objectName():
            Graficos.setObjectName('Graficos')
        Graficos.resize(800, 600)
        Graficos.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(
            ':/grobal/img/grafico.png', QSize(), QIcon.Normal, QIcon.Off
        )
        Graficos.setWindowIcon(icon)
        self.centralwidget = QWidget(Graficos)
        self.centralwidget.setObjectName('centralwidget')
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setStyleSheet(
            'QFrame{\n' '	background-color: rgb(85, 85, 127);\n' '}'
        )
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName('frame_2')
        self.frame_2.setStyleSheet(
            'QChartView{\n'
            '	border-radius: 5%;\n'
            '	background-color: rgb(78, 78, 117);\n'
            '}'
        )
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 8, -1, -1)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName('verticalLayout_9')
        self.vl_grafico_pizza1 = QVBoxLayout()
        self.vl_grafico_pizza1.setObjectName('vl_grafico_pizza1')

        self.verticalLayout_9.addLayout(self.vl_grafico_pizza1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName('verticalLayout_10')
        self.vl_grafico_pizza2 = QVBoxLayout()
        self.vl_grafico_pizza2.setObjectName('vl_grafico_pizza2')

        self.verticalLayout_10.addLayout(self.vl_grafico_pizza2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_10)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.horizontalLayout_3.setContentsMargins(-1, 8, -1, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.vl_grafico_barra = QVBoxLayout()
        self.vl_grafico_barra.setObjectName('vl_grafico_barra')

        self.verticalLayout_3.addLayout(self.vl_grafico_barra)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout.addWidget(self.frame_2)

        Graficos.setCentralWidget(self.centralwidget)

        self.retranslateUi(Graficos)

        QMetaObject.connectSlotsByName(Graficos)

    # setupUi

    def retranslateUi(self, Graficos):
        Graficos.setWindowTitle(
            QCoreApplication.translate('Graficos', 'Dashboard', None)
        )

    # retranslateUi
