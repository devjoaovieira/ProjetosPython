import os

#caminho de pastas para testes
#caminho_atual = os.path.dirname(os.path.abspath(__file__))
#caminho_raiz = os.path.abspath(os.path.join(caminho_atual, '..', 'DRILLS_DE_AUTOMACAO'))
caminho_desejado = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DRILLS_DE_AUTOMACAO'))


# O os.walk gera 3 coisas a cada passo que ele dá:
# 1. atual: Onde ele está agora (nome da pasta)
# 2. subpastas: Quais pastas tem aqui dentro para ele descer depois
# 3. arquivos: Quais arquivos soltos tem aqui

print('-' * 40)
print('Estrutura de pastas e arquivos:')
print('-' * 40)
for atual, subpastas, arquivos in os.walk(caminho_desejado):
    print(f'Estamos em: {atual}')
    print(f'Temos as subpastas: {subpastas}')
    print(f'Temos os arquivos: {arquivos}')
    print()  # Linha em branco para melhor visualização