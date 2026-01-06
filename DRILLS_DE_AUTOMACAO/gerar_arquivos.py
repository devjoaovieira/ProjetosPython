import os
import random

# Lista de extensões que vamos simular
extensoes = {
    'relatorios': ['.pdf', '.docx', '.txt'],
    'imagens': ['.jpg', '.png', '.gif'],
    'planilhas': ['.xlsx', '.csv'],
    'sistema': ['.log', '.tmp', '.bat']
}

pasta_bagunca = "BAGUNCA_TESTE"

# Cria a pasta se não existir
if not os.path.exists(pasta_bagunca):
    os.makedirs(pasta_bagunca)

print(f"🌪️ Criando furacão na pasta '{pasta_bagunca}'...")

# Gera 100 arquivos vazios com nomes aleatórios
for i in range(1, 101):
    tipo = random.choice(list(extensoes.keys()))
    ext = random.choice(extensoes[tipo])
    nome_arquivo = f"arquivo_teste_{i}{ext}"
    
    caminho = os.path.join(pasta_bagunca, nome_arquivo)
    
    # Cria um arquivo vazio (touch)
    with open(caminho, 'w') as f:
        f.write("Este é um arquivo de teste para o Drill 1.")
    
print("✅ Bagunça criada com sucesso! Agora é com você.")