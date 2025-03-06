# 🍕 Pizzaria - Backend

Backend da aplicação de gerenciamento de pizzaria, desenvolvido com **Flask** e **SQL Server**.
Esta API fornece um CRUD completo para gerenciamento de produtos com integração ao banco de dados.

## 🚀 Pré-requisitos

- Python 3.8+
- SQL Server (ou Docker para implantação em contêiner)
- [ODBC Driver 17 for SQL Server](https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server)
- pip (Gerenciador de pacotes Python)

## ⚙️ Configuração Local

### 1. Clone o repositório

```bash
git clone https://github.com/BarbasPedro/Pizzaria-backend.git
cd Pizzaria-backend
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Certifique-se de que o SQL Server esteja rodando e crie um banco de dados chamado `PIZZAIMPAC`. Atualize as configurações de conexão em `main.py` se necessário:

```python
server = "localhost\\SQLEXPRESS"  # Nome da instância do SQL Server
database = "PIZZAIMPAC"          # Nome do banco de dados
```

### 5. Execute a aplicação

```bash
python main.py
```

O servidor iniciará em `http://localhost:5000`

## 🛣️ Endpoints da API

### Produtos

| Método | Endpoint         | Descrição               |
| ------ | ---------------- | ----------------------- |
| GET    | `/produtos`      | Lista todos os produtos |
| POST   | `/produtos`      | Cria novo produto       |
| PUT    | `/produtos/<id>` | Atualiza produto por ID |
| DELETE | `/produtos/<id>` | Deleta produto por ID   |

### Exemplos de Corpo da Requisição

#### Criar/Atualizar Produto

```json
{
  "NomeProd": "Pizza Margherita",
  "PcVenda": 45.9,
  "Descricao": "Pizza italiana tradicional com molho de tomate, muçarela e manjericão",
  "Imagem": "url_da_imagem.jpg"
}
```

## 🔧 Estrutura do Banco de Dados

### TblProdutos

- `IdProd` (INT, Chave Primária)
- `NomeProd` (VARCHAR)
- `PcVenda` (DECIMAL)
- `Descricao` (TEXT)
- `ImgURL` (VARCHAR)

## 🔒 Tratamento de Erros

A API inclui tratamento de erros para operações no banco de dados e retorna códigos de status HTTP apropriados:

- 200: Sucesso
- 201: Criado com sucesso
- 500: Erro no servidor

## 🛠️ Tecnologias Utilizadas

- Flask: Framework web
- pyodbc: Conexão com SQL Server
- flask-cors: Suporte a CORS
- SQL Server: Banco de dados

## 👥 Como Contribuir

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/RecursoIncrivel`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona algum RecursoIncrivel'`)
4. Faça push para a branch (`git push origin feature/RecursoIncrivel`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## 📧 Contato

Pedro Barbas - [GitHub](https://github.com/BarbasPedro)

Link do Projeto: [https://github.com/BarbasPedro/Pizzaria-backend](https://github.com/BarbasPedro/Pizzaria-backend)
