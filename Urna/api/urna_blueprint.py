from flask import Blueprint
from flask import request, jsonify
from model.urna import colegi
from model.rsa import get_keys
from phe import paillier


urna_blueprint = Blueprint('urna', __name__, url_prefix='/urna')

#PRO
#URL = "http://127.0.0.1:5500/pubkey"
#Kpublica_censo = request.get(url = URL)

#PRE
keys = get_keys()
Kpublica_censo = keys[1]
urna = colegi("test", Kpublica_censo)
#urna.get_kpublica_mesa_electoral()
votos = []



@urna_blueprint.route('/votar' , methods=['POST'])
def root(): 
    if request.method == 'POST':
        voto = request.get_json()
        usuario_valido = urna.validar_votante(voto["firma_votante"])
        if usuario_valido == True:
            try:
                votos.append(voto["voto"])
            except:
                return jsonify({'message': usuario_valido,
                            'payload': "invalid_vote"
                            })
            return jsonify({'message': usuario_valido})
        else:
            return jsonify({'message': usuario_valido,
                            'payload': "invalid_user"
                            })

@urna_blueprint.route('/encrypted_votes' , methods=['GET'])
def root2(): 
    return votos

@urna_blueprint.route('/encrypted_votes' , methods=['GET'])
def root3():
    result = 0
    for voto in votos:
        result = result.__add_encoded(voto)
    return result
#    return "Alice_Kpub: [{}, {}]\nAlice_Kpriv: [{}, {}] \r Bob_Kpub: [{}, {}]\nBob_Kpriv: [{}, {}]".format(Alice_keys[1], Alice_keys[0], Alice_keys[2], Alice_keys[0],Bob_keys[1], Bob_keys[0], Bob_keys[2], Bob_keys[0])
#    return "Alice keys: [{},{}]\n".format(Alice_keys.self__private_exponent, Alice_keys.self__public_exponent)