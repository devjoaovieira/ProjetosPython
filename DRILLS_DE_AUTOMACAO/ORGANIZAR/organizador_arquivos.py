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

import os
import shutil

# 1. Descobre onde o script 'organizador_arquivos.py' está rodando AGORA
pasta_atual_do_script = os.path.dirname(os.path.abspath(__file__))

# 2. Volta um nível (para sair da pasta 'ORGANIZAR' e ir para 'DRILLS_DE_AUTOMACAO')
pasta_mae_drills = os.path.dirname(pasta_atual_do_script)

# 3. Agora monta o caminho para a bagunça (que é vizinha)

dir_bagunca = os.path.join(pasta_mae_drills, 'BAGUNCA_TESTE')
dest_docs = os.path.join(pasta_mae_drills, 'ORGANIZAR', '01_DOCS')
dest_imagens = os.path.join(pasta_mae_drills, 'ORGANIZAR', '02_IMAGENS')
dest_dados = os.path.join(pasta_mae_drills, 'ORGANIZAR', '03_DADOS' )
dest_outros = os.path.join(pasta_mae_drills, 'ORGANIZAR', '99_OUTROS')

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
    
    for arquivo in os.listdir(dir_bagunca):
        caminho_completo_entrada = os.path.join(dir_bagunca, arquivo)
        
        if arquivo.endswith(doc_extensoes): # 1 - MOVER AQRUIVOS DE DOCUMENTOS
            #precisa montar caminho completo para identificar
            caminho_completo_destino = os.path.join(dest_docs, arquivo)

            # Cria a pasta de destino se não existir
            if not os.path.exists(dest_docs):
                os.makedirs(dest_docs)
            shutil.move(caminho_completo_entrada, caminho_completo_destino)
            print(f"✅ Movido: {arquivo}")    
            print()
            
        elif arquivo.endswith(img_extensoes): # 2 - MOVER AQRUIVOS DE IMAGEM
            caminho_completo_destino = os.path.join(dest_imagens, arquivo)
            
            if not os.path.exists(dest_imagens):
                os.makedirs(dest_imagens)
            shutil.move(caminho_completo_entrada, caminho_completo_destino)
            print(f"✅ Movido: {arquivo}")
            print()
            
        elif arquivo.endswith(dados_extensoes): # 3 - MOVER AQRUIVOS DE DADOS
            caminho_completo_destino = os.path.join(dest_dados, arquivo)
                
            if not os.path.exists(dest_dados):
                os.makedirs(dest_dados)
            shutil.move(caminho_completo_entrada, caminho_completo_destino)
            print(f"✅ Movido: {arquivo}")
            print()
                
        else: # 99 - MOVER OUTROS ARQUIVOS
            caminho_completo_destino = os.path.join(dest_outros, arquivo)
            if not os.path.exists(dest_outros):
                os.makedirs(dest_outros)
            shutil.move(caminho_completo_entrada, caminho_completo_destino)
            print(f"✅ Movido: {arquivo}")
            print()


#==================================================================================================================


#separar subpastas de acordo com a extensão: 

#01_DOCS (para .pdf, .docx, .txt)
#02_IMAGENS (para .jpg, .png)
#03_DADOS (para .xlsx, .csv)
#99_OUTROS (o resto)




#==========================ERROSS==========================
#não usar "r" antes do caminho do diretório, assim o python interpreta sequencias como codigo especial