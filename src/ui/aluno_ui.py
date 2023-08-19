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
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName('pushButton')
        self.pushButton.setGeometry(QRect(10, 10, 50, 50))
        self.pushButton.setMinimumSize(QSize(50, 50))
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.setStyleSheet(
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
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName('pushButton_2')
        self.pushButton_2.setGeometry(QRect(90, 10, 50, 50))
        self.pushButton_2.setMinimumSize(QSize(50, 50))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        self.pushButton_2.setStyleSheet(
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
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName('pushButton_3')
        self.pushButton_3.setGeometry(QRect(170, 10, 50, 50))
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setStyleSheet(
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
            'QLabel{\n'
            '	color: rgb(255, 255, 255);\n'
            '	font: 10pt "Arial";\n'
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
            ''
        )
        self.page = QWidget()
        self.page.setObjectName('page')
        self.label = QLabel(self.page)
        self.label.setObjectName('label')
        self.label.setGeometry(QRect(0, 40, 271, 20))
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName('lineEdit')
        self.lineEdit.setGeometry(QRect(0, 60, 271, 22))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName('label_2')
        self.label_2.setGeometry(QRect(300, 40, 151, 20))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.dateEdit = QDateEdit(self.page)
        self.dateEdit.setObjectName('dateEdit')
        self.dateEdit.setGeometry(QRect(300, 60, 151, 22))
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName('label_3')
        self.label_3.setGeometry(QRect(480, 40, 131, 20))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName('lineEdit_2')
        self.lineEdit_2.setGeometry(QRect(480, 60, 131, 22))
        self.lineEdit_2.setMaxLength(14)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName('label_4')
        self.label_4.setGeometry(QRect(640, 40, 171, 20))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_3 = QLineEdit(self.page)
        self.lineEdit_3.setObjectName('lineEdit_3')
        self.lineEdit_3.setGeometry(QRect(640, 60, 171, 22))
        self.lineEdit_3.setText('()-')
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setEchoMode(QLineEdit.Normal)
        self.lineEdit_3.setCursorPosition(14)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.checkBox = QCheckBox(self.page)
        self.checkBox.setObjectName('checkBox')
        self.checkBox.setGeometry(QRect(830, 66, 81, 20))
        self.checkBox_2 = QCheckBox(self.page)
        self.checkBox_2.setObjectName('checkBox_2')
        self.checkBox_2.setGeometry(QRect(830, 46, 91, 20))
        self.pushButton_4 = QPushButton(self.page)
        self.pushButton_4.setObjectName('pushButton_4')
        self.pushButton_4.setGeometry(QRect(940, 20, 271, 211))
        self.pushButton_4.setStyleSheet(
            'QPushButton{\n'
            '	border-radius: 5%;\n'
            '	border: 2px solid  rgb(208, 99, 162);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            ''
        )
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName('label_5')
        self.label_5.setGeometry(QRect(940, 20, 271, 211))
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName('label_6')
        self.label_6.setGeometry(QRect(0, 110, 271, 20))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_4 = QLineEdit(self.page)
        self.lineEdit_4.setObjectName('lineEdit_4')
        self.lineEdit_4.setGeometry(QRect(0, 130, 271, 22))
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName('label_7')
        self.label_7.setGeometry(QRect(300, 110, 151, 20))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_5 = QLineEdit(self.page)
        self.lineEdit_5.setObjectName('lineEdit_5')
        self.lineEdit_5.setGeometry(QRect(300, 130, 151, 22))
        self.lineEdit_5.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName('label_8')
        self.label_8.setGeometry(QRect(480, 110, 131, 20))
        self.label_8.setAlignment(Qt.AlignCenter)
        self.lineEdit_6 = QLineEdit(self.page)
        self.lineEdit_6.setObjectName('lineEdit_6')
        self.lineEdit_6.setGeometry(QRect(480, 130, 131, 22))
        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName('label_9')
        self.label_9.setGeometry(QRect(640, 110, 171, 20))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.lineEdit_7 = QLineEdit(self.page)
        self.lineEdit_7.setObjectName('lineEdit_7')
        self.lineEdit_7.setGeometry(QRect(640, 130, 171, 22))
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName('label_10')
        self.label_10.setGeometry(QRect(0, 170, 271, 20))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.lineEdit_8 = QLineEdit(self.page)
        self.lineEdit_8.setObjectName('lineEdit_8')
        self.lineEdit_8.setGeometry(QRect(0, 190, 271, 22))
        self.groupBox = QGroupBox(self.page)
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
        self.lineEdit_9 = QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName('lineEdit_9')
        self.lineEdit_9.setGeometry(QRect(0, 60, 271, 22))
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
        self.dateEdit_2 = QDateEdit(self.groupBox)
        self.dateEdit_2.setObjectName('dateEdit_2')
        self.dateEdit_2.setGeometry(QRect(300, 60, 151, 22))
        self.dateEdit_2.setAlignment(Qt.AlignCenter)
        self.dateEdit_2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit_2.setCalendarPopup(True)
        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName('lineEdit_10')
        self.lineEdit_10.setGeometry(QRect(480, 60, 131, 22))
        self.lineEdit_11 = QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName('lineEdit_11')
        self.lineEdit_11.setGeometry(QRect(640, 60, 171, 22))
        self.lineEdit_12 = QLineEdit(self.groupBox)
        self.lineEdit_12.setObjectName('lineEdit_12')
        self.lineEdit_12.setGeometry(QRect(0, 130, 271, 22))
        self.lineEdit_13 = QLineEdit(self.groupBox)
        self.lineEdit_13.setObjectName('lineEdit_13')
        self.lineEdit_13.setGeometry(QRect(300, 130, 151, 22))
        self.lineEdit_14 = QLineEdit(self.groupBox)
        self.lineEdit_14.setObjectName('lineEdit_14')
        self.lineEdit_14.setGeometry(QRect(480, 130, 131, 22))
        self.lineEdit_15 = QLineEdit(self.groupBox)
        self.lineEdit_15.setObjectName('lineEdit_15')
        self.lineEdit_15.setGeometry(QRect(640, 130, 171, 22))
        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName('label_19')
        self.label_19.setGeometry(QRect(0, 170, 271, 20))
        self.label_19.setAlignment(Qt.AlignCenter)
        self.lineEdit_16 = QLineEdit(self.groupBox)
        self.lineEdit_16.setObjectName('lineEdit_16')
        self.lineEdit_16.setGeometry(QRect(0, 190, 271, 22))
        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName('label_20')
        self.label_20.setGeometry(QRect(940, 90, 271, 211))
        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName('pushButton_5')
        self.pushButton_5.setGeometry(QRect(940, 90, 271, 211))
        self.pushButton_5.setStyleSheet(
            'QPushButton{\n'
            '	border-radius: 5%;\n'
            '	border: 2px solid  rgb(208, 99, 162);\n'
            '	background-color: rgba(0, 0, 0, 0);\n'
            '}\n'
            ''
        )
        self.label_20.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.lineEdit_9.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.dateEdit_2.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_13.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_15.raise_()
        self.label_19.raise_()
        self.lineEdit_16.raise_()
        self.pushButton_5.raise_()
        self.stackedWidget.addWidget(self.page)
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.dateEdit.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.label_4.raise_()
        self.lineEdit_3.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.label_5.raise_()
        self.pushButton_4.raise_()
        self.label_6.raise_()
        self.lineEdit_4.raise_()
        self.label_7.raise_()
        self.lineEdit_5.raise_()
        self.label_8.raise_()
        self.lineEdit_6.raise_()
        self.label_9.raise_()
        self.lineEdit_7.raise_()
        self.label_10.raise_()
        self.lineEdit_8.raise_()
        self.groupBox.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName('page_2')
        self.stackedWidget.addWidget(self.page_2)
        JanelaAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaAluno)

        QMetaObject.connectSlotsByName(JanelaAluno)

    # setupUi

    def retranslateUi(self, JanelaAluno):
        JanelaAluno.setWindowTitle(
            QCoreApplication.translate('JanelaAluno', 'Aluno', None)
        )
        self.pushButton.setText('')
        self.pushButton_2.setText('')
        self.pushButton_3.setText('')
        self.label.setText(
            QCoreApplication.translate('JanelaAluno', 'Nome do aluno', None)
        )
        self.label_2.setText(
            QCoreApplication.translate('JanelaAluno', 'Data nascimento', None)
        )
        self.label_3.setText(
            QCoreApplication.translate('JanelaAluno', 'CPF', None)
        )
        self.lineEdit_2.setInputMask(
            QCoreApplication.translate('JanelaAluno', '999.999.999-99', None)
        )
        self.label_4.setText(
            QCoreApplication.translate('JanelaAluno', 'Celular', None)
        )
        self.lineEdit_3.setInputMask(
            QCoreApplication.translate('JanelaAluno', '(99)9999999-99', None)
        )
        self.checkBox.setText(
            QCoreApplication.translate('JanelaAluno', 'Whatsapp', None)
        )
        self.checkBox_2.setText(
            QCoreApplication.translate('JanelaAluno', 'Respons\u00e1vel', None)
        )
        self.pushButton_4.setText('')
        self.label_5.setText('')
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
            QCoreApplication.translate('JanelaAluno', 'TextLabel', None)
        )
        self.label_20.setText('')
        self.pushButton_5.setText('')

    # retranslateUi
