from flask import Flask, render_template, request
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')

@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

@app.route('/aluno')
def lista_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/professor')
def lista_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista=lista)

@app.route('/turma')
def lista_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista=lista)

@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    dados = f"Usuário: {usuario}, Senha: {senha}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/desafio', methods=['GET', 'POST'])
def desafio():
    if request.method == 'GET':
        return render_template('desafio/desafio.html')
    nome = request.form['nome']
    data = request.form['data de nascimento']
    cpf = request.form['cpf']
    nome_da_mae = request.form['nome da mãe']
    dados = f"Nome: {nome}, Data de Nascimento: {data}, CPF: {cpf}, Nome da Mãe: {nome_da_mae}"
    return render_template('desafio/desafio.html', valor_recebido=dados)







if __name__ == '__main__':
    app.run(debug=True)