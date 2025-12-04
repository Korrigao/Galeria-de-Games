from funcoes import *
from menu import *

while True:
    x = menu()

    if(x == 1):
        cadastro()
    elif(x == 2):
        lista()
    elif(x == 3):
        excluir()
    elif(x == 4):
        créditos()
    elif(x == 9):
        print("Encerrando o Pogama")
        break
    else:
        print("Opção Inválida. Tente Novamente\n")
    


    





