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

    opcao = entrada_numerica("Escolha uma opção entre 1 e 4: ")
    return opcao
#-----------------------------------------------------------------------------------#
def main():
    turma = []
    while True:
        opcao = exibir_menu()
        if opcao == 1:
            matricula = int(input("Matricula do aluno: "))
            matricula = {}
            matricula['nome'] = str(input('Digite o nome do aluno: '))
            matricula['curso'] = str(input(f'Digite o nome do curso de {matricula['nome']}: ')).strip().capitalize()
            turma.append(matricula)
            print(matricula)
            print(turma)
            
            
            #perguntar nome
            #matricula 6 digitos
            #curso
    
            

#codigo principal

main()