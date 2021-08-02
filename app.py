from flask import Flask, render_template , url_for , request, redirect
from flask_sqlalchemy import SQLAlchemy
from subprocess import call

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
    speed = db.Column(db.Integer,nullable=False)
    gen = db.Column(db.Integer,nullable=False)
    legend = db.Column(db.Boolean)

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

@app.route('/import/', methods=['POST'])
def import_csv():
    if request.method == 'POST':
        call(['python','import_csv.py'])
        return redirect('/')
    else:
        pass

@app.route('/delete/<int:id>')
def delete(id):
    pokemon_to_delete = Pokemon.query.get_or_404(id)

    try:
        db.session.delete(pokemon_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your pokemon'

if __name__ == "__main__":
    app.run(debug=True)