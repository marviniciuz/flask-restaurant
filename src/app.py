from flask import Flask, request, render_template
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
    tipo_cozinha = db.Column(db.String(50))

    def to_json(self):
        return {"id": self.id, "nome": self.nome,
                "tipo_cozinha": self.tipo_cozinha
                }


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    restaurantes = Restaurante.query.all()
    return render_template('index.html', restaurantes=restaurantes)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    tipo = request.form.get('tipo_cozinha')
    
    if nome:
        novo = Restaurante(nome=nome, tipo_cozinha=tipo)
        db.session.add(novo)
        db.session.commit()
     
    restaurantes = Restaurante.query.all()
    return render_template('lista.html', restaurantes=restaurantes)


@app.route('/pesquisar')
def pesquisar():
    busca = request.args.get('q')
    if busca:
        restaurantes = Restaurante.query.filter(Restaurante.nome.contains(busca)).all()
    else:
        restaurantes = Restaurante.query.all()
    
    return render_template('lista.html', restaurantes=restaurantes)



@app.route('/deletar/<int:id>', methods=['DELETE'])
def deletar(id):
    item = Restaurante.query.get(id)
    if item:
        db.session.delete(item)
        db.session.commit()

    restaurantes = Restaurante.query.all()
    return render_template('lista.html', restaurantes=restaurantes)


if __name__ == '__main__':
    app.run(debug=True)