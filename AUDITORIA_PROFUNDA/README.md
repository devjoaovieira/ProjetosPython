# 📂 Auditor de Arquivos (Deep Audit)

> Um script de automação em Python para análise profunda de diretórios e consumo de armazenamento.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)

## 📝 Sobre o Projeto

Este projeto foi desenvolvido para atender uma demanda simulada de um **Escritório de Arquitetura**. O objetivo era mapear servidores lotados, identificando arquivos pesados e gerando relatórios de consumo por tipo de arquivo, sem a necessidade de instalar softwares complexos.

O script percorre recursivamente pastas e subpastas (usando `os.walk`), coleta metadados e armazena tudo em um banco de dados local para geração de inteligência de dados.

## 🚀 Funcionalidades

- [x] **Varredura Recursiva:** "Mergulha" em todas as subpastas do diretório alvo.
- [x] **Banco de Dados Automático:** Cria e estrutura um arquivo `.db` (SQLite) automaticamente.
- [x] **Conversão de Unidades:** Calcula e converte bytes para Megabytes (MB) para fácil leitura.
- [x] **Relatório "Top 10":** Exibe os 10 arquivos mais pesados encontrados.
- [x] **Relatório Gerencial:** Agrupa arquivos por extensão (Ex: `.cad`, `.jpg`, `.pdf`) somando a quantidade e o tamanho total ocupado.

## 🛠️ Tecnologias Utilizadas

* **Python 3** - Linguagem base.
* **SQLite3** - Banco de dados SQL embutido (Nativo).
* **OS Module** - Manipulação de sistema de arquivos e caminhos (Nativo).

## ⚙️ Como Executar

### Pré-requisitos
Você precisa ter o [Python](https://www.python.org/) instalado em sua máquina. Não é necessário instalar bibliotecas externas (`pip install`), pois o script utiliza apenas bibliotecas nativas.

### Passo a Passo

1. Clone este repositório ou baixe o arquivo `auditor.py`.
2. Certifique-se de que a pasta que você deseja auditar esteja acessível.
3. Abra o terminal na pasta do projeto e execute:

```bash
python auditor.py
```

Quando solicitado, digite o nome da pasta alvo.📊 

Exemplo de Saída (Terminal)

```bash
Auditoria concluída. Dados salvos no banco de dados.

--- 📊 RELATÓRIO DE ARQUIVOS (TOP 10 MAIS PESADOS) ---
ID: 45 | projeto_shopping.cad | 150.40 MB
ID: 12 | render_fachada.psd | 89.20 MB
ID: 03 | video_apresentacao.mp4 | 55.10 MB
...

--- 📑 RELATÓRIO POR EXTENSÃO ---
Extensão: .cad | Quantidade: 140 | Tamanho Total: 520.00 MB
Extensão: .jpg | Quantidade: 500 | Tamanho Total: 120.50 MB
Extensão: .txt | Quantidade: 50  | Tamanho Total: 0.05 MB
```

## 🗂️ Estrutura do Banco de Dados

O script gera um arquivo `auditoria_arquivos.db` com a seguinte tabela:

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | INTEGER | Identificador único |
| `nome_arquivo` | TEXT | Nome do arquivo |
| `extensao` | TEXT | Extensão (ex: .pdf) |
| `tamanho_mb` | REAL | Tamanho calculado em MB |
| `caminho_completo` | TEXT | Localização exata no disco |


## ✒️ Autor
Desenvolvido por `João Vieira` durante a jornada de aprendizado em Automação com Python.