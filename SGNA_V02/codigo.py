import funcoes

def main():
    turma = [] # Ou o dicionário que você planejou

    while True:
        funcoes.exibir_menu_principal()
        opcao = funcoes.validar_num()

        if opcao == 1:
            print('num 1 OK')
            #funcoes.adicionar_novo_aluno(turma) # Escreva isso, mesmo sem a função existir
        
        elif opcao == 2:
            print('num 2 OK')
            #funcoes.lancar_notas(turma) # Escreva isso...
        
        elif opcao == 3:
            print('num 3 OK')
           # funcoes.exibir_boletim(turma) # Escreva isso...
        
        elif opcao == 4:
            print('num 4 OK')
            break
        
        else:
            print("Opção inválida.")

funcoes.boas_vindas()
main()