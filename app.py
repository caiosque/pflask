from flask import Flask, render_template


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
    lista_alunos = [
    (1, "Lucas", 18, "Teresina"),
(2, "Mariana", 22, "Parnaíba"),
(3, "Rafael", 25, "Picos"),
(4, "Beatriz", 19, "Floriano"),
(5, "Gabriel", 21, "Piripiri"),
(6, "Camila", 24, "Campo Maior"),
(7, "João", 20, "Barras"),
(8, "Larissa", 27, "Oeiras"),
(9, "Pedro", 23, "São Raimundo Nonato"),
(10, "Amanda", 18, "Teresina"),
(11, "Matheus", 26, "Esperantina"),
(12, "Juliana", 21, "Altos"),
(13, "Felipe", 30, "Corrente"),
(14, "Isabela", 20, "União"),
(15, "Bruno", 28, "José de Freitas"),
(16, "Carolina", 23, "Batalha"),
(17, "Diego", 19, "Cocal"),
(18, "Letícia", 25, "Pedro II"),
(19, "André", 22, "Valença do Piauí"),
(20, "Fernanda", 29, "Teresina"),
(21, "Gustavo", 31, "Picos"),
(22, "Bianca", 18, "Parnaíba"),
(23, "Thiago", 24, "Piracuruca"),
(24, "Renata", 26, "Floriano"),
(25, "Vinícius", 20, "Campo Maior"),
(26, "Natália", 22, "Oeiras"),
(27, "Eduardo", 27, "Teresina"),
(28, "Sabrina", 19, "Barras"),
(29, "Rodrigo", 32, "São João do Piauí"),
(30, "Patrícia", 21, "Esperantina"),
(31, "Leonardo", 23, "Altos"),
(32, "Aline", 28, "União"),
(33, "Marcelo", 35, "Picos"),
(34, "Priscila", 24, "Parnaíba"),
(35, "Henrique", 18, "Teresina"),
(36, "Vanessa", 30, "José de Freitas"),
(37, "Ricardo", 26, "Piripiri"),
(38, "Jéssica", 22, "Pedro II"),
(39, "Samuel", 20, "Floriano"),
(40, "Daniela", 27, "Campo Maior"),
(41, "Alexandre", 33, "Corrente"),
(42, "Débora", 19, "Teresina"),
(43, "Maurício", 29, "Picos"),
(44, "Cristina", 25, "São Raimundo Nonato"),
(45, "Fábio", 21, "Barras"),
(46, "Tatiane", 23, "Parnaíba"),
(47, "Wesley", 28, "Cocal"),
(48, "Raquel", 20, "Oeiras"),
(49, "Igor", 24, "Piripiri"),
(50, "Elaine", 31, "Teresina")
]

    return render_template('aluno/lista.html',lista_alunos=lista_alunos)






if __name__ == '__main__':
    app.run(debug=True)

