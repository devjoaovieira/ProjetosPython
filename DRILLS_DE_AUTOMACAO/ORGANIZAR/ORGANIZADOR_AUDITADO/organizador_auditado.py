import sqlite3
from datetime import datetime
import os
import shutil

# Criar caminho para o banco de dados
caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(caminho_atual, 'organizador_auditado.db')

#caminho para a bagunça
pasta_raiz = os.path.dirname(os.path.dirname(caminho_atual))
dir_bagunca = os.path.join(pasta_raiz, 'BAGUNCA_TESTE')
arquivos = os.listdir(dir_bagunca)

# Estabelecer a conexão
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

# Criar a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS arquivos_auditados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_arquivo TEXT,
    destino_arquivo TEXT,
    data_auditoria TEXT
    )
    ''')

# DICIONARIOS DE DESTINO
pastas_destino = {
    "DOCS": os.path.join(caminho_atual, 'DB_ORGANIZADO', '01_DOCS'),
    "IMAGENS": os.path.join(caminho_atual,'DB_ORGANIZADO', '02_IMAGENS'),
    "DADOS": os.path.join(caminho_atual,'DB_ORGANIZADO', '03_DADOS'),
    "OUTROS": os.path.join(caminho_atual,'DB_ORGANIZADO', '99_OUTROS')
}

#extensões
doc_extensoes = (".txt", ".pdf", ".docx")
img_extensoes = (".jpg", ".png" )
dados_extensoes = (".xlsx", ".csv")

#criar pasta DB_ORGANIZADO se não existir
for caminho in pastas_destino.values():
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"✅ Pasta criada: {caminho}")
    else:
        print(f"📂 Pasta já existe: {caminho}")
        
#DEBUG: Sempre imprima para ver se o caminho está certo antes de tentar usar
print(f"📂 O Script está em: {caminho_atual}")
print()
print(f'🎯 O Banco de Dados está em: {caminho_banco}')
print()
print(f'🎯 As Pastas de Destino estão em: {pastas_destino}')

#veridicar se a pasta existe antes de tentar listar
if not os.path.exists(dir_bagunca):
    print("🚨 ERRO: A pasta BAGUNCA_TESTE não foi encontrada nesse caminho!")
else:
    #Só entra aqui se a pasta existir
    
    for arquivo in arquivos:
        origem = os.path.join(dir_bagunca, arquivo)
        
        nome_arquivo = arquivo
        data_auditoria = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #decidir o destino
        if arquivo.endswith(doc_extensoes):
            destino_arquivo = pastas_destino["DOCS"]
        elif arquivo.endswith(img_extensoes):
            destino_arquivo = pastas_destino["IMAGENS"]
        elif arquivo.endswith(dados_extensoes):
            destino_arquivo = pastas_destino["DADOS"]
        else:
            destino_arquivo = pastas_destino["OUTROS"]
        # Monta o caminho final com o nome do arquivo
        caminho_destino = os.path.join(destino_arquivo, arquivo)
        # Move (Sem precisar verificar a pasta de novo!)
        # Tenta fazer a operação arriscada (Mover + Gravar)
        try:
            # 1. Tenta Mover
            shutil.move(origem, caminho_destino)
            
            # 2. Se a linha de cima não deu erro, Grava no Banco
            cursor.execute('''
                INSERT INTO arquivos_auditados (nome_arquivo, destino_arquivo, data_auditoria)
                VALUES (?, ?, ?)
            ''', (nome_arquivo, destino_arquivo, data_auditoria))
            
            # 3. Salva
            conexao.commit()
            print(f"✅ Sucesso: {arquivo} -> {os.path.basename(destino_arquivo)}")

        except Exception as e:
            # Se der qualquer erro (arquivo em uso, etc), cai aqui
            print(f"❌ ERRO ao processar {arquivo}: {e}")
            # O script NÃO para, ele vai para o próximo arquivo do loop

    
print("\n--- 📖 LENDO O BANCO DE DADOS DE AUDITORIA ---")
#ler e mostrar todas as auditorias
cursor.execute('SELECT * FROM arquivos_auditados')
auditoria = cursor.fetchall()
for registro in auditoria:
    print(f"ID: {registro[0]} | Arquivo: {registro[1]} | Destino: {registro[2]} | Data Auditoria: {registro[3]}")
#fechar a conexão
conexao.close()

    