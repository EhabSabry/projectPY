# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_select_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from select import Ui_Form_9
from select2 import Ui_Form_11
from select3 import Ui_Form_12
from select4 import Ui_Form_14

class Ui_Form_10(object):
    def openWindow4(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_9()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow5(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_11()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow6(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_12()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow7(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_14()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form_10):
        Form_10.setObjectName("Form_10")
        Form_10.resize(1015, 797)
        self.pushButton_32 = QtWidgets.QPushButton(Form_10,clicked = lambda: self.openWindow4())
        self.pushButton_32.setGeometry(QtCore.QRect(580, 120, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.pushButton_32.setDefault(True)
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_34 = QtWidgets.QPushButton(Form_10,clicked = lambda: self.openWindow6())
        self.pushButton_34.setGeometry(QtCore.QRect(590, 450, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.pushButton_34.setDefault(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(Form_10,clicked = lambda: self.openWindow7())
        self.pushButton_35.setGeometry(QtCore.QRect(70, 450, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.pushButton_35.setDefault(True)
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_33 = QtWidgets.QPushButton(Form_10,clicked = lambda: self.openWindow5())
        self.pushButton_33.setGeometry(QtCore.QRect(70, 120, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("Color: rgba(0, 7, 141, 1)\n"
"")
        self.pushButton_33.setDefault(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.label_1 = QtWidgets.QLabel(Form_10)
        self.label_1.setGeometry(QtCore.QRect(-90, 10, 851, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_1.setObjectName("label_1")

        self.retranslateUi(Form_10)
        QtCore.QMetaObject.connectSlotsByName(Form_10)

    def retranslateUi(self, Form_10):
        _translate = QtCore.QCoreApplication.translate
        Form_10.setWindowTitle(_translate("Form_10", "Form"))
        self.pushButton_32.setText(_translate("Form_10", "?????? ?????????? ???????????? ????????????"))
        self.pushButton_34.setText(_translate("Form_10", "?????? ?????????? ???????????? ??????????????"))
        self.pushButton_35.setText(_translate("Form_10", "?????? ?????????? ???????????? ??????????????"))
        self.pushButton_33.setText(_translate("Form_10", "?????? ?????????? ???????????? ??????????????"))
        self.label_1.setText(_translate("Form_10", "?????????? ?????? ??????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_10 = QtWidgets.QWidget()
    ui = Ui_Form_10()
    ui.setupUi(Form_10)
    Form_10.show()
    sys.exit(app.exec_())
