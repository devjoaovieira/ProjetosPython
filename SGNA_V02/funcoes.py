#--------BIBLIOTECAS--------#
from time import sleep
from random import randint
#---------------------------#
#-------------------TOPO DO CÓDIGO / PRINCIPAL------------------#
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
#-------------------------------------#

#--------------FUNÇÕES GENÉRICAS DE VALIDAÇÃO-----------------------#

def validar_num(mensagem_input):
    while True:
        try:
            # Tenta converter a entrada para um número inteiro
            numero = int(input(mensagem_input))
            # Se a conversão for bem-sucedida, sai do loop
            break
        except ValueError:
            # Se ocorrer um erro (ex: o usuário digitou texto), informa o erro
            print("Entrada inválida. Por favor, digite um número inteiro.")
    return numero
        

def obter_texto_validado(mensagem_input):
    """Garante que o usuário não digitou um texto vazio."""
    while True:
        texto = input(mensagem_input).strip().title()

        if texto != "":
            return texto
        else:
            print('ERRO! A entrada não pode estar vazia.')

def validar_S_N(pergunta):
    while True:
        resp = str(input(pergunta)).strip().upper()[0]
        if resp in 'SN':
            
            break
        else:
            print('ERRO! Digite apenas SIM ou NÂO')
    return resp
#============================== FIM ================================#

#-------------------OPÇÕES DOS ALUNOS------------------#
# ADICIONAR NOVO ALUNO
def add_novo_aluno(lista_da_turma):
    aluno = {}
    print()
    aluno['Nome'] = obter_texto_validado("Digite o nome do Aluno: ").title()
    aluno['Curso'] = obter_texto_validado("Digite o curso do Aluno: ").title()
   # Em funcoes.py, dentro de add_novo_aluno()

    while True:
        # 1. Gera um número candidato
        matricula = randint(110000, 119999) 
        # 2. Assume que o número é único (configura a "flag")
        matricula_encontrada = False 
        
        # 3. Percorre a LISTA DE DICIONÁRIOS que veio do main()
        for aluno_existente in lista_da_turma: 
            
            # 4. Compara o NÚMERO (matricula) com o VALOR da chave 'Matricula'
            if aluno_existente['Matricula'] == matricula: 
                matricula_encontrada = True # 5. Encontrou uma duplicata!
                break # 6. Para de procurar (quebra o 'for')
        
        # 7. DEPOIS de verificar TODOS os alunos:
        if not matricula_encontrada:
            # 8. Se a flag ainda for Falsa, o número é único.
            aluno['Matricula'] = matricula
            break # 9. Quebra o 'while True' e continua o programa
        
        # (Se a flag for True, o 'while True' recomeça e gera um novo número)
    aluno_verificado = conferir_dados_aluno(aluno)
    
    # A fábrica só devolve o produto 100% aprovado!
    return aluno_verificado 
    

def conferir_dados_aluno(aluno):
     while True:
        print()
        print('Confira os dados do aluno:')
        sleep(0.5)
        print()
        for k, v in aluno.items():
            print(f'{k}: {v}')
            sleep(0.8)
        print()
        resp = validar_S_N("Os dados do aluno estão corretos? [S/N] ")
        if resp in 'Ss':
            print('Confirmando dados...')
            sleep(0.7)
            print('Adicionando aluno...')
            sleep(0.7)
            return aluno
        
        elif resp in 'Nn':
            alterar_dado = validar_num(
'''Qual dado deseja alterar?
[1] - Nome do Aluno
[2] - Curso
Escolha: 
''')
            if alterar_dado == 1:
                print('Corrija abaixo o nome do novo aluno')
                aluno["Nome"] = obter_texto_validado("Nome do aluno: ") 
                print()
                print(f'Nome do aluno {aluno["Nome"]} corrigido com sucesso')
                print()
                
            elif alterar_dado == 2:
                print('Corrija abaixo o curso do novo aluno')
                aluno["Curso"] = obter_texto_validado("Curso do aluno: ")
                print()
                print(f'Curso do aluno {aluno["Nome"]} corrigido para {aluno["Curso"]} com sucesso')
                print()
            else:
                print('Opção Inválida.')
        
#============================== FIM ================================#
def verificar_existencia_alunos(turma, existencia=False):
    if len(turma) == 0:
        print('Não existem alunos na turma. \nImpossível lançar notas. Para começar adicione um aluno na turma.')
        print()
    else:
        existencia=True
        print('Aluno(s) encontrado(s) na Turma. Aguarde para lançar notas...')
        sleep(1)
        print()

        if existencia:
            buscar_aluno_por_matricula(turma)


def buscar_aluno_por_matricula(lista_da_turma):
        print('Vamos buscar aluno(a) para lançar notas.')
        sleep(0.5)
        print()
        # verificar se existe matricula digitada na turma
        matricula_procurada = validar_num("Digite a matrícula do aluno para começar: ")

        for aluno in lista_da_turma:
            if aluno['Matricula'] == matricula_procurada:
                print(f'Aluno Encontrado: ')
                for k, v in aluno.items():
                    print(f'{k} {v}')
                print()
                return aluno
            
        print("Erro: Matrícula não encontrada na turma.")
        print()
        return None
            
            

