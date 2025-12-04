#------------Funções--------------

#listas dos games.
#não consegui colocar no main.
lista_jogos = []
novo_jogo = []

#Variáveis de contagem
i = 0
count = 0

#função para cadastrar jogos.
def cadastro():
    print("\nCadastro do jogo")

    print("\nDigite o nome do Jogo:")
    novo_jogo.append(input())

    print("\nEmpresa Responsável:")
    novo_jogo.append(input())

    print("\nGenêros do Jogo, separados por vírgula:")
    novo_jogo.append(input())

    print("\nPlataformas do jogo:")
    novo_jogo.append(input())

    print("\nAno de Lançamento do jogo:")
    novo_jogo.append(input())

    merge()

    print("\nCadastro Realizado com sucesso!")

    #count é o contador para saber quanto o número de jogos criados.
    global count
    count = count + 1
    novo_jogo.clear()

# nota: append() e insert() não criam outras listas, cria-se apenas um pointer que aponta para o endereço de memória da primeira lista. 
# Por isso se usa o metodo slicing [:], para criar um novo objeto lista.
#Função para mesclar a lista novo_jogo para a lista lista_jogos.
def merge():
    global i
    i = i + 1
    lista_jogos.insert(i,  novo_jogo[:])
    


def excluir():
    global count
    exit = ""
    ctz = ""
    while exit != "nao":
        print("\nSelecione o indice do jogo a ser excluido:")
        exc = int(input())

        #verifica se existe o indice digitado
        if (exc < count):
            #Mostra o jogo a ser deletado
            print("\nTem certeza que deseja excluir esse jogo? Digite 1 se sim.")
            print(f"{lista_jogos[exc][0]} {lista_jogos[exc][4]}")
            ctz = input()
            #Deleta o jogo, atualiza o contador de jogos e depois mostra a lista atualizada
            if(ctz == "1"):
                del lista_jogos[exc]
                count = count - 1
                print("\nJogo excluido com sucesso")
                print("\nLista atualizada dos games:\n")
                lista()
        elif(exc >= count):
            print("\nNão há nenhum jogo cadastrado nesse indice.")

        print("\nDeseja excluir outro jogo? Se não, digite nao, se sim digite qualquer tecla.")
        exit = input()

        
def lista():
    print("\nLista de Jogos catalogados:")
    for i in range(count):
        print(f"[{i}] {lista_jogos[i][0]} | Empresa: {lista_jogos[i][1]} | Gêneros: {lista_jogos[i][2]} | Plataformas: {lista_jogos[i][3]} | Ano: {lista_jogos[i][4]}")
#--------------------------