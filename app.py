from flask import Flask, render_template , url_for , request, redirect, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort , fields, marshal_with
from subprocess import call
from functools import wraps
import jwt
import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokedex.db'
app.config['SECRET_KEY'] = 'pikachu'
api = Api(app)
db = SQLAlchemy(app)

# BD Model
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
        # return '<Pokemon %r>' % self.id
        return f"Pokemon(num={num}, name={name}, typeu={typeu}, typed={typed}, total={total}, hp={hp}, attack={attack}, defense={defense}, spatk={spatk}, spdef={spdef}, speed={speed}, gen={gen}, legend={legend})"

resource_fieds = {
    'id' : fields.Integer,
    'num' : fields.Integer,
    'name' : fields.String,
    'typeu' : fields.String,
    'typed' : fields.String,
    'total' : fields.Integer,
    'hp' : fields.Integer,
    'attack' : fields.Integer,
    'defense' : fields.Integer,
    'spatk' : fields.Integer,
    'spdef' : fields.Integer,
    'speed' : fields.Integer,
    'gen' : fields.Integer,
    'legend' : fields.Boolean
}

# Import - CSV a BD
@app.route('/import/', methods=['POST'])
def import_csv():
    if request.method == 'POST':
        call(['python','import_csv.py'])
        return redirect('/')
    else:
        return 'There was an issue importing data'

## FRONT - entrypoint

# Index route
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        pass

    else:
        pokemons = Pokemon.query.all()
        return render_template('index.html', pokemons = pokemons)

## Form route DELETE
@app.route('/delete/<int:id>')
def delete(id):
    pokemon_to_delete = Pokemon.query.get_or_404(id)

    try:
        db.session.delete(pokemon_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your pokemon'

## Form route UPDATE
@app.route('/update/<int:id>', methods = ['GET','POST'])
def update(id):
    pokemon_to_update = Pokemon.query.get_or_404(id)

    if request.method == 'POST':
        pokemon_to_update.num = request.form['num']
        pokemon_to_update.name = request.form['name']
        pokemon_to_update.typeu = request.form['typeu']
        pokemon_to_update.typed = request.form['typed']
        pokemon_to_update.total = request.form['total']
        pokemon_to_update.hp = request.form['hp']
        pokemon_to_update.attack = request.form['attack']
        pokemon_to_update.defense = request.form['defense']
        pokemon_to_update.spatk = request.form['spatk']
        pokemon_to_update.spdef = request.form['spdef']
        pokemon_to_update.speed = request.form['speed']
        pokemon_to_update.gen = request.form['gen']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating you pokemon'

    else:
        return render_template('update.html', pokemon_to_update = pokemon_to_update)

## BACK - endpoint

# Return all pokemons
class Pokemons(Resource):
    @marshal_with(resource_fieds)
    def get(self):
        result = Pokemon.query.all()
        if not result:
            abort(404, message="No pokemons on database")
        else:
            return result

# Return sorted pokemons by parameter
class PokemonSorted(Resource):
    @marshal_with(resource_fieds)
    def get(self,parameter):
        for pname in resource_fieds:
            if pname == parameter:
                result = Pokemon.query.order_by(pname).all()
        try: 
            if(result):
                    return result
        except:
            abort(404, message="Los pokemons no tienen este atributo" )
        
# Authentication

@app.route('/login')
def login():
    auth = request.authorization 
    if auth and auth.username == 'trainer2' and auth.password == 'pokemonclub':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token})

    return make_response('Are you a pokemon trainer?', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})


api.add_resource(Pokemons,"/pokemon")
api.add_resource(PokemonSorted,"/pokemonsort/<string:parameter>")


if __name__ == "__main__":
    app.run(debug=True)