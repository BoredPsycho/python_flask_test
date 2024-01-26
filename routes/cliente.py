from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    #listar os clientes
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    #inserir os dados do cliente

    data = request.json #payload do envio

    novo_usuario = {
        'id': len(CLIENTES)+1,
        'nome': data['nome'],
        'email': data['email'],
    }

    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    #formulario pra criar um cliente
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    #exibir detalhes do cliente
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    #formulario pra editar um cliente

    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/updadte', methods=['PUT'])
def atualizar_cliente(cliente_id):
    #atualizar informacoes cliente
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    #deletar informacoes cliente
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]
    return {'deleted':'ok'}