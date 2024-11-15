from flask import Blueprint, render_template
from database.cliente import CLIENTES # importa o dicionário CLIENTES do arquivo na pasta database

cliente_rota = Blueprint('cliente', __name__)

#     Rota de clientes (GET recebe dados do servidor, POST envia dados pro servidor, PUT atualiza dados e DELETE deleta dados)

#     - /clientes/ (GET) - Listar os clientes
#     - /clientes/ (POST) - Inserir o cliente no servidor
#     - /clientes/new (GET) - Renderizar o formulário para criar um cliente
#     - /clientes/<id> (GET) - Obter os dados de um cliente
#     - /clientes/<id>/edit (GET)- Renderizar um formulário para editar um cliente
#     - /clientes/<id>/update (PUT) - Atualizar os dados do cliente
#     - /clientes/<id>/delete (DELETE) -Deleta o registro do usuario

# No caso dos POST, PUT e DELETE não tem render_template pq eles não precisam de uma página, eles só modificam dados

@cliente_rota.route('/')
def lista_clientes():
    # listar os clientes
    return render_template('lista_clientes.html', clientes = CLIENTES)

@cliente_rota.route('/', methods=['POST']) 
def inserir_cliente():
    # inserir os dados do cliente no banco de dados
    pass

@cliente_rota.route('/new') # por padrão as rotas são GET, nem precisa mencionar
def form_cliente():
    # formulario para cadastrar um cliente
    return render_template('form_cliente.html')

@cliente_rota.route('/<int:cliente_id>') #isso faz aparecer a variável descrita depois do nome na barra (ex: /cliente/123 )
def detalhe_cliente(cliente_id): #quando o usuário acessar a rota 'cliente_id' ela será recebida aqui
    # exibir detalhes do cliente
    return render_template('detalhe_cliente.html')

@cliente_rota.route('/<int:cliente_id>/edit') 
def form_edit_cliente(cliente_id): 
    # formulario para editar um cliente
    return render_template('form_edit_cliente.html')

@cliente_rota.route('/<int:cliente_id>/update', methods=['PUT']) 
def atualizar_cliente(cliente_id): 
    # atualizar informações do cliente
    pass 

@cliente_rota.route('/<int:cliente_id>/delete', methods=['DELETE']) 
def deletar_cliente(cliente_id): 
    # deletar informações do cliente
    pass 
    