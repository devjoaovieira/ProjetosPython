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
            aluno['Nome_Aluno'] = str(input("Nome do aluno: ")).strip().title()
            aluno['matricula'] = int(input("Matricula do aluno: "))
            aluno['curso'] = str(input("Curso do aluno: ")).strip().title()
            turma.append(aluno.copy())
            print('Confira as informações do aluno:')
            for k, v in aluno.items():
                print(f'{k}: {v}')
                sleep(0.7)
            print()
            print('Aluno adicionado com sucesso!')
            print()
#codigo principal
#ATENÇÃO - A lista Turmas devem ser separadas por matéria cursada - É necessario descobrir a lógica para fazer isso

main()