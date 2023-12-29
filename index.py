from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configurações do banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname='teste1',
    user='postgres',
    password='postgres',
    host='localhost'
)

# Rota para receber a lista via REST API e inserir no banco de dados
@app.route('/insert_data', methods=['POST'])
def insert_data():
    try:
        data = request.get_json()

        cursor = conn.cursor()

        for item in data:
            name = item.get('name')
            corporationId = item.get('corporationId')
            ssn = item.get('ssn')
            isPaidInFull = item.get('isPaidInFull')

            cursor.execute(
                'INSERT INTO clientes (name, corporationId, ssn, isPaidInFull) VALUES (%s, %s, %s, %s)',
                (name, corporationId, ssn, isPaidInFull)
            )

        conn.commit()
        cursor.close()

        return jsonify({'message': 'Dados inseridos com sucesso no banco de dados!'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
