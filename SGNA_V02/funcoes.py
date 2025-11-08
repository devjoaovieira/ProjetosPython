#--------BIBLIOTECAS--------#
from time import sleep
from random import randint
#---------------------------#

def boas_vindas():
    saudacao = "SEJA BEM-VINDO(A) AO GERENCIADOR ACADEMICO"
    print('-'*len(saudacao))
    print(saudacao)
    print('-'*len(saudacao))


def exibir_menu_principal():
    print("GERENCIADOR DE NOTAS ACADÊMICAS")
    print()
    print('1. Adicionar Novo Aluno')
    print('2. Lançar Notas do Aluno')
    print('3. Visualizar Boletim')
    print('4. Sair')

def validar_num():
    while True:
        try:
            # Tenta converter a entrada para um número inteiro
            numero = int(input("Digite um número inteiro: "))
            # Se a conversão for bem-sucedida, sai do loop
            break
        except ValueError:
            # Se ocorrer um erro (ex: o usuário digitou texto), informa o erro
            print("Entrada inválida. Por favor, digite um número inteiro.")
    return numero
        

def obter_texto_validado(mensagem_input):
    """Garante que o usuário não digitou um texto vazio."""
    while True:
        texto = input(mensagem_input).strip()

        if texto != "":
            return texto
        else:
            print('ERRO! A entrada não pode estar vazia.')