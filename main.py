from flask import Flask, jsonify, request
import pyodbc
from flask_cors import CORS

# Configurações do Flask
app = Flask(__name__)
CORS(app)

# Configurações do banco de dados
server = "localhost\\SQLEXPRESS"  # Nome da instância do SQL Server
database = "PIZZAIMPAC"           # Nome do banco de dados
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"  # Autenticação do Windows
)


# Função para conectar ao banco de dados
def get_db_connection():
    return pyodbc.connect(conn_str)


# Rota para retornar a lista de produtos
@app.route('/produtos', methods=['GET'])
def get_produtos():
    try:
        # Conectar ao banco de dados
        conn = get_db_connection()
        cursor = conn.cursor()

        # Executar a consulta SQL
        cursor.execute("SELECT * FROM TblProdutos")

        # Converter os resultados em uma lista de dicionários
        produtos = []
        for row in cursor:
            produto = {
                "IdProd": row.IdProd,
                "NomeProd": row.NomeProd,
                "PcVenda": float(row.PcVenda),
                "Descricao": row.Descricao,
                "Imagem": row.ImgURL
            }
            produtos.append(produto)

        # Fechar a conexão
        cursor.close()
        conn.close()

        # Retornar os produtos em formato JSON
        return jsonify(produtos)
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500


# Rota para atualizar um produto existente
@app.route('/produtos/<int:id>', methods=['PUT'])
def update_produto(id):
    try:
        # Obter os dados do corpo da requisição
        data = request.get_json()
        nome = data.get("NomeProd")
        preco = data.get("PcVenda")
        descricao = data.get("Descricao")
        imagem = data.get("Imagem")

        # Conectar ao banco de dados
        conn = get_db_connection()
        cursor = conn.cursor()

        # Executar a atualização no banco de dados
        cursor.execute("""
            UPDATE TblProdutos
            SET NomeProd = ?,
            PcVenda = ?,
            Descricao = ?,
            ImgURL = ?
            WHERE IdProd = ?
            """,
            (nome, preco, descricao, imagem, id)
        )
        conn.commit()

        # Fechar a conexão
        cursor.close()
        conn.close()

        # Retornar uma mensagem de sucesso
        return jsonify({"message": "Produto atualizado com sucesso!"}), 200
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500


# Rota para adicionar um novo produto
@app.route('/produtos', methods=['POST'])
def add_produto():
    try:
        # Obter os dados do corpo da requisição
        data = request.get_json()
        nome = data.get("NomeProd")
        preco = data.get("PcVenda")
        descricao = data.get("Descricao")
        imagem = data.get("Imagem")

        # Conectar ao banco de dados
        conn = get_db_connection()
        cursor = conn.cursor()

        # Executar a inserção no banco de dados
        cursor.execute(
            "INSERT INTO TblProdutos (NomeProd, PcVenda, Descricao, ImgURL) VALUES (?, ?, ?, ?)",
            (nome, preco, descricao, imagem)
        )
        conn.commit()

        # Fechar a conexão
        cursor.close()
        conn.close()

        # Retornar uma mensagem de sucesso
        return jsonify({"message": "Produto adicionado com sucesso!"}), 201
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500


# Rota para excluir um produto
@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    try:
        # Conectar ao banco de dados
        conn = get_db_connection()
        cursor = conn.cursor()

        # Executar a exclusão no banco de dados
        cursor.execute("DELETE FROM TblProdutos WHERE IdProd = ?", (id,))
        conn.commit()

        # Fechar a conexão
        cursor.close()
        conn.close()

        # Retornar uma mensagem de sucesso
        return jsonify({"message": "Produto excluído com sucesso!"}), 200
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500


# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
