#Importacao de bibliotecas
import random



#Definicao de funcoes
def NumeroMisterioso():
    "Inicia o jogo e faz o sorteio"
    
    print("Bem vindo ao jogo de adivinhacoes...\n")
    numeroDaSorte = random.randrange(101)
    
    return numeroDaSorte



def Dica(chute, NumeroMisterioso):
    "Ajuda o usuario a descobrir o numero misterioso"
    if chute > NumeroMisterioso:
        Dica = "MENOR"
    else:
        Dica = "MAIOR"
    
    return Dica



#Programa principal
num = NumeroMisterioso()
chute = int(input("Digite um numero inteiro de 0 a 100\n>> "))
tentativas = 1

while chute != num:
    print("Errrrrrou! Numero de tentativas: {}".format(tentativas))
    tentativas += 1
    
    dica = Dica(chute, num)
    print("Tenta de novo, o numero misterioso eh {}\n".format(dica))
    chute = int(input("Digite um numero inteiro de 0 a 100\n>> "))
    
print("Parabens, voce acertou em {} tentativas!".format(tentativas))
