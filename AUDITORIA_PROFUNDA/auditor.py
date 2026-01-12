import sqlite3
import os

#criar banco de dados para guardar arquivos do escritorio de arquitetura
#o cliente quer que o relatorio contenha:

#Nome do arquivo (Ex: planta_térreo.cad)
#Extensão (Ex: .cad - para eles filtrarem depois)
#Tamanho em MB (Para acharem os arquivos pesados)
#Caminho Completo (Para saberem onde está o arquivo escondido)

def criar_banco_dados(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()
    cursor.execute ('''
            CREATE TABLE IF NOT EXISTS arquivos ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_arquivo TEXT,
            extensao TEXT,
            tamanho_mb REAL,
            caminho_completo TEXT
            )
            ''')
    return conexao, cursor

def auditor_pasta(conexao, pasta_alvo):
    cursor = conexao.cursor()
    for raiz, diretorios, arquivos in os.walk(pasta_alvo):
        for arquivo in arquivos:
            nome_arquivo, extensao = os.path.splitext(arquivo)
            caminho_completo = os.path.join(raiz, arquivo)
            tamanho_mb = os.path.getsize(caminho_completo) / (1024 * 1024)  # converter bytes para MB
            
            cursor.execute (''' 
                    INSERT into arquivos (nome_arquivo, extensao, tamanho_mb, caminho_completo)
                    VALUES (?, ?, ?, ?)
                    ''', (nome_arquivo, extensao, tamanho_mb, caminho_completo))
    conexao.commit()

def ler_dados(conexao):
    print("\n--- 📊 RELATÓRIO DE ARQUIVOS (TOP 10 MAIS PESADOS) ---")
    cursor = conexao.cursor()
    
    #ORDER BY tamanho_mb DESC LIMIT 10
    cursor.execute('''
            SELECT id, nome_arquivo, extensao, tamanho_mb
            FROM arquivos
            ORDER BY tamanho_mb DESC
            LIMIT 10
            ''')
    
    arquivos = cursor.fetchall()
    
    for item in arquivos:
        id_arquivo = item[0]
        nome = item[1]
        ext = item[2]
        tamanho = item[3]
        
        # Formatação bonita com f-string (:>10 alinha a direita)
        print(f"ID: {id_arquivo} | {nome}{ext} | {tamanho:.2f} MB")
        
def gerar_relatorio(conexao):
    cursor = conexao.cursor()
    
    sql = '''
            SELECT extensao, COUNT(*), SUM(tamanho_mb)
            FROM arquivos
            GROUP BY extensao
            ORDER BY SUM(tamanho_mb) DESC
            '''
            
    cursor.execute(sql)
    dados = cursor.fetchall()
    
    print("\n--- 📑 RELATÓRIO POR EXTENSÃO ---")
    for linha in dados:
        extensao = linha[0]
        quantidade = linha[1]
        tamanho_total = linha[2]
        
        print(f"Extensão: {extensao} | Quantidade: {quantidade} | Tamanho Total: {tamanho_total:.2f} MB")
    
        
#codigo principal 



if __name__ == "__main__":
    
    nome_banco = "auditoria_arquivos.db"
    pasta_alvo = input("Digite o nome da pasta a ser auditada: ").strip()
    caminho_pasta_alvo = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', pasta_alvo)
    
    #cria e conecta ao banco de dados
    conexao, cursor = criar_banco_dados(nome_banco)
    
    #audita a pasta alvo
    print(f"Iniciando auditoria na pasta: {pasta_alvo}...")
    auditor_pasta(conexao, caminho_pasta_alvo)
    
    #ler e mostrar os dados
    ler_dados(conexao)
    
    #finaliza
    print("Auditoria concluída. Dados salvos no banco de dados.")
    
    #exibe relatorio por extensao
    gerar_relatorio(conexao)
    conexao.close()