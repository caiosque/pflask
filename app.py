
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return "<h1>Sobre nós</h1><p>Esta é a página sobre.</p>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1><p>Entre em contato conosco.</p>"


if __name__ == "__main__":
    app.run(debug=True)
