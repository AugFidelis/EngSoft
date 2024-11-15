from flask import Blueprint, render_template

home_rota = Blueprint('home', __name__, template_folder='templates')    #'home' representa o nome do grupo de rotas
# template_folder representa o local dos templates desse grupo

@home_rota.route('/') # na hora de se chamar a rota em blueprint, é o grupo.route ao invés de app.route
def pagina():
    return render_template('index.html')