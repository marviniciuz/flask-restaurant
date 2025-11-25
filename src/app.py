from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo  DB
class Restaurante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo_cozinha = db.Column(db.String(50)) # Ex: Italiana, Japonesa

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "tipo_cozinha": self.tipo_cozinha}

with app.app_context():
    db.create_all()

# --- ROTAS DA API ---

# (POST)
@app.route('/restaurantes', methods=['POST'])
def cadastrar_restaurante():
    dados = request.json
    
    novo_restaurante = Restaurante(
        nome=dados.get('nome'),
        tipo_cozinha=dados.get('tipo_cozinha')
    )
    
    db.session.add(novo_restaurante)
    db.session.commit()
    
    return jsonify({"mensagem": "Restaurante cadastrado com sucesso!", "dados": novo_restaurante.to_json()}), 201

# (GET)
@app.route('/restaurantes', methods=['GET'])
def pesquisar_restaurantes():
    nome_busca = request.args.get('nome') # Pega o parametro da URL
    
    if nome_busca:
        resultados = Restaurante.query.filter(Restaurante.nome.contains(nome_busca)).all()
    else:
        resultados = Restaurante.query.all()
        
    return jsonify([r.to_json() for r in resultados])

# (DELETE)
@app.route('/restaurantes/<int:id>', methods=['DELETE'])
def excluir_restaurante(id):
    restaurante = Restaurante.query.get(id)
    
    if not restaurante:
        return jsonify({"erro": "Restaurante não encontrado"}), 404
        
    db.session.delete(restaurante)
    db.session.commit()
    
    return jsonify({"mensagem": "Restaurante removido!"})

if __name__ == '__main__':
    app.run(debug=True)