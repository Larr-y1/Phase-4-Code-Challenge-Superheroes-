#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Welcome to Superheroes code challenge</h1>'

@app.route('/heroes')
def get_heroes():
    heroes = []
    
    for hero in Hero.query.all():
        hero_dict = hero.to_dict(rules=('-hero_powers',))
        heroes.append(hero_dict)
    
    response = make_response(jsonify(heroes), 200)
    return response

@app.route('/heroes/<int:id>')
def get_heroes_by_id(id):
    hero = Hero.query.filter(Hero.id == id).first()
    
    if not hero:
        return make_response(jsonify({"error": "Hero not found"}), 404)
    
    response = make_response(jsonify(hero.to_dict()), 200)
    return response

@app.route('/powers')
def get_powers():
    powers = []
    for power in Power.query.all():
        power_dict = power.to_dict(rules=('-hero_powers',))
        powers.append(power_dict)
        
    response = make_response(jsonify(powers), 200)
    return response

@app.route('/powers/<int:id>')
def get_powers_by_id(id):
    power = Power.query.filter(Power.id == id).first()
    
    if not power:
        return make_response(jsonify({"error": "Power not found"}), 404)
    
    response = make_response(jsonify(power.to_dict(rules=('-hero_powers',))), 200)
    return response

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
        power = Power.query.filter(Power.id == id).first()
        
        if not power:
            return make_response(jsonify({"error": "Power not found"}), 404)
        
        data = request.get_json()
        try:
            for key in data:
                if hasattr(power, key):
                    setattr(power, key, data[key])
            db.session.commit()
            return jsonify(power.to_dict()), 200
        except ValueError as ve:
            return jsonify({"errors": [str(ve)]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        new_hp = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )
        db.session.add(new_hp)
        db.session.commit()
        return jsonify(new_hp.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
    

        
         
    




if __name__ == '__main__':
    app.run(port=5555, debug=True)