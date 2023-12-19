from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(532, 313)
        
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
        
        self.pushButtonT = QtWidgets.QPushButton(Dialog)
        self.pushButtonT.setGeometry(QtCore.QRect(50, 130, 431, 61))
        self.pushButtonT.setObjectName("pushButtonT")
        self.pushButtonT.setText("Tradicional")
        
        self.pushButtonC = QtWidgets.QPushButton(Dialog)
        self.pushButtonC.setGeometry(QtCore.QRect(50, 200, 431, 61))
        self.pushButtonC.setObjectName("pushButtonC")
        self.pushButtonC.setText("Científica")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 281, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("INICIAR CALCULADORA")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
