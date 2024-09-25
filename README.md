# Projeto CRUD com Flask e MongoDB

## Contexto
Este projeto consiste em uma aplicação web CRUD (Create, Read, Update, Delete) construída com o framework Flask e conectada a um banco de dados MongoDB via MongoDB Atlas. A aplicação permite gerenciar cadastros de funcionários, possibilitando a criação, visualização, atualização e exclusão de registros diretamente na interface web.

## Configuração
Clone o repositório:
```
git clone https://github.com/leopxz/CRUD_mongoDB.git
cd CRUD_mongoDB
```
**Crie um ambiente virtual (opcional, mas recomendado):**
```
python3 -m venv venv
source venv/bin/activate   # Para usuários Linux/Mac
.\venv\Scripts\activate    # Para usuários Windows
```
**Instale as dependências:**
```
pip install -r requirements.txt
```
**Configuração do MongoDB:**

Crie uma conta no MongoDB Atlas.
Crie um cluster e uma base de dados.
Atualize a string de conexão no arquivo app.py com as credenciais do seu MongoDB Atlas.

## Execução
Para executar a aplicação localmente, siga os passos:

Certifique-se de que as dependências estão instaladas e a string de conexão ao MongoDB está configurada corretamente.

**Execute a aplicação:**
```
python app.py
```
Acesse a aplicação no navegador no endereço: http://127.0.0.1:5000.

## Estrutura

CRUD mongodb/<br>
│<br>
├── static/css/              -> Contém o arquivo de estilo CSS para a interface da aplicação.<br>
 |   └── style.css/<br>
├── templates/               -> Define os modelos de dados usados na aplicação.<br>
│   └── create.html<br>
 |   └── details.html<br>
│   └── index.html<br>
│   └── update.html<br>
├── app.py                  -> Arquivo principal que contém as rotas da aplicação Flask e a lógica para conexão com o MongoDB.<br>
<br>
##Contribuição
Sinta-se à vontade para abrir issues e enviar pull requests. Toda ajuda é bem-vinda para melhorar a aplicação.
