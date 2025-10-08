'''PONTOS NECESSÁRIOS PARA GERENCIADOR DE LISTA - objetivo treinar conhecimentos em listas >>> 01/10/2025 aprendizado orientado a projetos
- lista vazia para receber tarefas
- while true para o programa sempre ficar rodando enquanto usuário não terminar de add tarefas
    > if "Deseja quer continuar?"
- if para usuario remover tarefa da lista
-saída do programa com os itens da lista e informando quais serão as atividades pertinentes
'''
from time import sleep

tarefas = []
nome = str(input('Digite seu nome: ')).strip().upper()
print(f'SEJA BEM-VINDO AO SEU GERENCIADOR DE TAREFAS {nome}.')
sleep(1)
print()
while True:
    finalizar = False
    nomec = nome.capitalize()
#adicionar primeira tarefa
    tarefa = str(input(f'{nomec}, digite a primeira tarefa desejada: ')).strip().capitalize()
    tarefas.append(tarefa)
    print(f'{tarefa} adicionado à lista com sucesso!!!')
    print()#adicionando uma linha de espaço

#adicionar mais tarefas    
    e = str(input(f'{nomec}, você deseja adicionar mais tarefas? [S/N] ')).strip().upper()[0]
    print()#adicionando uma linha de espaço

    #ESTRUTURA DE REPETIÇÃO
    while e not in 'SsNn': #validação de entrada
        print(f'Opção inválida. Tente novamente!')
        print()#adicionando uma linha de espaço
        e = str(input(f'{nomec}, você deseja adicionar mais tarefas? [S/N] ')).strip().upper()[0]
        

    while e in 'Ss': #fica repetindo o bloco de código enquanto usuário quiser inserir tarefas
            tarefa = str(input(f'Digite a tarefa desejada: ')).strip().capitalize()
            tarefas.append(tarefa)
            print(f'{nomec}, sua lista de tarefas atualizada está aqui:')
            for indice, tarefa in enumerate(tarefas): #visualizar lista até o momento
                print(f'{indice + 1} - {tarefa}')
            print()#adicionando uma linha de espaço
            e = str(input(f'{nomec}, você deseja continuar adicionando tarefas? [S/N] ')).strip().upper()[0]
            
            while e not in 'SsNn': #verificação de entrada caso o usuário digite algo diferente de SIM ou NÃO
                print(f'Opção inválida. Tente novamente!')
                print()#adicionando uma linha de espaço
                e = str(input(f'{nomec}, você deseja adicionar uma tarefa? [S/N] ')).strip().upper()[0]
#--------------------------------------------------------------------------------------------------------------------#

    if e in 'Nn':
        print()#adicionando uma linha de espaço
        print(f'{nomec}, sua lista de tarefas atualizada está aqui:\n')
        #MOSTRAR LISTA
        for indice, tarefa in enumerate(tarefas): #visualizar lista até o momento
            print(f'{indice + 1} - {tarefa}')
        print()#adicionando uma linha de espaço

        e = str(input(f'Você deseja continuar alterando sua lista de tarefas? [S/N] ')).strip().upper()[0]

        while e not in 'SsNn': #validação de entrada
            print(f'Opção inválida. Tente novamente!')
            print()#adicionando uma linha de espaço
            e = str(input(f'Você deseja continuar alterando sua lista de tarefas? [S/N] ')).strip().upper()[0]
#--------------------------------------------------------------------------------------------------------------------#

#-----------------ESTRUTURA DE REPETIÇÃO PARA ALTERAR LISTA APPEND OU REMOVE-----------------------------------------#
        if e in 'Nn':
            print() #adicionando uma linha de espaço
            print(f'Lista de Tarefas concluída com total de {len(tarefas)} tarefas.')
            for indice, tarefa in enumerate(tarefas): #visualizar lista final
                print(f'{indice + 1} - {tarefa}')
            print() #adicionando uma linha de espaço
            print() #adicionando uma linha de espaço
            break

        else:
            if e in 'Ss':
                opcao = int(input('''Escolha a opção que você deseja:\n
    1 - Adicionar Item na lista\n 
    2 - Remover Item da lista\n
    Digite: '''))
                
                while True:
                    if opcao == 1: #adicionar item
                        tarefa = str(input(f'Digite a tarefa desejada: ')).strip().capitalize()
                        tarefas.append(tarefa)
                        print(f'{nomec}, sua lista de tarefas atualizada está aqui:')
                        for indice, tarefa in enumerate(tarefas): #visualizar lista até o momento
                            print(f'{indice + 1} - {tarefa}')
                        print()#adicionando uma linha de espaço

                        opcao = int(input('''Escolha a opção que você deseja:\n
    1 - Adicionar Item na lista\n 
    2 - Remover Item da lista\n
    3 - Finalizar programa e visualizar lista\n
    Digite: '''))

                    elif opcao == 2: #remover item
                        #MEU OBJETIVO AGORA É REMOVER O ITEM ESCOLHIDO PELO USUÁRIO
                        remover = int(input('Digite o número da tarefa que deseja remover: '))
                        tarefas.pop(remover - 1) # -1 
                        print(f'{nomec}, sua lista de tarefas atualizada está aqui:')
                        for indice, tarefa in enumerate(tarefas): #visualizar lista até o momento
                            print(f'{indice + 1} - {tarefa}')
                        print()#adicionando uma linha de espaço

                        opcao = int(input('''Escolha a opção que você deseja:\n
    1 - Adicionar Item na lista\n 
    2 - Remover Item da lista\n
    3 - Finalizar programa e visualizar lista\n
    Digite: '''))

                    elif opcao == 3:
                        print(f'Lista de Tarefas concluída com total de {len(tarefas)} tarefas.')
                        for indice, tarefa in enumerate(tarefas): #visualizar lista até o momento
                            print(f'{indice + 1} - {tarefa}')
                        finalizar = True
                        break

                    elif opcao != 1 or opcao != 2:
                        print('Opção Inválida. Tente novamente!')
                        opcao = int(input('''Escolha a opção que você deseja:\n
                
    1 - Adicionar Item na lista\n 
    2 - Remover Item da lista\n
    3 - Finalizar programa e visualizar lista\n
    Digite: '''))
    if finalizar:
        break                
              
        
#próximo bloco de estudos == usar metodo pop() + enumerate para remover item específico que o usuário deseja da lista
print()
print(f'Mantenha a displina e siga sua lista com rigor!!\n\nAté mais...')
