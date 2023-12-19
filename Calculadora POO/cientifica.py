from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 369)
        
        style_sheet = """
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-family: Arial;
                font-size: 16px;
            }
            
            QLabel {
                font-family: Arial;
                font-size: 24px;
                color: #333333;
            }
        """
        
        Dialog.setStyleSheet(style_sheet)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 290, 401, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 611, 205))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 0, 5, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout.addWidget(self.pushButton_30, 3, 6, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 3, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout.addWidget(self.pushButton_27, 1, 6, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 1, 4, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout.addWidget(self.pushButton_29, 2, 6, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setDefault(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 4, 6, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 0, 2, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 0, 4, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout.addWidget(self.pushButton_24, 3, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 4, 3, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_31, 4, 5, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 2, 4, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 2, 5, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 3, 4, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 4, 2, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 0, 3, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout.addWidget(self.pushButton_28, 4, 4, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_26, 0, 6, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 1, 5, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 3, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(Dialog)
        self.pushButton_25.setGeometry(QtCore.QRect(10, 290, 75, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_21.setText(_translate("Dialog", "sin"))
        self.pushButton_30.setText(_translate("Dialog", "e"))
        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_27.setText(_translate("Dialog", ")"))
        self.pushButton_15.setText(_translate("Dialog", "+"))
        self.pushButton_8.setText(_translate("Dialog", "+/-"))
        self.pushButton_3.setText(_translate("Dialog", "9"))
        self.pushButton_9.setText(_translate("Dialog", "2"))
        self.pushButton_29.setText(_translate("Dialog", "pi"))
        self.pushButton_17.setText(_translate("Dialog", "C"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_13.setText(_translate("Dialog", "="))
        self.pushButton_19.setText(_translate("Dialog", "sqrt"))
        self.pushButton_20.setText(_translate("Dialog", "/"))
        self.pushButton_24.setText(_translate("Dialog", "^"))
        self.pushButton.setText(_translate("Dialog", "7"))
        self.pushButton_11.setText(_translate("Dialog", "."))
        self.pushButton_31.setText(_translate("Dialog", "ln"))
        self.pushButton_14.setText(_translate("Dialog", "-"))
        self.pushButton_23.setText(_translate("Dialog", "tan"))
        self.pushButton_16.setText(_translate("Dialog", "*"))
        self.pushButton_7.setText(_translate("Dialog", "1"))
        self.pushButton_10.setText(_translate("Dialog", "0"))
        self.pushButton_18.setText(_translate("Dialog", "<<"))
        self.pushButton_28.setText(_translate("Dialog", "!"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_2.setText(_translate("Dialog", "8"))
        self.pushButton_26.setText(_translate("Dialog", "("))
        self.pushButton_22.setText(_translate("Dialog", "cos"))
        self.pushButton_12.setText(_translate("Dialog", "3"))
        self.pushButton_25.setText(_translate("Dialog", "Voltar"))
        self.label.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
