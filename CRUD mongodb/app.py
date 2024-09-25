from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

# Conectar ao MongoDB
client = MongoClient('mongodb+srv://leopxz:5TsrA1U0D74YfMSt@aplicacao.zht7j.mongodb.net/?retryWrites=true&w=majority&appName=aplicacao')
db = client['agenda']
contacts = db.contacts

# Página principal (listar contatos)
@app.route('/')
def index():
    all_contacts = contacts.find()
    return render_template('index.html', contacts=all_contacts)

# Página para criar um novo contato
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        contact = {
            "nome": request.form['name'],
            "cpf": request.form['cpf'],
            "idade": int(request.form['idade']),
            "email": request.form['email'],
            "telefone": request.form['telefone'],
            "endereco": {
                "rua": request.form['rua'],
                "numero": int(request.form['numero']),
                "cidade": request.form['cidade'],
                "estado": request.form['estado'],
                "cep": request.form['cep']
            },
            "data_de_nascimento": request.form['data_de_nascimento'],
            "data_cadastro": datetime.now()
        }
        contacts.insert_one(contact)
        return redirect(url_for('index'))
    return render_template('create.html')

# Página para mostrar detalhes de um contato
@app.route('/details/<contact_id>')
def details(contact_id):
    contact = contacts.find_one({'_id': ObjectId(contact_id)})
    return render_template('details.html', contact=contact)


# Página para atualizar um contato
@app.route('/update/<contact_id>', methods=['GET', 'POST'])
def update(contact_id):
    contact = contacts.find_one({'_id': ObjectId(contact_id)})
    if request.method == 'POST':
        updated_contact = {
            "nome": request.form['name'],
            "cpf": request.form['cpf'],
            "idade": int(request.form['idade']),
            "email": request.form['email'],
            "telefone": request.form['telefone'],
            "endereco": {
                "rua": request.form['rua'],
                "numero": int(request.form['numero']),
                "cidade": request.form['cidade'],
                "estado": request.form['estado'],
                "cep": request.form['cep']
            },
            "data_de_nascimento": request.form['data_de_nascimento'],
        }
        contacts.update_one({'_id': ObjectId(contact_id)}, {'$set': updated_contact})
        return redirect(url_for('index'))
    return render_template('update.html', contact=contact)

# Deletar um contato
@app.route('/delete/<contact_id>')
def delete(contact_id):
    contacts.delete_one({'_id': ObjectId(contact_id)})
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
