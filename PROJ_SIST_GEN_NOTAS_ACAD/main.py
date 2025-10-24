from time import sleep
#criar função auxiliar para validar entradas numéricas dos usuários
def entrada_numerica(mensagem):
    while True:
            try:
                numero = int(input('Escolha um número: '))
                return numero
            except ValueError:
                print("Erro: Você não digitou um número válido! \nTente novamente!")
#-----------------------------------------------------------------------------------#
def exibir_menu():
    print('GERENCIADOR DE NOTAS ACADÊMICAS\n')
    print('1. Adicionar Novo Aluno')
    print('2. Lançar Notas do Aluno')
    print('3. Visualizar Boletim')
    print('4. Sair')
    print()
    opcao = entrada_numerica("Escolha uma opção entre 1 e 4: ")
    return opcao
#-----------------------------------------------------------------------------------#
def main():
    turma = []
    while True:
        opcao = exibir_menu()
        if opcao == 1:
            aluno = {}
            aluno.clear()
            print()
            aluno['Nome'] = str(input("Nome do aluno: ")).strip().title()
            aluno['Curso'] = str(input("Curso do aluno: ")).strip().title()
            aluno['Matricula'] = int(input("Matricula do aluno: "))
            
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
                    alterar_dado = int(input(
                    '''Qual dado deseja alterar?
    [1] - Nome do Aluno
    [2] - Curso
    '''))
                    if alterar_dado == 1:
                        print('Corrija abaixo o nome do novo aluno')
                        aluno['Nome'] = str(input("Nome do aluno: ")).strip().title()
                        print()
                        print(f'Nome do aluno {aluno['Nome']} corrigido com sucesso')
                        print()
                        
                    if alterar_dado == 2:
                        print('Corrija abaixo o curso do novo aluno')
                        aluno['Curso'] = str(input("Curso do aluno: ")).strip().title()
                        print()
                        print(f'Curso do aluno {aluno['Nome']} corrigido para {aluno['Curso']} com sucesso')
                        print()
                        
                if resp == 'S':
                    turma.append(aluno.copy())
                    sleep(0.5)
                    print()
                    print()
                    for k, v in aluno.items():
                        print(f'{k}: {v}')
                        sleep(0.8)
                    print()
                    print('Novo aluno registrado com sucesso na Turma!')
                    print()
                    break
            
            
#codigo principal
#ATENÇÃO - A lista Turmas devem ser separadas por matéria cursada - É necessario descobrir a lógica para fazer isso

main()