#--------BIBLIOTECAS--------#
from time import sleep
from random import randint
#---------------------------#

#--------LISTAS--------#
# -> TURMAS
tecnologia = []
matematica = []
direito = []
#----------------------#
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

def obter_entrada_segura(mensagem, tipo):
   resp = input(mensagem)
   return f'Você digitou a opção {resp}'
