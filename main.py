#importando as bibliotecas 
import sqlite3
import json

# Conectando com o banco de dados
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Lendo a primeira linha da tabela
cursor.execute('SELECT * FROM CLIENTES LIMIT 1')
cliente = cursor.fetchone()

# Desconectando do banco de dados
conn.close()


    # Transformando a linha do banco de dados em um dicionário para ficar organizado no json
cliente_dict = {
        'id': cliente[0],
        'nome': cliente[1],
        'email': cliente[2],
        'telefone': cliente[3]
    }

    # Salvando e criando o arquivo json
with open('clientes.json', 'w') as json_file:
        json.dump(cliente_dict, json_file, indent=4)