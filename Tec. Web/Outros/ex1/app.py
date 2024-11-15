from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    titulo = "Teste de flask"

    return render_template("index.html", tit = titulo)

@app.route('/pagina2')
def pagina2():
    itens = ["skibidi","edge","rizz"]

    return render_template('index2.html', lista = itens)

if(__name__ == '__main__'):
    app.run(debug=True)