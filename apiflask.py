from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    dbname="YOUR DB NAME",
    user="USER DB",
    password="PASSWORD DB",
    host="HOST DB",
    port="PORT DB")
print("Conexão com o banco de dados estabelecida com sucesso!")



@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM pedidos")
        rows = cur.fetchall()
        pedidos = []
        for row in rows:
            pedido = {
                'id': row[0],
                'nome_cliente': row[1],
                'sobrenome_cliente': row[2],
                'endereco_cliente': row[3],
                'telefone_cliente': row[4],
                'lanche': row[5],
                'bebida': row[6],
                'acompanhamento': row[7],
                'valor_total': row[8]
            }
            pedidos.append(pedido)
        return jsonify(pedidos)
    elif request.method == 'POST':
        pedido = request.json
        nome_cliente = pedido['nome_cliente']
        sobrenome_cliente = pedido['sobrenome_cliente']
        endereco_cliente = pedido['endereco_cliente']
        telefone_cliente = pedido['telefone_cliente']
        lanche = pedido['lanche'] if 'lanche' in pedido else None
        bebida = pedido['bebida'] if 'bebida' in pedido else None
        acompanhamento = pedido['acompanhamento'] if 'acompanhamento' in pedido else None
        valor_total = pedido['valor_total']
    try:
        cur = conn.cursor()
        cur.execute(""" INSERT INTO pedidos (nome_cliente, sobrenome_cliente, endereco_cliente, telefone_cliente, lanche, bebida, acompanhamento, valor_total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (nome_cliente, sobrenome_cliente, endereco_cliente, telefone_cliente, lanche, bebida, acompanhamento, valor_total))
        conn.commit()
        return jsonify({'message': 'Pedido criado com sucesso'})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': 'não foi possível criar o pedido: {}'.format(str(e))})



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
