# ESSE É O ARQUIVO PRINCIPAL QUE PUXA AS ROTAS DOS OUTROS ARQUIVOS .PY NA PASTA ROUTE

from flask import Flask

from routes.home import home_rota # Importa o grupo do home.py para que ele exista aqui
from routes.cliente import cliente_rota

app = Flask(__name__)

app.register_blueprint(home_rota) # Registra o grupo criado no home.py no arquivo principal
app.register_blueprint(cliente_rota, url_prefix='/clientes')

app.run(debug=True)