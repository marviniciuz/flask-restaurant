# 🍽️ Flask Restaurant control

Um sistema de gestão de restaurantes leve e simples, desenvolvido com **Flask** e **HTMX**.

O objetivo deste projeto é demonstrar como criar aplicações web interativas e responsivas utilizando **Server-Side Rendering (SSR)**, eliminando a complexidade de frameworks JavaScript pesados (como React/Vue) para operações CRUD simples.

![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)
![Badge Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Badge Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey?style=for-the-badge&logo=flask)
![Badge HTMX](https://img.shields.io/badge/HTMX-1.9-orange?style=for-the-badge)


## 🛠️ Tecnologias Utilizadas no projeto

* **Back-end:** Python, Flask, SQLAlchemy (SQLite).
* **Front-end:** HTML5, Materialize CSS (Design Responsivo).
* **Interatividade:** HTMX (Requisições AJAX declarativas direto no HTML).
* **Testes:** Pytest, Pytest-HTML.

## ✨ Funcionalidades

* ✅ **Cadastro de Restaurantes:** Adição sem recarregar a página.
* ✅ **Busca em Tempo Real:** Filtragem dinâmica (`debounce`) enquanto digita.
* ✅ **Exclusão:** Remoção de itens da lista via requisição DELETE.
* ✅ **Banco de Dados:** Persistência automática em SQLite.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Python 3.x instalado.

### Passo a Passo

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)
    cd NOME-DO-REPO
    ```

2.  **Crie o ambiente virtual**
    ```bash
    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate

    # Windows (PowerShell)
    python -m venv venv
    .\venv\Scripts\Activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute:**
    ```bash
    python app.py
    ```
    O servidor iniciará em `http://127.0.0.1:5000`.

## Testes 

O projeto conta com testes de integração utilizando **Pytest**.

Para rodar os testes simples:
```bash
pytest
```