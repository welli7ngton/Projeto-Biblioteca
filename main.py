import random, openpyxl, time
from openpyxl import Workbook


id_aluno = []
id_livro = []

info_alunos = {}
info_livros = {}


##################################################################################################################

try:
    database_ids = openpyxl.load_workbook("ids_alunos_livros.xlsx")
except FileNotFoundError:
    database_ids = Workbook()
    database_ids.save("ids_alunos_livros.xlsx")


if "ids_alunos"  in database_ids.sheetnames:
    planilha_ids_alunos = database_ids["ids_alunos"]
else:
    planilha_ids_alunos = database_ids.create_sheet("ids_alunos")
    planilha_ids_alunos.title = "ids_alunos"
    database_ids.save("ids_alunos_livros.xlsx")

for celula in planilha_ids_alunos["A"]:
    id_aluno.append(celula.value)


if "ids_livros"  in database_ids.sheetnames:
    planilha_ids_livros = database_ids["ids_livros"]
else:
    planilha_ids_livros = database_ids.create_sheet("ids_livros")
    planilha_ids_livros.title = "ids_livros"
    database_ids.save("ids_alunos_livros.xlsx")
    
for celula in planilha_ids_livros["A"]:
    id_livro.append(celula.value)

##################################################################################################################

def cadastra_aluno():
       
    verificador = random.randint(0, 9999)
    if verificador not in id_aluno:
        id_aluno.append(verificador)
 
    nome = input("Nome do Aluno: ")
    

    serie = input("Série: ")
    turno = input("Turno: ")
    idade = int(input("Idade: "))
    print("Contato: (xx) x xxxx-xxxx")
    contato = input()
    print("Endereço: Rua, Bairro, Número.:")
    endereco = input()
    info_alunos[str(verificador)] = f"Nome = {nome.capitalize()}, Série = {serie}, Turno = {turno}, Idade = {idade}, Contato = {contato}, Endereço = {endereco.capitalize()}"

    
    proxima_linha_aluno = planilha_ids_alunos.max_row + 1

    planilha_ids_alunos[f"A{proxima_linha_aluno}"] = verificador
    planilha_ids_alunos[f"B{proxima_linha_aluno}"] = nome.capitalize()
    planilha_ids_alunos[f"C{proxima_linha_aluno}"] = serie
    planilha_ids_alunos[f"D{proxima_linha_aluno}"] = turno.capitalize()
    planilha_ids_alunos[f"E{proxima_linha_aluno}"] = idade
    planilha_ids_alunos[f"F{proxima_linha_aluno}"] = contato
    planilha_ids_alunos[f"G{proxima_linha_aluno}"] = endereco.capitalize()

    database_ids.save("ids_alunos_livros.xlsx")
    


def cadastra_livro():
    
    titulo_livro = input("Digite o título do livro: ")
    genero = input("Digite o gênero do livro: ")
    autor = input("Digite o Autor: ")
    editora = input("Digite a Editora: ")
    qtd = input("Digite a quantidade: ")
    while True:
        if qtd.isdigit() == False:
            qtd = input("Digite um valor válido, um número: ")
        else:
            break
    numeracao = input("Digite a numeração: ")
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

            
    proxima_linha_livro = planilha_ids_livros.max_row + 1

    planilha_ids_livros[f"A{proxima_linha_livro}"] = numeracao
    planilha_ids_livros[f"B{proxima_linha_livro}"] = titulo_livro.capitalize()
    planilha_ids_livros[f"B{proxima_linha_livro}"] = genero.capitalize()
    planilha_ids_livros[f"D{proxima_linha_livro}"] = autor.capitalize()
    planilha_ids_livros[f"E{proxima_linha_livro}"] = editora.capitalize()
    planilha_ids_livros[f"F{proxima_linha_livro}"] = int(qtd)


    info_livros[numeracao] = f"Título = {titulo_livro.capitalize()}, Gênero = {genero.capitalize()}, Autor = {autor.capitalize()},Editora =  {editora.capitalize()}, Quantidade = {qtd}, Numeração = {numeracao}"
    id_livro.append(numeracao) 
    print("############ As informações do livro cadasrtado são: ############")  
    print("NUMERAÇÃO: ", numeracao) 
    print(info_livros[numeracao])
    print("#################################################################")
    database_ids.save("ids_alunos_livros.xlsx")

##################################################################################################################

def altera_livro():
    while True:
        num_livro = input("Digite a numeração do livro que quer alterar: ")
        if num_livro not in id_livro:
            print("Livro não cadastrado ou numeração inválida, revise e digite uma numeração válida.")
            continue
        else:
            print("O livro que vai ser alterado é:")
            print(info_livros[num_livro])
            print("Digite as alterações:")

            titulo_livro = input("Digite o título do livro: ")
            genero = input("Digite o gênero do livro: ")
            autor = input("Digite o Autor: ")
            editora = input("Digite a Editora: ")
            qtd = int(input("Digite a quantidade: "))
            
            info_livros[num_livro] = f"Título = {titulo_livro.capitalize()}, Gênero = {genero.capitalize()}, Autor = {autor.capitalize()},Editora =  {editora.capitalize()}, Quantidade = {qtd}"
            break
       
def altera_aluno():
    while True:
        num_aluno = input("Digite a numeração do Aluno que quer alterar: ")
        if num_aluno not in id_aluno:
            print("Aluno não cadastrado ou numeração inválida, revise e digite uma numeração válida.")
            continue
        else:
            print("O cadastro que vai ser alterado é:")
            print(info_alunos[num_aluno])
            print("Digite as alterações:")

            nome = input("Nome do Aluno: ")
            serie = input("Série: ")
            turno = input("Turno: ")
            idade = int(input("Idade: "))
            print("Contato: (xx) x xxxx-xxxx")
            contato = input()
            print("Endereço: Rua, Bairro, Número.:")
            endereco = input()
            info_alunos[num_aluno] = f"Nome = {nome.capitalize()}, Série = {serie}, Turno = {turno}, Idade = {idade}, Contato = {contato}, Endereço = {endereco.capitalize()}"
            break

##################################################################################################################

while True:
    print(len(id_aluno), "aluno")
    print(len(id_livro), "livro")
    print(id_aluno, "aluno")
    print(id_livro, "livro")
    print("############## MENU ##############")
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
                else:
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
        database_ids.save("ids_alunos_livros.xlsx")
        time.sleep(3)
        break