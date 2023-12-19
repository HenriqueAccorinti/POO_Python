import menu
import tradicional
import cientifica

from math import sin, cos, tan, sqrt, factorial, log
from PyQt5 import QtCore, QtGui, QtWidgets
import re

class controller():
    def __init__(self):
        self.Dialog_tradicional = QtWidgets.QDialog()
        self.ui_tradicional = tradicional.Ui_Dialog()
        self.ui_tradicional.setupUi(self.Dialog_tradicional)

        self.Dialog_cientifica = QtWidgets.QDialog()
        self.ui_cientifica = cientifica.Ui_Dialog()
        self.ui_cientifica.setupUi(self.Dialog_cientifica)

        self.Dialog_menu = QtWidgets.QDialog()
        self.ui_menu = menu.Ui_Dialog()
        self.ui_menu.setupUi(self.Dialog_menu)
        
        # Open
        self.ui_menu.pushButtonT.clicked.connect(self.abre_tradicional)
        self.ui_menu.pushButtonC.clicked.connect(self.abre_cientifica)

        # Back
        self.ui_tradicional.pushButton_21.clicked.connect(self.abre_menu)
        self.ui_cientifica.pushButton_25.clicked.connect(self.abre_menu)

        self.ui_tradicional.label.setText("0")
            
        # Dot
        self.ui_tradicional.pushButton_11.clicked.connect(self.dot)
        self.ui_cientifica.pushButton_11.clicked.connect(self.dot)
        
        # Equal
        self.ui_tradicional.pushButton_13.clicked.connect(self.resultado_tradicional)
        self.ui_cientifica.pushButton_13.clicked.connect(self.resultado_cientifica)

        # Clear
        self.ui_tradicional.pushButton_17.clicked.connect(self.botClear_tradicional)
        self.ui_cientifica.pushButton_17.clicked.connect(self.botClear_cientifica)

        # Backspace
        self.ui_tradicional.pushButton_18.clicked.connect(self.backspace_tradicional)
        self.ui_cientifica.pushButton_18.clicked.connect(self.backspace_cientifica)

        # Sine, cosine, and tangent
        self.ui_cientifica.pushButton_21.clicked.connect(self.sine)
        self.ui_cientifica.pushButton_22.clicked.connect(self.cosine)
        self.ui_cientifica.pushButton_23.clicked.connect(self.tangent)
        
        # Square Root
        self.ui_tradicional.pushButton_19.clicked.connect(self.sqrt_tradicional)
        self.ui_cientifica.pushButton_19.clicked.connect(self.sqrt_cientifica)
            
        # Ln
        self.ui_cientifica.pushButton_31.clicked.connect(self.log_cientifica)
        
        # Toggle Sign
        self.ui_tradicional.pushButton_8.clicked.connect(self.toggleSign_tradicional)
        self.ui_cientifica.pushButton_8.clicked.connect(self.toggleSign_cientifica)

        demaisBotoes = [
            self.ui_tradicional.pushButton,
            self.ui_tradicional.pushButton_2, self.ui_tradicional.pushButton_3,
            self.ui_tradicional.pushButton_4, self.ui_tradicional.pushButton_5,
            self.ui_tradicional.pushButton_6, self.ui_tradicional.pushButton_7,
            self.ui_tradicional.pushButton_9, self.ui_tradicional.pushButton_10,
            self.ui_tradicional.pushButton_12,
            self.ui_tradicional.pushButton_14, self.ui_tradicional.pushButton_15,
            self.ui_tradicional.pushButton_16, self.ui_tradicional.pushButton_20,
            self.ui_tradicional.pushButton_22, self.ui_tradicional.pushButton_23,
            self.ui_tradicional.pushButton_29, self.ui_tradicional.pushButton_30,
            self.ui_tradicional.pushButton_32,
        
            self.ui_cientifica.pushButton,
            self.ui_cientifica.pushButton_2, self.ui_cientifica.pushButton_3,
            self.ui_cientifica.pushButton_4, self.ui_cientifica.pushButton_5,
            self.ui_cientifica.pushButton_6, self.ui_cientifica.pushButton_7,
            self.ui_cientifica.pushButton_9, self.ui_cientifica.pushButton_10,
            self.ui_cientifica.pushButton_12,
            self.ui_cientifica.pushButton_14, self.ui_cientifica.pushButton_15,
            self.ui_cientifica.pushButton_16, self.ui_cientifica.pushButton_20,
            self.ui_cientifica.pushButton_24, self.ui_cientifica.pushButton_26,
            self.ui_cientifica.pushButton_27, self.ui_cientifica.pushButton_28,
            self.ui_cientifica.pushButton_29, self.ui_cientifica.pushButton_30,
        ]

        for botao in demaisBotoes:
            botao.clicked.connect(lambda checked, botao=botao: self.bot(botao.text()))

    def abre_tradicional(self):
        self.Dialog_tradicional.show()
        self.Dialog_menu.hide()
        self.ui_tradicional.label.setText("0")

    def abre_cientifica(self):
        self.Dialog_cientifica.show()
        self.Dialog_menu.hide()
        self.ui_cientifica.label.setText("0")
        

    def abre_menu(self):
        self.Dialog_menu.show()
        self.Dialog_tradicional.hide()
        self.Dialog_cientifica.hide()
        self.ui_tradicional.label.setText("0")
        self.ui_cientifica.label.setText("0")
        
        
    def bot(self, valor):
        textoAtualT = self.ui_tradicional.label.text()
        textoAtualC = self.ui_cientifica.label.text()
        
        operators = ['+', '-', '/', '*', '!', '^', '.']
        
    
        if textoAtualT == "0":
            self.ui_tradicional.label.setText(valor)
        else:
            self.ui_tradicional.label.setText(textoAtualT + valor)
            
        
            if valor not in [')', 'pi', 'e'] and (valor not in operators) and (textoAtualT[-1] in ['!', ')', 'e', 'i'] or textoAtualC[-1] in ['e', 'i']):
                self.ui_tradicional.label.setText(textoAtualT + '*' + valor)
            elif valor in ['pi', 'e'] and (not textoAtualT or textoAtualT[-1].isdigit() or textoAtualT[-1] in [')', 'e', 'i']):
                self.ui_tradicional.label.setText(textoAtualT + '*' + valor)
            else:
                self.ui_tradicional.label.setText(textoAtualT + valor)
        
        
        
        
        if textoAtualC == "0":
            self.ui_cientifica.label.setText(valor)
        else:
            self.ui_cientifica.label.setText(textoAtualC + valor)
                
        
            if valor not in [')', 'pi', 'e'] and (valor not in operators) and (textoAtualC[-1] in ['!', ')', 'e', 'i']):
                self.ui_cientifica.label.setText(textoAtualC + '*' + valor)
            elif valor in ['pi', 'e'] and (not textoAtualC or textoAtualC[-1].isdigit() or textoAtualT[-1] in [')', 'e', 'i']):
                self.ui_cientifica.label.setText(textoAtualC + '*' + valor)
            else:
                self.ui_cientifica.label.setText(textoAtualC + valor)
                



    def botClear_tradicional(self):
        self.ui_tradicional.label.setText("0")

    def botClear_cientifica(self):
        self.ui_cientifica.label.setText("0")
        
        
        

    def backspace_tradicional(self):
        textoAtual = self.ui_tradicional.label.text()
        if len(textoAtual) > 0:
            textoNovo = textoAtual[:-1]
            self.ui_tradicional.label.setText(textoNovo)
        else:
            self.ui_tradicional.label.setText("0")

    def backspace_cientifica(self):
        textoAtual = self.ui_cientifica.label.text()
        if len(textoAtual) > 0:
            textoNovo = textoAtual[:-1]
            self.ui_cientifica.label.setText(textoNovo)
        else:
            self.ui_cientifica.label.setText("0")
            
            
            
            
    def sine(self):
        self.ui_cientifica.label.setText("sin(" + self.ui_cientifica.label.text() + ")")
            
    def cosine(self):
        self.ui_cientifica.label.setText("cos(" + self.ui_cientifica.label.text() + ")")

    def tangent(self):
        self.ui_cientifica.label.setText("tan(" + self.ui_cientifica.label.text() + ")")
    
    def sqrt_tradicional(self):
        self.ui_tradicional.label.setText("sqrt(" + self.ui_tradicional.label.text() + ")")

    def sqrt_cientifica(self):
        self.ui_cientifica.label.setText("sqrt(" + self.ui_cientifica.label.text() + ")")
    
    def log_cientifica(self):
        self.ui_cientifica.label.setText("log(" + self.ui_cientifica.label.text() + ")")
        
        
        
        
    def resultado_tradicional(self):
        textoAtual = self.ui_tradicional.label.text()
        textoAtual = self.ajustes(textoAtual)
        
        textoAtual = re.sub(r'(\d+)!', lambda match: str(factorial(int(match.group(1)))), textoAtual)
        
        resultado = eval(textoAtual)
        resultado_str = "{:.15g}".format(resultado)
        self.ui_tradicional.label.setText(str(resultado_str))
    
    def resultado_cientifica(self):
        textoAtual = self.ui_cientifica.label.text()
        textoAtual = self.ajustes(textoAtual)
        
        textoAtual = re.sub(r'(\d+)!', lambda match: str(factorial(int(match.group(1)))), textoAtual)
    
    
        log_start = textoAtual.find("log(")
        
        if log_start != -1:
            log_end = textoAtual.find(")", log_start)
            log_expression = textoAtual[log_start + 4:log_end]
            log_result = log(eval(log_expression))
            textoAtual = textoAtual[:log_start] + str(log_result) + textoAtual[log_end + 1:]
        
        resultado = eval(textoAtual)
        resultado_str = "{:.15g}".format(resultado)
        self.ui_cientifica.label.setText(str(resultado_str))
        
        
        
    def ajustes(self, expression):
        open_parentheses = expression.count('(')
        closed_parentheses = expression.count(')')
    
        if open_parentheses > closed_parentheses:
            extra_parentheses = open_parentheses - closed_parentheses
            expression += ')' * extra_parentheses
        
        expression = expression.replace('^', '**')
        expression = expression.replace('pi', '3.14159265')
        expression = expression.replace('e', '2.718281828')
    
        return expression
    
    

    def dot(self):
        operators = ['+', '-', '/', '*', '!', '^']
        
        if self.ui_tradicional.label.text()[-1] in operators:
            self.ui_tradicional.label.setText(self.ui_tradicional.label.text() + "0.")
        elif not self.ui_tradicional.label.text()[-1] == ".":
            self.ui_tradicional.label.setText(self.ui_tradicional.label.text() + ".")
        
        if self.ui_cientifica.label.text()[-1] in operators:
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + "0.")
        elif not self.ui_cientifica.label.text()[-1] == ".":
            self.ui_cientifica.label.setText(self.ui_cientifica.label.text() + ".")


        
    def toggleSign_tradicional(self):
        self.toggleSign(self.ui_tradicional.label)
    
    def toggleSign_cientifica(self):
        self.toggleSign(self.ui_cientifica.label)
    
    def toggleSign(self, label):
        textoAtual = label.text()
    
        if textoAtual == "0":
            label.setText("0")
        else:
            operadores = ['+', '-', '/', '*']
            ultimo_operador = max(textoAtual.rfind(op) for op in operadores)
            novo_texto = ''
    
            if ultimo_operador != -1:
                if textoAtual[ultimo_operador] == '+':
                    novo_texto = textoAtual[:ultimo_operador] + '-' + textoAtual[ultimo_operador+1:]
                elif textoAtual[ultimo_operador] == '-':
                    novo_texto = textoAtual[:ultimo_operador] + '+' + textoAtual[ultimo_operador+1:]
                elif textoAtual[ultimo_operador] == '/':
                    novo_texto = textoAtual[:ultimo_operador] + '/-' + textoAtual[ultimo_operador+1:]
                elif textoAtual[ultimo_operador] == '*':
                    novo_texto = textoAtual[:ultimo_operador] + '*-' + textoAtual[ultimo_operador+1:]
            else:
                if re.match(r'^[+\-*/].*', textoAtual):
                    novo_texto = '-' + textoAtual[1:]
                else:
                    novo_texto = '-' + textoAtual
    
            label.setText(novo_texto)
            

import sys
app = QtWidgets.QApplication([])
application = controller()
application.Dialog_menu.show()
sys.exit(app.exec())


