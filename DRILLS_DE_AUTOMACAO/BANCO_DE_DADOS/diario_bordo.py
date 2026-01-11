import sqlite3
import os
from datetime import datetime

#def criar_banco_dados():
    #conectar ao banco de dados (ou criar se não existir)
    
#criar caminho para o banco de dados
caminho_banco = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'diario_bordo.db')

#estabelecer a conexão
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()


#criar a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_tarefa TEXT,
    data TEXT
    )
    ''')

#input do usuário
nome_tarefa = input("Digite o nome da tarefa: ").upper().strip()
data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#inserir a tarefa no banco de dados
cursor.execute('''
               INSERT INTO tarefas (nome_tarefa, data)
               VALUES (?, ?)
                ''', (nome_tarefa, data))
#salvar (commit) as mudanças
conexao.commit()

print("\n--- 📖 LENDO O DIÁRIO ---")
#ler e mostrar todas as tarefas
cursor.execute('SELECT * FROM tarefas')
tarefas = cursor.fetchall()
for tarefa in tarefas:
    print(f"ID: {tarefa[0]} | Tarefa: {tarefa[1]} | Data: {tarefa[2]}")

#fechar a conexão
conexao.close()

