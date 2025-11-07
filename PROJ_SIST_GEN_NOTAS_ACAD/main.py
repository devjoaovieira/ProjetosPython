from funcoes import entrada_numerica, opcoes_do_menu

#codigo principal
#ATENÇÃO - A lista Turmas devem ser separadas por matéria cursada - É necessario descobrir a lógica para fazer isso

print('GERENCIADOR DE NOTAS ACADÊMICAS\n')
print('1. Adicionar Novo Aluno')
print('2. Lançar Notas do Aluno')
print('3. Visualizar Boletim')
print('4. Sair')
print()

resp = entrada_numerica(input('Escolha um número para ser começar: '))
opcoes_do_menu(resp)