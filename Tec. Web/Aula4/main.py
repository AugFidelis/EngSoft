from flask import Flask, render_template, request

app = Flask(__name__)

frutas = []

@app.route('/', methods = ('GET', 'POST'))
def home_page():
    if(request.method == 'POST'):
        if(request.form.get('fruta')):
            frutas.append(request.form.get("fruta"))

    return render_template("index.html", frutas_do_html=frutas)

@app.route('/segundapagina', methods = ('GET', 'POST'))
def segunda_pagina():

    return render_template("index2.html", frutas_do_html=frutas)

if __name__ == '__main__':
    app.run(debug=True)