import funcoes

def main():
    turma = [] 

    while True:
        funcoes.exibir_menu_principal()
        opcao = funcoes.validar_num("Escolha um número (1-4): ")

        if opcao == 1:
            novo_aluno = funcoes.add_novo_aluno(turma)
            turma.append(novo_aluno)
            print(f">>>> Aluno adicionado com sucesso <<<<")
            print(f"Total de alunos na turma: {len(turma)}")
            print()
        
        elif opcao == 2: # lançar notas do aluno
            aluno_encontrado = funcoes.verificar_existencia_alunos(turma)

            if aluno_encontrado is not None:
                lancar_nota(aluno_encontrado)
            
            #funcoes.lancar_notas(turma) # Escreva isso...
        
        elif opcao == 3:
            print('num 3 OK')
           # funcoes.exibir_boletim(turma) # Escreva isso...
        
        elif opcao == 4:
            print('num 4 OK')
            break
        
        else:
            print("Opção inválida.")

# código principal
funcoes.boas_vindas()
main()