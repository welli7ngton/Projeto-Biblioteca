import random
import pandas as pd

id_livro = []
id_aluno = []

info_livros = {}
info_alunos = {}

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

def cadastra_livro():
    
    titulo_livro = input("Digite o título do livro: ")
    genero = input("Digite o gênero do livro: ")
    autor = input("Digite o Autor: ")
    editora = input("Digite a Editora: ")
    qtd = int(input("Digite a quantidade: "))
    numeracao = input("Digite a numeração: ")
    while True:
        if numeracao.isdigit():
            numeracao = int(numeracao)
            while True:
                if numeracao not in id_livro:
                    break
                else:
                    print("Livro já cadastrado.")
                    numeracao = int(input("Digite uma numeração que não foi cadastrada: "))
            break
        else:
            print("Digite uma numeração válida.")

        numeracao = input("Digite a numeração: ")

    info_livros[str(numeracao)] = f"Título = {titulo_livro.capitalize()}, Gênero = {genero.capitalize()}, Autor = {autor.capitalize()},Editora =  {editora.capitalize()}, Quantidade = {qtd}, Numeração = {numeracao}"
    id_livro.append(numeracao)    
    print(info_livros)

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

print(info_alunos)
