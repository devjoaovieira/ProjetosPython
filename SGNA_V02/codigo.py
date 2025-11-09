import funcoes

def main():
    turma = [] # Ou o dicionário que você planejou

    while True:
        funcoes.exibir_menu_principal()
        opcao = funcoes.validar_num("Escolha um número (1-4): ")

        if opcao == 1:
            novo_aluno = funcoes.add_novo_aluno(turma)
            turma.append(novo_aluno)
            print(f">>>> Aluno adicionado com sucesso <<<<")
            print(f"Total de alunos na turma: {len(turma)}")
            print()
        
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