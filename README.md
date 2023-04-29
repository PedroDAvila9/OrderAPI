Flask API with PostgreSQL

This project is a simple Flask API with PostgreSQL that allows creating and fetching orders. The project contains a single endpoint /pedidos that accepts GET and POST requests.
Requirements

    Python 3
    Flask
    Flask-CORS
    psycopg2

Usage

To use the API, start the Flask server:

python app.py

Then, you can send GET and POST requests to http://127.0.0.1:5000/pedidos. For example, to fetch all orders, send a GET request to http://127.0.0.1:5000/pedidos.

To create a new order, send a POST request to http://127.0.0.1:5000/pedidos with a JSON payload containing the order information:

json

{
    "nome_cliente": "John",
    "sobrenome_cliente": "Doe",
    "endereco_cliente": "123 Main St",
    "telefone_cliente": "555-5555",
    "lanche": "hamburger",
    "bebida": "soda",
    "acompanhamento": "fries",
    "valor_total": 10.99
}

Contributions

    Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or send a pull request.