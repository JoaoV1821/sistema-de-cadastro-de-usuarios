from Usuario_class import * # Importa o módulo com as classes
from os import system # Função que digita comandos no terminal do windows

lista_usuarios = Lista_de_usuarios() # Instancia um objeto do tipo "Lista_de_usuarios"

while True: # Looping infinito
    try:
        nome = input('Digite seu nome: ') # Input do nome
        cpf = input('Digite seu CPF: ') # Input do CPF
        email = input('Digite seu email: ') # Input do email
        numero_de_celular = input('Digite seu número de celular: ') # Input do número de celular

        usuario = Usuario(nome, cpf, email, numero_de_celular) # Instancia um objeto do tipo "Usuario"

        lista_usuarios.add_usuario(usuario) # Faz a listagem dos usuários


    except Exception as E: # Captura as exceções
            print(E) # Imprime a mensagem de erro
            continue # Retorna ao início do looping
    else: # Caso não ocorra exeções, o programa irá perguntar se o usuário irá cadastrar mais alguém
        flag = input('Deseja cadastrar mais alguém? [S/N]: ').upper().strip()

        if flag == 'S': # Se o flag for igula a "S", o programa voltará ao looping
            continue
        else:
            break # Se não, irá encerrar o looping

system('cls') # limpa o terminal

print('-'*120)
lista_usuarios.imprime_usuarios() # Imprime a lista de usuários
print('-'*120)
