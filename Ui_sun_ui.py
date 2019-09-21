# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\python\sun_show\sun_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 698)
        self.pushButton_Enter = QtWidgets.QPushButton(Form)
        self.pushButton_Enter.setGeometry(QtCore.QRect(240, 180, 238, 101))
        self.pushButton_Enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Enter.setObjectName("pushButton_Enter")
        self.pushButton_Exit = QtWidgets.QPushButton(Form)
        self.pushButton_Exit.setGeometry(QtCore.QRect(80, 330, 239, 103))
        self.pushButton_Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Exit.setObjectName("pushButton_Exit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Enter.setText(_translate("Form", "Enter"))
        self.pushButton_Exit.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

