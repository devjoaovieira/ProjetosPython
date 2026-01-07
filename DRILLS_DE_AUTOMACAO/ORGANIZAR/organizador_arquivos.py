import os
import shutil

#criar subpastas
def criar_pastas(pasta_raiz_para_guardar):
    pastas = [
        "01_DOCS", #(para .pdf, .docx, .txt)
        "02_IMAGENS", #(para .jpg, .png)
        "03_DADOS", #(para .xlsx, .csv)
        "99_OUTROS" #(o resto)
        ]
    for pasta in pastas:
        caminho = os.path.join(pasta_raiz_para_guardar, pasta)
        if not os.path.exists(caminho):
            os.makedirs(caminho)
            print(f"✅ Pasta criada: {pasta}")

# ==== DEFINIÇÃO DE CAMINHOS =====
# 1. Descobre onde o script 'organizador_arquivos.py' está rodando AGORA
pasta_atual_do_script = os.path.dirname(os.path.abspath(__file__))

# 2. Volta um nível (para sair da pasta 'ORGANIZAR' e ir para 'DRILLS_DE_AUTOMACAO')
pasta_mae_drills = os.path.dirname(pasta_atual_do_script)

# 3. Agora monta o caminho para a bagunça (que é vizinha)
dir_bagunca = os.path.join(pasta_mae_drills, 'BAGUNCA_TESTE')

# ==== DICIONÁRIOS DE DESTINO =====
pastas_destino = {
    "DOCS": os.path.join(pasta_mae_drills, 'ORGANIZAR', '01_DOCS'),
    "IMAGENS": os.path.join(pasta_mae_drills, 'ORGANIZAR', '02_IMAGENS'),
    "DADOS": os.path.join(pasta_mae_drills, 'ORGANIZAR', '03_DADOS'),
    "OUTROS": os.path.join(pasta_mae_drills, 'ORGANIZAR', '99_OUTROS')
}

# --- 2. PREPARAÇÃO DO TERRENO (Cria pastas UMA VEZ só) ---
print("🏗️ Verificando infraestrutura de pastas...")
for caminho in pastas_destino.values():
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"✅ Pasta criada: {caminho}")

# --- DEBUG: Sempre imprima para ver se o caminho está certo antes de tentar usar ---
print(f"📂 O Script está em: {pasta_atual_do_script}")
print()
print(f"🎯 A Bagunça está em: {dir_bagunca}")

#tupla de extensões para verificar todas de uma vez
doc_extensoes = (".txt", ".pdf", ".docx")
img_extensoes = (".jpg", ".png" )
dados_extensoes = (".xlsx", ".csv")

#Verificar se a pasta existe antes de tentar listar


if not os.path.exists(dir_bagunca):
    print("🚨 ERRO: A pasta BAGUNCA_TESTE não foi encontrada nesse caminho!")
else:
    #Só entra aqui se a pasta exisitir
    arquivos = os.listdir(dir_bagunca)
    for arquivo in arquivos:
        origem = os.path.join(dir_bagunca, arquivo)
        
        if arquivo.endswith(doc_extensoes): # 1 - MOVER AQRUIVOS DE DOCUMENTOS
            #precisa montar caminho completo para identificar
            destino_final = pastas_destino["DOCS"]
            
        elif arquivo.endswith(img_extensoes): # 2 - MOVER AQRUIVOS DE IMAGEM
            destino_final = pastas_destino["IMAGENS"]
            
            
        elif arquivo.endswith(dados_extensoes): # 3 - MOVER AQRUIVOS DE DADOS
            destino_final = pastas_destino["DADOS"]
                
                
        else: # 99 - MOVER OUTROS ARQUIVOS
            destino_final = pastas_destino["OUTROS"]
        
        # Monta o caminho final com o nome do arquivo
        caminho_destino = os.path.join(destino_final, arquivo)
        
        # Move (Sem precisar verificar a pasta de novo!)
        shutil.move(origem, caminho_destino)
        print(f"📦 {arquivo} -> {os.path.basename(destino_final)}")
        
print('Organização Concluída!')
