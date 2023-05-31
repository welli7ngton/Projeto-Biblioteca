import random, openpyxl, time
from openpyxl import Workbook

# listas para salvar os identificadores únicos e não ter cadastro duplicados   
id_aluno = []
id_livro = []

# dicionarios para vincular identificadores únicos aos atributos 
info_alunos = {}
info_livros = {}

#################################################################################################################

# criação da base de dados
# verifica se a planilha já existe e cria o arquivo caso não exista
try:
    database_ids = openpyxl.load_workbook("biblioteca.xlsx")

except FileNotFoundError:
    database_ids = Workbook()
    database_ids.save("biblioteca.xlsx")

# cria uma sheet chamada alunos na base de dados caso não exista
if "alunos"  in database_ids.sheetnames:
    planilha_alunos = database_ids["alunos"]
else:
    planilha_alunos = database_ids.create_sheet("alunos")
    planilha_alunos.title = "alunos"
    database_ids.save("biblioteca.xlsx")

# for para exportar os identificadores dos alunos para a lista 
for celula in planilha_alunos["A"]:
    id_aluno.append(celula.value)


# o primeiro for cria uma chave de dicionáro para cada identificador único do aluno com uma lista vazia
# o segundo for itera sobre as colunas da planilha e adiciona os dados(das linhas) na lista vinculando o 
# identificador único a cada conjunto de atribunos ex: nome, idade, turno...
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
for a in range(len(id_aluno)):                              #///////////////////////////////////////////////
    info_alunos[id_aluno[a]] = []                           #///////////////////////////////////////////////
    for coluna in planilha_alunos.iter_cols():              #///////////////////////////////////////////////
        info_alunos[id_aluno[a]].append(coluna[a].value)    #///////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////

if "livros"  in database_ids.sheetnames:
    planilha_livros = database_ids["livros"]
else:
    planilha_livros = database_ids.create_sheet("livros")
    planilha_livros.title = "livros"
    database_ids.save("biblioteca.xlsx")
  
for celula in planilha_livros["A"]:
    id_livro.append(celula.value)



# o primeiro for cria uma chave de dicionáro para cada identificador único de livro com uma lista vazia
# o segundo for itera sobre as colunas da planilha e adiciona os dados(das linhas) na lista vinculando o 
# identificador único a cada conjunto de atribunos ex, titulo, autor, editora...
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
for a in range(len(id_livro)):                              #///////////////////////////////////////////////
    info_livros[id_livro[a]] = []                           #///////////////////////////////////////////////
    for coluna in planilha_livros.iter_cols():              #///////////////////////////////////////////////
        info_livros[id_livro[a]].append(coluna[a].value)    #///////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////

##################################################################################################################

# função para cadastro de alunos
def cadastra_aluno():
    # criação de verificador unico    
    verificador = len(id_aluno)
    
    if verificador not in id_aluno:
        id_aluno.append(verificador)
        
    else:
        verificador += 1
    print("ID =",verificador)
    nome = input("Nome do Aluno: ")
    

    serie = input("Série: ")
    turno = input("Turno: ")
    idade = int(input("Idade: "))
    print("Contato: 00 0 0000 0000")
    contato = input()
    print("Endereço: Rua, Bairro, Número.:")
    endereco = input()

    # atualizando dicionário
    info_alunos[verificador] = f"Nome = {nome.capitalize()}, Série = {serie}, Turno = {turno}, Idade = {idade}, Contato = {contato}, Endereço = {endereco.capitalize()}"

    
    proxima_linha_aluno = planilha_alunos.max_row + 1

    # atualizando a planilha
    planilha_alunos[f"A{proxima_linha_aluno}"] = verificador
    planilha_alunos[f"B{proxima_linha_aluno}"] = nome.capitalize()
    planilha_alunos[f"C{proxima_linha_aluno}"] = serie
    planilha_alunos[f"D{proxima_linha_aluno}"] = turno.capitalize()
    planilha_alunos[f"E{proxima_linha_aluno}"] = idade
    planilha_alunos[f"F{proxima_linha_aluno}"] = contato
    planilha_alunos[f"G{proxima_linha_aluno}"] = endereco.capitalize()

    # salvando dados
    database_ids.save("biblioteca.xlsx")
    

# função para cadastro livros
def cadastra_livro():
    
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
                if int(numeracao) not in id_livro and numeracao.isdigit():
                    break
                else:
                    print("Livro já cadastrado ou numeração inválida.")
                    numeracao = input("Digite uma numeração válida: ")
            break
        else:
            print("Digite uma numeração válida.")

    numeracao = int(numeracao)

    proxima_linha_livro = planilha_livros.max_row + 1
    # atualizando a planilha
    planilha_livros[f"A{proxima_linha_livro}"] = numeracao
    planilha_livros[f"B{proxima_linha_livro}"] = titulo_livro.capitalize()
    planilha_livros[f"C{proxima_linha_livro}"] = genero.capitalize()
    planilha_livros[f"D{proxima_linha_livro}"] = autor.capitalize()
    planilha_livros[f"E{proxima_linha_livro}"] = editora.capitalize()
    planilha_livros[f"F{proxima_linha_livro}"] = int(qtd)

    # atualizando dicionário
    info_livros[numeracao] = f"Título = {titulo_livro.capitalize()}, Gênero = {genero.capitalize()}, Autor = {autor.capitalize()},Editora =  {editora.capitalize()}, Quantidade = {qtd}, Numeração = {numeracao}"
    id_livro.append(numeracao) 

    print("############ As informações do livro cadasrtado são: ############")  
    print("NUMERAÇÃO: ", numeracao) 
    print(info_livros[numeracao])
    print("#################################################################")
    database_ids.save("biblioteca.xlsx")

##################################################################################################################

# funções para alterações de cadastro
def altera_livro():
    # verificação de existencia do livro
    while True:
        numeracao = int(input("Digite a numeração do livro que quer alterar: "))
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



            linha_livro = id_livro.index(numeracao) + 1

            planilha_livros[f"B{linha_livro}"] = titulo_livro.capitalize()
            planilha_livros[f"C{linha_livro}"] = genero.capitalize()
            planilha_livros[f"D{linha_livro}"] = autor.capitalize()
            planilha_livros[f"E{linha_livro}"] = editora.capitalize()
            planilha_livros[f"F{linha_livro}"] = qtd

            break
                
def altera_aluno():
    while True:
        verificador = int(input("Digite o ID do Aluno que quer alterar: "))
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

            # atualizando planilha

            planilha_alunos[f"B{verificador + 1}"] = nome.capitalize()
            planilha_alunos[f"C{verificador + 1}"] = serie
            planilha_alunos[f"D{verificador + 1}"] = turno.capitalize()
            planilha_alunos[f"E{verificador + 1}"] = idade
            planilha_alunos[f"F{verificador + 1}"] = contato
            planilha_alunos[f"G{verificador + 1}"] = endereco.capitalize()

            # salvando dados
            database_ids.save("biblioteca.xlsx")
            break


##################################################################################################################

while True:
    
    # menu de opções
    print("################ MENU ################")
    print("1 = CADASTRO ALUNO/LIVRO")
    print("2 = ALTERAÇÃO DE CADASTRO ALUNO/LIVRO")
    print("0 = ENCERRAR PROGRAMA")

    r = input("Escolha a ação: ")
    if r == "1":
        while True:
            r = input("Digite [1] para cadastrar Aluno ou [2] para Livro: ")
            if r not in "12":
                print("Esse valor não é válido.")
                continue
            else:
                if r == "1":
                    cadastra_aluno() 
                    while True:               
                        r = input("Deseja cadastrar mais um aluno [S]im [N]ão: ")
                        if r.upper() in "SN":   
                            if r.upper() == "N":
                                break
                            else:
                                cadastra_aluno()
                        else: print("Digite um valor válido.")

                    break
                elif r == "2":
                    cadastra_livro()
                    while True:               
                        r = input("Deseja cadastrar mais um livro [S]im [N]ão: ")
                        if r.upper() in "SN":   
                            if r.upper() == "N":
                                break
                            else:
                                cadastra_livro()
                        else: print("Digite um valor válido.")

                    break 

    elif r == "2":
        while True:
            r = input("Digite [1] para alterar Aluno ou [2] para Livro: ")
            if r not in "12":
                print("Esse valor não é válido.")
                continue
            else:
                if r == "1":
                    altera_aluno() 
                    while True:               
                        r = input("Deseja alterar mais um aluno [S]im [N]ão: ")
                        if r.upper() in "SN":   
                            if r.upper() == "N":
                                break
                            else:
                                altera_aluno()
                        else: print("Digite um valor válido.")

                    break
                else:
                    altera_livro()
                    while True:               
                        r = input("Deseja alterar mais um livro [S]im [N]ão: ")
                        if r.upper() in "SN":   
                            if r.upper() == "N":
                                break
                            else:
                                altera_livro()
                        else: print("Digite um valor válido.")

                    break
        

    elif r == "0":
        
        print("Encerrando...")
        database_ids.save("biblioteca.xlsx")
        time.sleep(3)
        break