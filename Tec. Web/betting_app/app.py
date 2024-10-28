from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sports')   
def sports():
    return render_template('sports.html')

@app.route('/casino')
def casino():
    return render_template('casino.html')

if __name__ == '__main__':
    app.run(debug=True)
