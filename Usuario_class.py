from validate_docbr import CPF # Biblioteca de validação de documentos nacionais
import re # Biblioteca de expressões regulares

class Usuario:
    def __init__(self, nome, cpf, email, numero_de_celular):
        self.__nome = self.__formata_nome(nome) # Nome do usuário
        self.__cpf = self.__valida_cpf(cpf) # CPF do usuário
        self.__email = self.__valida_email(email) # Email do usuário
        self.__numero_de_celular = self.__valida_celular(numero_de_celular) # Número de celular do usuário


    def __formata_nome(self, nome): # Formata as iniciais do nome para maiúsculo e retira os espaços excedentes dos lados
        return nome.strip().title()


    def __valida_cpf(self, cpf): # Função responsável por validar o CPF
       if len(cpf) != 11: # Verifica a quantidade de dígitos do CPF
           raise ValueError('\033[31mCPF inválido!\033[m') # Erro caso o len de CPF for diferente de 11
       else:
            validador = CPF() # Objeto do tipo "CPF"
            if validador.validate(cpf): # Valida o CPF 
                return validador.mask(cpf) # Formata o CPF para "000.000.000-00"
            else:
                raise ValueError('\033[31mCPF inválido!\033[m') # Erro caso o CPF seja inválido

    
    def __valida_email(self, email): # Função responsável por validar o email
        modelo_email = '([a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-z](\.[a-z])?)' # Expressão regular para validar o email
        valida = re.findall(modelo_email, email) # Se estiver no padrão irá retornar "True" se não, irá retornar "False"

        if valida: # Retornará o email se "valida" for "True"
            return email
        else:
            raise ValueError('\033[31mEmail inválido!\033[m') # Retornará um erro se "valida" for "False"
    

    def __valida_celular(self, numero):
        if len(numero) != 11: # Retorna um erro se o len do número for diferente de 11
            raise ValueError('\033[31mNúmero de celular inválido!\033[m')
        else:
            modelo_celular = ('[1-9]{2}9[0-9]{4}[0-9]{4}') # Expressão regular para validar o número de celular
            valida = re.findall(modelo_celular, numero) # Se estiver no padrão irá retornar "True" se não, irá retornar "False"

            if valida: # Retornará o número se valida for "True"
                return f'+55({numero[0:2]}){numero[2:7]}-{numero[7:]}' # Formata o número para "+55(00)90000-0000"
            else:
                raise ValueError('\033[31mNúmero de celular inválido!\033[m') # Retornará um erro se valida for "False"

        
    @property # Getter do nome
    def nome(self): 
        return self.__nome


    @property # Getter do CPF
    def cpf(self):
        return self.__cpf
    

    @property # Getter do email
    def email(self):
        return self.__email


    @property # Getter do número de celular
    def numero_de_celular(self):
        return self.__numero_de_celular


# Classe responsável por listar os usuários
class Lista_de_usuarios:
    def __init__(self):
        self.__lista_de_usuarios = [] # Lista de usuários
    

    def add_usuario(self, usuario): # Adiciona os usuários na lista
       self.__lista_de_usuarios.append(usuario)
    

    def imprime_usuarios(self):
        for usuario in self.__lista_de_usuarios: # Imprime todos os usuários cadastrados
            print(f'{self.__lista_de_usuarios.index(usuario)+1} - Nome: {usuario.nome} CPF: {usuario.cpf} Email: {usuario.email} Número do celular: {usuario.numero_de_celular}')
