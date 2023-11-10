from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Spell, spell_schema, spells_schema
import uuid

api = Blueprint('api', __name__, url_prefix= '/api')

@api.route('/spells', methods = ['POST'])
@token_required
def create_spell(current_user_token):
    id = request.json['id']
    url = request.json['url']
    name = request.json['name']
    level = request.json['level']
    casting_time = request.json['casting_time']
    duration = request.json['duration']
    classes = request.json['classes']
    desc = request.json['desc']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    spell = Spell(id, url, name, level, casting_time, duration, classes, desc, user_token = user_token )

    db.session.add(spell)
    db.session.commit()

    response = spell_schema.dump(spell)
    return jsonify(response)
#Get ALL Spells
@api.route('/spells', methods = ['GET'])
@token_required
def get_spells(current_user_token):
    a_user = current_user_token.token
    spells = Spell.query.filter_by(user_token = a_user).all()
    response = spells_schema.dump(spells)
    return jsonify(response)

#Get Single Contact
@api.route('/spells/<id>', methods = ['GET'])
@token_required
def get_single_spell(current_user_token, id):
    spell = Spell.query.get(id)
    response = spell_schema.dump(spell)
    return jsonify(response)

# UPDATE endpoint <id> is a variable, 'PUT' is the replacement method
@api.route('/spells/<id>', methods = ['POST','PUT'])
@token_required
def update_spell(current_user_token,id):
    spell = Spell.query.get(id)
    spell.id = str(uuid.uuid4())
    spell.url = request.json['url']
    spell.name = request.json['name']
    spell.level = request.json['level']
    spell.casting_time = request.json['casting_time']
    spell.duration = request.json['duration']
    spell.classes = request.json['classes']
    spell.desc = request.json['desc']
    spell.user_token = current_user_token.token


    db.session.commit()
    response = spell_schema.dump(spell)
    return jsonify(response)


# DELETE ENDPOINT
@api.route('/spells/<id>', methods = ['DELETE'])
@token_required
def delete_spell(current_user_token, id):
    spell = Spell.query.get(id)
    db.session.delete(spell)
    db.session.commit()
    response = spell_schema.dump(spell)
    return jsonify(response)