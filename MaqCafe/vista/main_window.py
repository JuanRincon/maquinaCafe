# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ListCoffeeForm(object):
    def setupUi(self, ListCoffeeForm):
        if not ListCoffeeForm.objectName():
            ListCoffeeForm.setObjectName(u"ListCoffeeForm")
        ListCoffeeForm.resize(980, 550)
        self.buttonsFrame = QFrame(ListCoffeeForm)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(10, 10, 941, 80))
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.oppenCoffeeButton = QPushButton(self.buttonsFrame)
        self.oppenCoffeeButton.setObjectName(u"oppenCoffeeButton")
        self.oppenCoffeeButton.setGeometry(QRect(20, 10, 71, 51))
        self.oppenCoffeeButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/icons/gaming.png", QSize(), QIcon.Normal, QIcon.Off)
        self.oppenCoffeeButton.setIcon(icon)
        self.oppenCoffeeButton.setIconSize(QSize(50, 50))
        self.oppenCoffeeButton.setFlat(True)
        self.label = QLabel(self.buttonsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 91, 21))
        self.oppen_new_button = QPushButton(self.buttonsFrame)
        self.oppen_new_button.setObjectName(u"oppen_new_button")
        self.oppen_new_button.setGeometry(QRect(140, 10, 71, 51))
        self.oppen_new_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/avatar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.oppen_new_button.setIcon(icon1)
        self.oppen_new_button.setIconSize(QSize(50, 50))
        self.oppen_new_button.setFlat(True)
        self.label_2 = QLabel(self.buttonsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 60, 91, 21))
        self.oppen_edit_button = QPushButton(self.buttonsFrame)
        self.oppen_edit_button.setObjectName(u"oppen_edit_button")
        self.oppen_edit_button.setGeometry(QRect(260, 10, 71, 51))
        self.oppen_edit_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/avatar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.oppen_edit_button.setIcon(icon2)
        self.oppen_edit_button.setIconSize(QSize(50, 50))
        self.oppen_edit_button.setFlat(True)
        self.label_3 = QLabel(self.buttonsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 60, 111, 21))
        self.delete_button = QPushButton(self.buttonsFrame)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(390, 10, 71, 51))
        self.delete_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../assets/icons/avatar (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon3)
        self.delete_button.setIconSize(QSize(50, 50))
        self.delete_button.setFlat(True)
        self.label_4 = QLabel(self.buttonsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 60, 111, 21))
        self.frame = QFrame(ListCoffeeForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 941, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 10, 71, 16))
        self.MenucomboBox = QComboBox(self.frame)
        self.MenucomboBox.setObjectName(u"MenucomboBox")
        self.MenucomboBox.setGeometry(QRect(60, 10, 161, 22))
        self.parametrolineEdit = QLineEdit(self.frame)
        self.parametrolineEdit.setObjectName(u"parametrolineEdit")
        self.parametrolineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(660, 10, 131, 25))
        icon4 = QIcon()
        icon4.addFile(u"../assets/icons/coffee-cup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon4)
        self.refreshButton = QPushButton(self.frame)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(800, 10, 131, 25))
        icon5 = QIcon()
        icon5.addFile(u"../assets/icons/refresh-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon5)
        self.listaventastable = QTableWidget(ListCoffeeForm)
        self.listaventastable.setObjectName(u"listaventastable")
        self.listaventastable.setGeometry(QRect(10, 160, 941, 341))
        self.label_6 = QLabel(ListCoffeeForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 520, 121, 16))
        self.label_7 = QLabel(ListCoffeeForm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 520, 47, 13))

        self.retranslateUi(ListCoffeeForm)

        QMetaObject.connectSlotsByName(ListCoffeeForm)
    # setupUi

    def retranslateUi(self, ListCoffeeForm):
        ListCoffeeForm.setWindowTitle(QCoreApplication.translate("ListCoffeeForm", u"Caf\u00e9 Pokemon \u2615", None))
        self.oppenCoffeeButton.setText("")
        self.label.setText(QCoreApplication.translate("ListCoffeeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Informe</span></p></body></html>", None))
        self.oppen_new_button.setText("")
        self.label_2.setText(QCoreApplication.translate("ListCoffeeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Comprar caf\u00e9</span></p></body></html>", None))
        self.oppen_edit_button.setText("")
        self.label_3.setText(QCoreApplication.translate("ListCoffeeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Actualizar compra</span></p></body></html>", None))
        self.delete_button.setText("")
        self.label_4.setText(QCoreApplication.translate("ListCoffeeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar compra</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("ListCoffeeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Men\u00fa:</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.searchButton.setText(QCoreApplication.translate("ListCoffeeForm", u"BUSCAR", None))
        self.refreshButton.setText(QCoreApplication.translate("ListCoffeeForm", u"REFRESCAR", None))
        self.label_6.setText(QCoreApplication.translate("ListCoffeeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">cantidad de ventas: </span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("ListCoffeeForm", u"#", None))
    # retranslateUi

