import os
 # 1 - descobrir onde ele está (GPS)
pasta_atual = os.path.dirname(os.path.abspath(__file__))

 # 2 - Criar uma Pasta-Mãe chamada Projeto_Automático
nome_projeto = 'PROJETO_AUTOMATICO'
caminho_projeto = os.path.join(pasta_atual, nome_projeto)


 # 3 - Dentro dela, criar 3 subpastas
 
estrturas = [
    os.path.join(caminho_projeto, "CODIGO"),
    os.path.join(caminho_projeto, "DADOS"),
    os.path.join(caminho_projeto, "DADOS", "BRUTOS"),
    os.path.join(caminho_projeto, "DADOS", "LIMPOS"),
    os.path.join(caminho_projeto, "RELATORIOS")
    
]

for pasta in estrturas:
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        print(f'Pasta criada: {pasta}')
    else:
        print(f'ATENÇÃO - JÁ EXISTE: {pasta} ')

# 4 - criar arquivo readme.txt no pasta-raiz PROJETO_AUTOMATICO
txt = "README.txt"
caminho_txt = os.path.join(caminho_projeto, txt)

if not os.path.exists(caminho_txt):
    with open(caminho_txt, 'w') as f:
        f.write('Esse Projeto foi criado automaticamente pelo Python.')
    print('Arquivo README criado.')
