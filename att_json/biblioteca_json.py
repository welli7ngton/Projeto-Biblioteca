import time, json

# listas para salvar os identificadores únicos e não ter cadastro duplicados   
id_aluno = []
id_livro = []

# dicionarios para vincular identificadores únicos aos atributos 
info_alunos = {}
info_livros = {}

# dicionarios para emprestimos
dic_emprestimos = {}


def importa(caminho,base_de_dados=[]):
    dados_import = []
    try:
        with open(caminho, "r",encoding="utf-8") as arq:
            base_de_dados = json.load(arq)
    except FileNotFoundError:
        exporta(caminho,base_de_dados)
    return base_de_dados

def exporta(caminho,base_de_dados):
    dados_import = base_de_dados
    with open(caminho, "w",encoding="utf-8") as arq:
        dados_import = json.dump(base_de_dados,arq,indent=2,ensure_ascii=False) 
    return base_de_dados


# funções para cadastro de alunos e livros
def cadastra_aluno():
    global id_aluno, info_alunos
    # criação de verificador unico    
    verificador = str(len(id_aluno))
    
    if verificador not in id_aluno:
        id_aluno.append(verificador)
        
    else:
        verificador += 1
    print("ID =",verificador)
    nome = input("Nome do Aluno: ")   
    idade = int(input("Idade: "))
    serie = input("Série: ")
    turno = input("Turno: ")
    contato = input("Contato (00 0 0000-0000): ")
    print("Endereço: Rua, Bairro, Número.:")
    endereco = input()

    # atualizando dicionário
    info_alunos[verificador] = f"Nome = {nome.capitalize()}, Série = {serie}, Turno = {turno}, Idade = {idade}, Contato = {contato}, Endereço = {endereco.capitalize()}"

    print()
    print("Os dados do aluno cadastrados são: ")
    print(info_alunos[verificador])
    print()
    
    exporta('.jsonfiles/id_aluno.json',id_aluno)
    exporta('.jsonfiles/info_alunos.json',info_alunos)



def cadastra_livro():    
    global id_livro, info_livros
    titulo_livro = input("Digite o título do livro: ")
    genero = input("Digite o gênero do livro: ")
    autor = input("Digite o Autor: ")
    editora = input("Digite a Editora: ")
    qtd = input("Digite a quantidade: ")
    # verificando se a quantidade é um valor numérico
    while True:
        if qtd.isdigit() == False:
            qtd = input("Digite um valor válido, um número: ")
        else:
            break
    numeracao = input("Digite a numeração: ")
    # verificando se a numeração do livro é um valor numérico
    while True:
        if numeracao.isdigit():
            while True:
                if numeracao not in id_livro and numeracao.isdigit():
                    break
                else:
                    print("Livro já cadastrado ou numeração inválida.")
                    numeracao = input("Digite uma numeração válida: ")
            break
        else:
            print("Digite uma numeração válida.")

    

    

    # atualizando dicionário
    info_livros[numeracao] = f"Título = {titulo_livro.capitalize()}, Gênero = {genero.capitalize()}, Autor = {autor.capitalize()},Editora =  {editora.capitalize()}, Quantidade = {qtd}, Numeração = {numeracao}"
    id_livro.append(numeracao) 

    print()
    print("As informações do livro cadasrtado são:")  
    print("NUMERAÇÃO: ", numeracao) 
    print(info_livros[numeracao])
    print()
    
    exporta('.jsonfiles/id_livro.json',id_livro)
    exporta('.jsonfiles/info_livros.json',info_livros)



# funções para alterações de cadastro
def altera_livro():
    global id_livro, info_livros
    # verificação de existencia do livro
    while True:
        numeracao = input("Digite a numeração do livro que quer alterar: ")
        if numeracao not in id_livro:
            print("Livro não cadastrado ou numeração inválida, revise e digite uma numeração válida.")
            continue
        else:
            print("O livro que vai ser alterado é:")
            print(info_livros[numeracao])
            print("Digite as alterações:")

            # cadastro de alterações
            titulo_livro = input("Digite o título do livro: ")
            genero = input("Digite o gênero do livro: ")
            autor = input("Digite o Autor: ")
            editora = input("Digite a Editora: ")
            qtd = input("Digite a quantidade: ")
            while True:
                if qtd.isdigit() == False:
                    qtd = input("Digite um valor válido, um número: ")
                else:
                    qtd = int(qtd)
                    break
            
            # atualizando dados no dicionário
            info_livros[numeracao] = f"Título = {titulo_livro.capitalize()}, Gênero = {genero.capitalize()}, Autor = {autor.capitalize()},Editora =  {editora.capitalize()}, Quantidade = {qtd}"
            break
    exporta('.jsonfiles/info_livros.json',info_livros)

                
def altera_aluno():
    global id_aluno, info_alunos
    while True:
        verificador = input("Digite o ID do Aluno que quer alterar: ")
        if verificador not in id_aluno:
            print("Aluno não cadastrado ou numeração inválida, revise e digite uma numeração válida.")
            continue 
        else:
            print("O cadastro que vai ser alterado é:")
            print(info_alunos[verificador])
            print("Digite as alterações:")

            nome = input("Nome do Aluno: ")
            serie = str(input("Série: "))
            turno = input("Turno: ")
            idade = int(input("Idade: "))
            print("Contato: 00 0 0000 0000")
            contato = input()
            print("Endereço: Rua, Bairro, Número.:")
            endereco = input()

            # atualizando dicionário
            info_alunos[verificador] = f"Nome = {nome.capitalize()}, Série = {serie}, Turno = {turno}, Idade = {idade}, Contato = {contato}, Endereço = {endereco.capitalize()}"

            break
    exporta('.jsonfiles/info_alunos.json',info_alunos)
    

# funções para empréstimo e devolução de livros

def emprestimo():
    global info_alunos, dic_emprestimos

    r = input("Tem conhecimento do ID do aluno? [S]im [N]ão: ")
    if r in "nN":
        nome = input("Digite o nome do aluno: ")

        contador = 0
        print(info_alunos["ID"])   
        for chave in info_alunos:    
            if nome in info_alunos[chave][1]:  
                print(info_alunos[chave])
                contador += 1
        if contador == 0:
            print("Aluno não encontrado.")
    
    while True:
        key_aluno = input("Digite o ID do aluno: ")

        if key_aluno not in info_alunos:
            print("ID não encontrado, digite um ID válido.")
            continue

        else:

            livro = input("Digite o Livro que será emprestado: ")
            devo = input("Digite a data para devolução(Dia/Mês): ")
            chave = key_aluno+(devo.replace("/", ""))
            
            while chave  in dic_emprestimos:
                print("O aluno já tem um livro para entregar nessa data, adicione mais um dia na data de entrega para poder emprestar mais um livro.")
                devo = input("Digite a data para devolução(Dia/Mês): ")
                chave = key_aluno+(devo.replace("/", ""))
                
            else:
                dic_emprestimos[chave] = info_alunos[key_aluno], livro, devo
                print(dic_emprestimos[chave])
                break
    exporta('.jsonfiles/dic_emprestimos.json',dic_emprestimos)
    

def devolucao():
    global dic_emprestimos
    

    r = input("Tem conhecimento do ID do aluno? [S]im [N]ão: ")
    if r in "nN":
        nome = input("Digite o nome do aluno: ")
        contador = 0
        print(f"Registros de {nome} nas pendências de devolução.")
        print(dic_emprestimos["ID EMPRESTIMO"])  
        for chave,valor in dic_emprestimos.items():    
            if nome.capitalize() in dic_emprestimos[chave]:  
                print(dic_emprestimos[chave])
                contador += 1
        if contador == 0:
            print("Aluno não encontrado.")
            
    while True:
        idaluno = input("Digite o ID do aluno: ")
        devo = input("DIGITE A DATA QUE FOI PROGRAMADA PARA ENTREGA(DD/MM): ")
        chave = idaluno+(devo.replace("/", ""))
        if chave in dic_emprestimos:
                
            dic_emprestimos.pop(chave)
            print()
            print("Devolução realizada.")
            print()
            break
        else:
            print("Data de devolução ou ID inválidos. Repita o processo.")
    exporta('.jsonfiles/dic_emprestimos.json',dic_emprestimos)



id_aluno = importa('.jsonfiles/id_aluno.json',base_de_dados=[])
id_livro = importa('.jsonfiles/id_livro.json',base_de_dados=[])


info_alunos = importa('.jsonfiles/info_alunos.json',base_de_dados=[])
info_livros = importa('.jsonfiles/info_livros.json',base_de_dados=[])

dic_emprestimos = importa('.jsonfiles/dic_emprestimos.json',base_de_dados=[])

opcoes = {
    "1":cadastra_aluno,
    "2":cadastra_livro,
    "3":altera_aluno,
    "4":altera_livro,
    "5":emprestimo,
    "6":devolucao,
}


while True:

    
    # menu de opções
    print("|#################-MENU-#################|")
    print("|(1) = CADASTRO ALUNO                    |")
    print("|(2) = CADASTRO LIVRO                    |")
    print("|(3) = ALTERAÇÃO DE CADASTRO ALUNO       |")
    print("|(4) = ALTERAÇÃO DE CADASTRO LIVRO       |")
    print("|(5) = EMPRÉSTIMO DE LIVRO               |")
    print("|(6) = DEVOLUÇÃO DE LIVRO                |")
    print("|(7) = RELAÇÃO DE ALUNOS CADASTRADOS     |")
    print("|(8) = RELAÇÃO DE LIVROS CADASTRADOS     |")
    print("|(9) = RELAÇÃO DE EMPRÉSTIMOS            |")
    print("|(0) = ENCERRAR PROGRAMA                 |")
    print("|########################################|")

    r = input("Escolha a ação: ")

    if r == "0":
        print("Encerrando...")
        time.sleep(2)
        break
    elif r == "7":
        print("RELAÇÃO DE ALUNOS CADASTRADOS")
        print("Gerando...")
        time.sleep(3)
        for chave,item in info_alunos.items():
            print("ID =",chave,item)

    elif r == "8":
        print("RELAÇÃO DE LIVROS CADASTRADOS")
        print("Gerando...")
        time.sleep(3)
        for item in info_livros:
            print(info_livros[item])

    elif r == "9":
        print("RELAÇÃO DE EMPRÉSTIMOS")
        print("Gerando...")
        time.sleep(3)
        for chave,item in dic_emprestimos.items():
            print(chave,item)
    else:
        execucao = opcoes.get(r)
        execucao()