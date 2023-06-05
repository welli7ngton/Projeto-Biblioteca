# Sistema-Gerência-de-Biblioteca

Este é um projeto de um sistema para gerenciamento de biblioteca em Python que permite cadastrar livros, alunos e prazos para entrega. O sistema utiliza a biblioteca Openpyxl para a manipulação dos dados e uma planilha do Excel como fonte de armazenamento.

# Funcionalidades
O sistema de biblioteca tem as seguintes funcionalidades:

Cadastro de Livros: Permite adicionar informações de novos livros, como título, autor, gênero, etc.

Cadastro de Alunos: Permite adicionar informações de novos alunos, como nome, número de matrícula, curso, etc.

Empréstimo de Livros: Permite emprestar livros para alunos, registrando a data de entrega esperada.

Devolução de Livros: Registra a devolução de um livro por um aluno.

Consulta de Livros Disponíveis: Permite visualizar os livros disponíveis na biblioteca.

Consulta de Alunos Cadastrados: Permite visualizar os alunos cadastrados.

Consulta de Livros Emprestados: Permite visualizar os livros emprestados e suas datas de entrega.

# Tecnologias Utilizadas
O projeto utiliza as seguintes tecnologias:

Python: Linguagem de programação principal.
Openpyxl: Biblioteca Python para manipulação de dados em formato tabular.

Excel: Planilha do Excel como fonte de armazenamento dos dados.

Como Utilizar
Instale o Python em seu sistema.

Instale a biblioteca Openpyxl usando o gerenciador de pacotes pip:
pip install Openpyxl

Execute o programa principal main.py para iniciar o sistema de biblioteca.

Siga as instruções do menu para cadastrar livros, alunos, realizar empréstimos, devoluções e consultas.

Os dados são armazenados em uma planilha do Excel chamada biblioteca.xlsx

# Observações
Certifique-se de ter a planilha biblioteca.xlsx no mesmo diretório do arquivo main.py.

O programa irá criar as planilhas necessárias caso a planilha não exista, mas é importante manter a estrutura correta das colunas.

É recomendado fazer backup do arquivo dados_biblioteca.xlsx regularmente para evitar a perda de dados.

# Melhorias Futuras
Implementar recursos adicionais, como edição de informações de livros e alunos, pesquisa avançada, relatórios, etc.

Adicionar autenticação de usuários para garantir o acesso seguro ao sistema.

Implementar validações de entrada para evitar erros e inconsistências nos dados.

Utilizar um banco de dados em vez de uma planilha do Excel para armazenar os dados.

Desenvolver uma interface gráfica para facilitar a interação com o sistema.

Implementar testes automatizados para garantir a qualidade do código.

## Sinta-se à vontade para personalizar o resumo de acordo com as necessidades do seu projeto e adicionar informações adicionais, como requisitos de instalação, créditos, licença, etc.
