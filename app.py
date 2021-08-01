from flask import Flask, render_template , url_for , request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokedex.db'
db = SQLAlchemy(app)

# Modelo en BD
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    name = db.Column(db.String(100),nullable=False)
    typeu = db.Column(db.String(100),nullable=False)
    typed = db.Column(db.String(100))
    total = db.Column(db.Integer,nullable=False)
    hp = db.Column(db.Integer,nullable=False)
    attack = db.Column(db.Integer,nullable=False)
    defense = db.Column(db.Integer,nullable=False)
    spatk = db.Column(db.Integer,nullable=False)
    spdef = db.Column(db.Integer,nullable=False)
    generation = db.Column(db.Integer,nullable=False)
    legend = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<Pokemon %r>' % self.id



# Ruta Index 
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        pass

    else:
        pokemons = Pokemon.query.all()
        return render_template('index.html', pokemons = pokemons)

if __name__ == "__main__":
    app.run(debug=True)