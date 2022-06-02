# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'venta_cafe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Venta_cafe(object):
    def setupUi(self, Venta_cafe):
        if not Venta_cafe.objectName():
            Venta_cafe.setObjectName(u"Venta_cafe")
        Venta_cafe.resize(405, 472)
        self.label = QLabel(Venta_cafe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(Venta_cafe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.lineEdit = QLineEdit(Venta_cafe)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 80, 141, 20))
        self.label_3 = QLabel(Venta_cafe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 60, 61, 13))
        self.label_4 = QLabel(Venta_cafe)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 101, 16))
        self.lineEdit_2 = QLineEdit(Venta_cafe)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 150, 113, 20))
        self.pushButton = QPushButton(Venta_cafe)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 240, 351, 221))
        icon = QIcon()
        icon.addFile(u"../assets/icons/1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(400, 400))
        self.spinBox = QSpinBox(Venta_cafe)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(210, 80, 111, 22))
        self.pushButton_2 = QPushButton(Venta_cafe)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 150, 111, 23))
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/confirmar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.retranslateUi(Venta_cafe)

        QMetaObject.connectSlotsByName(Venta_cafe)
    # setupUi

    def retranslateUi(self, Venta_cafe):
        Venta_cafe.setWindowTitle(QCoreApplication.translate("Venta_cafe", u"Venta", None))
        self.label.setText(QCoreApplication.translate("Venta_cafe", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">NUEVA VENTA</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Venta_cafe", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Opci\u00f3n</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Venta_cafe", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Az\u00facar</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Venta_cafe", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Insertar dinero</span></p></body></html>", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Venta_cafe", u"HACER PEDIDO", None))
    # retranslateUi

