'''PONTOS NECESSÁRIOS PARA GERENCIADOR DE LISTA - objetivo treinar conhecimentos em listas >>> 01/10/2025 aprendizado orientado a projetos
- lista vazia para receber tarefas
- while true para o programa sempre ficar rodando enquanto usuário não terminar de add tarefas
    > if "Deseja quer continuar?"
- if para usuario remover tarefa da lista
-saída do programa com os itens da lista e informando quais serão as atividades pertinentes
'''

tarefas = []
nome = str(input('Digite seu nome: ')).strip().upper()
print(f'SEJA BEM-VINDO AO SEU GERENCIADOR DE TAREFAS {nome}.')
while True:
    nomec = nome.capitalize()
    
#adicionar tarefas    
    e = str(input(f'{nomec}, você deseja adicionar uma tarefa? [S/N] ')).strip().upper()[0]
    if e in 'Ss':
            tarefa = str(input(f'Digite a tarefa desejada: ')).strip().capitalize()
            tarefas.append(tarefa)
            print(f'{nomec}, sua lista de tarefas atualizada está aqui: {tarefas}.')
    elif e in 'Nn':
        print('Lista de Tarefas concluída.')
        print()
        print(f'{nomec}, sua lista de tarefas atualizada está aqui: {tarefas}.')
        break
    
    elif e not in 'SsNn':
        print(f'Opção inválida. Tente novamente!')
        #e = str(input(f'{nomec}, você deseja adicionar uma tarefa? [S/N] ')).strip().upper()[0]
        
#apenas visualizar tarefas - criar uma estrutura de repetição para visualizar a lista de tarefas
#e perguntar se desejar mover de lugar (acessar índice.)
        
#remover tarefas - criar uma estrutura de repetição para o usuário remover tarefas da lista

print(f'Mantenha a displina e siga sua lista com rigor!!\nAté mais...')
