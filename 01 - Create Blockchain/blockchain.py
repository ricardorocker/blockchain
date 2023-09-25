import datetime
import hashlib
import json
from flask import Flask, jsonify
#Essas linhas de código importam as bibliotecas necessárias para o funcionamento do programa. A biblioteca `datetime` é usada para lidar com datas e horários, `hashlib` é usada para calcular hashes criptográficos, `json` é usada para manipular objetos JSON e `flask` é uma estrutura de desenvolvimento web para Python.

class Blockchain:
#Aqui é definida a classe `Blockchain`, que será usada para criar e gerenciar a blockchain.


def __init__(self):
    self.chain = []
    self.create_block(proof = 1, previous_hash = '0')
#Isso é o método de inicialização da classe `Blockchain`. Ele cria uma lista vazia `chain` que será usada para armazenar os blocos da cadeia e chama o método `create_block` para criar o primeiro bloco da cadeia.


def create_block(self, proof, previous_hash):
    block = {'index': len(self.chain) + 1,
             'timestamp': str(datetime.datetime.now()),
             'proof': proof,
             'previous_hash': previous_hash}
    self.chain.append(block)
    return block
#Este método cria um novo bloco na blockchain. Ele recebe como argumentos a prova de trabalho `proof` e o hash do bloco anterior `previous_hash`. O bloco é um dicionário com chave-valor que contém o índice do bloco, o horário em que foi criado, a prova de trabalho, e o hash do bloco anterior. O bloco é então adicionado à lista `chain`.


def get_previous_block(self):
    return self.chain[-1]
#Este método retorna o bloco mais recente da cadeia.


def proof_of_work(self, previous_proof):
    new_proof = 1
    check_proof = False
    while check_proof is False:
        hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
        if hash_operation[:4] == '0000':
            check_proof = True
        else:
            new_proof += 1
    return new_proof
#Este método implementa um algoritmo de prova de trabalho para minerar um novo bloco. Ele recebe a prova de trabalho do bloco anterior `previous_proof` como argumento e calcula uma nova prova `new_proof`. Ele usa uma operação de hash SHA-256 para encontrar um hash que comece com quatro zeros. Ele faz isso incrementando a nova prova até que a condição seja atendida.


def hash(self, block):
    encoded_block = json.dumps(block, sort_keys = True).encode()
    return hashlib.sha256(encoded_block).hexdigest()
#Este método calcula o hash do bloco usando a função `hashlib.sha256`. Ele converte o bloco em uma string JSON, ordena as chaves do dicionário, codifica a string em bytes e, em seguida, calcula o hash usando a função `hexdigest()`.


def is_chain_valid(self, chain):
    previous_block = chain[0]
    block_index = 1
    while block_index < len(chain):
        block = chain[block_index]
        if block['previous_hash'] != self.hash(previous_block):
            return False
        previous_proof = previous_block['proof']
        proof = block['proof']
        hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
        if hash_operation[:4] != '0000':
            return False
        previous_block = block
        block_index += 1
    return True
#Este método verifica se uma cadeia de blocos é válida. Ele percorre cada bloco na cadeia e verifica se o hash do bloco anterior é igual ao hash calculado usando a função `hash`. Ele também verifica se a prova de trabalho é válida verificando se o hash da prova de trabalho começa com quatro zeros.


app = Flask(__name__)

blockchain = Blockchain()
#Essas linhas de código definem o objeto `app` como uma instância da classe `Flask` e criam uma instância da classe `Blockchain` chamada `blockchain`.


@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Parabens voce acabou de minerar um bloco!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200
#Esta é uma rota do Flask que é ativada quando a URL `'/mine_block'` é acessada com um método GET. Ele executa a mineração de um novo bloco chamando os métodos relevantes da classe `Blockchain`. Em seguida, ele cria uma resposta JSON que inclui as informações sobre o novo bloco, como índice, horário, prova de trabalho e hash do bloco anterior.


@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200
#Esta é outra rota do Flask que é ativada quando a URL `'/get_chain'` é acessada com um método GET. Ele retorna a cadeia de blocos atual e seu comprimento em uma resposta JSON.


@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message' : ' Tudo certo, o blockchain e valido '}
    else:
        response = {'message' : ' O blockchain nao e valido '}
    return jsonify(response), 200
#Esta é uma rota do Flask que é ativada quando a URL `'/is_valid'` é acessada com um método GET. Ele verifica se a cadeia de blocos é válida chamando o método `is_chain_valid` e retorna uma resposta JSON indicando se a cadeia de blocos é válida ou não.


app.run(host = '0.0.0.0', port = 5000)
#Esta linha inicia o servidor Flask na porta 5000 e permite que a aplicação seja acessada a partir de qualquer endereço IP.