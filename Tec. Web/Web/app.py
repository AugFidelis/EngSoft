from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def paginaPrincipal():
    frutas = ["Maçã", "Banana", "Abacaxi"]
    return render_template('index.html', frutashtml=frutas)

if __name__ == '__main__':
    app.run(debug=True)