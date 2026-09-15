from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/aluno')
def listar_aluno():
    # Conectar ao banco de dados SQLite
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Executar consulta SQL
    cursor.execute("SELECT id, nome, idade, cidade FROM aluno")
    
    # Obtém todos os registros
    lista = cursor.fetchall()
    
    # Fecha a conexão com o banco de dados
    conn.close()
    
    # Indentação e nome da função corrigidos
    return render_template("aluno/lista.html", lista=lista)

if __name__ == '__main__':
    app.run(debug=True)