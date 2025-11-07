from time import sleep
from random import randint

turma = []
notas = []

#criar função auxiliar para validar entradas numéricas dos usuários
def entrada_numerica(msg):
    while True:
        print("Erro: Você não digitou um número válido! \nTente novamente!")
        if msg.isnumeric():
            break 
#-----------------------------------------------------------------------------------#
#def escolha_menu(num):
 
#-----------------------------------------------------------------------------------#
def opcoes_do_menu(opcao):
    while True:
        if opcao == 1: #adicionar novo aluno
            aluno = {}
            aluno.clear()
            print()
            aluno["Nome"] = str(input("Nome do aluno: ")).strip().title()
            aluno["Curso"] = str(input("Curso do aluno: ")).strip().title()
            while True:
                matricula = randint(110000, 119999)
                if matricula not in turma:
                    break
            aluno['Matricula'] = matricula
            
            while True:
                print()
                print('Confira os dados do aluno:')
                sleep(0.5)
                print()
                for k, v in aluno.items():
                    print(f'{k}: {v}')
                    sleep(0.8)
                print()
                while True:
                    resp = str(input('Os dados do aluno estão corretos? [S/N]')).strip().upper()[0]
                    if resp in 'SN':
                        break
                    print('ERRO! Responda apenas S ou N')
                if resp == 'N':
                    alterar_dado = entrada_numerica(
                    '''Qual dado deseja alterar?
        [1] - Nome do Aluno
        [2] - Curso
        ''')
                    if alterar_dado == 1:
                        print('Corrija abaixo o nome do novo aluno')
                        aluno["Nome"] = str(input("Nome do aluno: ")).strip().title()
                        print()
                        print(f'Nome do aluno {aluno["Nome"]} corrigido com sucesso')
                        print()
                        
                    if alterar_dado == 2:
                        print('Corrija abaixo o curso do novo aluno')
                        aluno["Curso"] = str(input("Curso do aluno: ")).strip().title()
                        print()
                        print(f'Curso do aluno {aluno["Nome"]} corrigido para {aluno["Curso"]} com sucesso')
                        print()
                        
                if resp == 'S':
                    print()
                    print('Validando Dados. Aguarde...')
                    sleep(1)
                    turma.append(aluno.copy())
                    sleep(0.5)
                    print()
                    for k, v in aluno.items():
                        print(f'{k}: {v}')
                        sleep(0.8)
                    print()
                    print('Novo aluno registrado com sucesso na Turma!')
                    print()
                    break
#-----------------------------------------------------------------------------------#            
        if opcao == 2: #lançar notas do aluno
            print()
            print('Você está na área de Lançamento de Notas')
            print('Para começar digite abaixo a matrícula do aluno desejado')
            while True:
                print()
                matricula = entrada_numerica('Digite Nº Matrícula: [4 para sair] ')
                if matricula == 4:
                        print('Voltando para Menu Principal. Aguarde...')
                        print()
                        sleep(0.8)
                        break
                print()
                for a in turma:
                    if a["Matricula"] == matricula:
                        print()
                        print('Aluno Encontrado.')
                        print()
                        for k, v in a.items():
                            print(f'{k}: {v}')
                            sleep(0.8)
                    else:
                        print('ERRO! Nº Matrícula não encontrado na Turma.')
                        print('Tente digitar novamente ou digite 4 para voltar ao menu principal')
                        
                        
                
            #selecionar aluno desejado pela matricula - aluno['matricula']
#-----------------------------------------------------------------------------------#             
        if opcao == 4: #sair do programa
            print('Programa finalizado com sucesso...')
            sleep(0.6)
            break