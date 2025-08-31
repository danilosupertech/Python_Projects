# 🐍 API REST com Python (Flask + SQLite)

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![REST](https://img.shields.io/badge/Style-REST-orange)

Este projeto demonstra, de forma simples e didática, uma **API RESTful** em Python usando **Flask** e **SQLite** para realizar operações **CRUD** (Create, Read, Update, Delete) de usuários. Ele serve como base de estudo para quem está começando em **desenvolvimento backend** e quer entender como sistemas se comunicam por **HTTP** trocando dados em **JSON**.

Repositório: `https://github.com/danilosupertech/Python_Projects.git`

---

## 🎯 Objetivo do Projeto
- Mostrar a importância de APIs REST na comunicação entre sistemas.
- Expor endpoints HTTP para criar, listar, buscar, atualizar e deletar usuários.
- Servir de template inicial para projetos Flask simples com persistência em SQLite.

---

## ⚙️ Tecnologias e Ferramentas Recomendadas
- **Python 3.10+** 🐍
- **Flask 2.x** 🌐 (framework web minimalista)
- **SQLite** 🗄️ (banco de dados leve embutido)
- **JSON** 📦 (formato de troca de dados)
- **Postman** 📬 (testar requisições HTTP de forma visual)
- **VS Code / PyCharm** 💻 (IDE recomendadas)
- **Git** 🧰 (controle de versão)

---

## 📌 Por que REST é importante?
**REST (Representational State Transfer)** é um estilo arquitetural que define como sistemas conversam via HTTP. Ele é amplamente adotado porque:
- ✅ **Simplicidade**: usa métodos HTTP conhecidos (`GET`, `POST`, `PUT`, `DELETE`).
- ✅ **Interoperabilidade**: independente de linguagem e plataforma.
- ✅ **Escalabilidade**: recursos bem definidos e sem estado (stateless).
- ✅ **Facilidade de integração**: frontends web/mobile, automações e serviços podem consumir a API.

---

## 🚀 Como rodar localmente

> **Pré-requisitos**: Python 3.10+ instalado e acesso ao terminal/PowerShell.

1) **Clone o repositório**
```bash
git clone https://github.com/danilosupertech/Python_Projects.git
cd Python_Projects
```

2) **(Opcional, recomendado) Crie e ative um ambiente virtual**
```bash
python -m venv venv

# Windows (PowerShell)
venv\Scriptsctivate

# Linux/Mac
source venv/bin/activate
```

3) **Instale as dependências**
```bash
pip install flask
```

4) **Crie a base de dados (tabela `users`)**  
Crie um arquivo `create_db.py` com o conteúdo abaixo e execute-o **uma vez**:
```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

conn.commit()
cursor.close()
conn.close()
print("Banco de dados e tabela criados com sucesso!")
```

Execute:
```bash
python create_db.py
```

5) **Execute a aplicação Flask**  
Certifique-se de que o arquivo com os endpoints (ex.: `app.py`) esteja no diretório atual e então rode:
```bash
python app.py
```
Servidor disponível em: **http://127.0.0.1:5500** (equivalente a **http://localhost:5500**).

---

## 🔌 Endpoints da API

> **Formato de dados:** JSON  
> **Headers recomendados:** `Content-Type: application/json`

### 1. Listar todos os usuários
**GET** `/users`  
**Resposta (200):**
```json
[
  { "id": 1, "name": "John Doe", "email": "johndoe@example.com" },
  { "id": 2, "name": "Jane Smith", "email": "janesmith@example.com" }
]
```

### 2. Obter usuário por ID
**GET** `/users/<id>`  
Exemplo: `GET http://127.0.0.1:5500/users/1`  
**Resposta (200):**
```json
{ "id": 1, "name": "John Doe", "email": "johndoe@example.com" }
```
**Se não encontrado (404):**
```json
{ "message": "User not found" }
```

### 3. Criar novo usuário
**POST** `/users`  
**Body (JSON):**
```json
{
  "name": "Danilo Belo",
  "email": "danilo@tech.com"
}
```
**Resposta (201):**
```json
{
  "message": "User created successfully",
  "user": { "id": 3, "name": "Danilo Belo", "email": "danilo@tech.com" }
}
```

### 4. Atualizar usuário existente
**PUT** `/users/<id>`  
Exemplo: `PUT http://127.0.0.1:5500/users/2`  
**Body (JSON):**
```json
{
  "name": "Jane Silva",
  "email": "janesilva@example.com"
}
```
**Resposta (200):**
```json
{
  "message": "User updated successfully",
  "user": { "id": 2, "name": "Jane Silva", "email": "janesilva@example.com" }
}
```

### 5. Deletar usuário
**DELETE** `/users/<id>`  
Exemplo: `DELETE http://127.0.0.1:5500/users/3`  
**Resposta (200):**
```json
{ "message": "User deleted successfully" }
```

### 6. Visualização HTML (navegador)
**GET** `/users/html`  
Exibe uma lista simples em HTML com os usuários cadastrados.  
Exemplo: `http://127.0.0.1:5500/users/html`

---

## 🧪 Testando com Postman

1. Abra o **Postman** e crie uma **Collection** (ex.: `Python API REST`).  
2. Adicione as requisições:
   - `GET http://127.0.0.1:5500/users`
   - `GET http://127.0.0.1:5500/users/1`
   - `POST http://127.0.0.1:5500/users` (Body → raw → JSON, conforme exemplo)
   - `PUT http://127.0.0.1:5500/users/1` (Body → raw → JSON, conforme exemplo)
   - `DELETE http://127.0.0.1:5500/users/1`
3. Envie cada requisição e valide as respostas JSON renderizadas pelo Postman.

> Dica: Instale uma extensão de **JSON Viewer** no navegador para visualizar melhor as respostas acessando diretamente os endpoints (ex.: `/users`).

---

## 🧰 Estrutura sugerida de arquivos
```
Python_Projects/
├─ app.py            # Código Flask com os endpoints
├─ create_db.py      # Script para criar a base SQLite e a tabela users
├─ example.db        # Banco de dados SQLite (gerado após rodar create_db.py)
└─ README.md         # Este manual
```

---

## ❗ Troubleshooting (Windows/PowerShell)
- **curl vs PowerShell**: `curl` no PowerShell pode ser alias de `Invoke-WebRequest`. Prefira o **Postman** para testes, ou chame explicitamente `C:\Windows\System32\curl.exe`.  
- **Erro 415 / Content-Type**: garanta que o header `Content-Type: application/json` está definido e que o corpo é **JSON válido**.  
- **Tabela inexistente**: rode `python create_db.py` antes de iniciar o servidor.

---

## 🤝 Contribuição
Contribuições são bem-vindas! Abra uma **Issue** ou envie um **Pull Request** com melhorias, correções ou novas funcionalidades.

---

## 👤 Autor
**Danilo Côrtes Gonçalves**  
GitHub: https://github.com/danilosupertech
