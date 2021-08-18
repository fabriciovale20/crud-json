import json
from time import sleep

cadastro = []

class CrudJson():
    def __init__(self):
        self.nome = nome
        self.idade = idade
        self.resp = resp

    def create(self, dados):  # Criado arquivo JSON
        with open('arquivo_json.json', 'w') as f:
            if resp != 1:
                dados.append({'nome': self.nome, 'idade': self.idade})
            return json.dump(dados, f, indent=4)


    def read(self):  # Lendo arquivo JSON
        with open('arquivo_json.json', 'r') as f:
            dados = json.load(f)
            return dados


    def post(self):  # Inserindo novos valores POST
        with open('arquivo_json.json', 'r') as f:
            dados = json.load(f)
        dados.append({'nome': self.nome, 'idade': self.idade})
        with open('arquivo_json.json', 'w') as f:
            return json.dump(dados, f, indent=4)

# def get():  # Consultando arquivo JSON
# def delete():  # Deleter cadastrado no arquivo JSON


resp = int(input('Qual operação deseja realizar? \n'
                 '\033[97m1.\033[m Redefinir arquivo JSON;\n'
                 '\033[97m2.\033[m Ler JSON;\n'
                 '\033[97m3.\033[m Inserir novo cadastro;\n'
                 '\033[97mResposta:\033[m '))

if resp == 3:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
else:
    nome = ''
    idade = 0

if resp == 1:  # Create
    print('\033[36mRedefinindo arquivo JSON', end='')
    for c in range(1, 3):
        print('.', end='')
        sleep(0.5)

    operacao = CrudJson().create(cadastro)

elif resp == 2:  # Read
    novo_cadastro = CrudJson()
    if len(novo_cadastro.read()) == 0:
        print('\033[91mNão há nenhum registro no arquivo JSON!\033[m')
    else:
        print(novo_cadastro.read())

elif resp == 3:  # Post
    print('\033[36mInserindo novo cadastro no arquivo JSON', end='')
    for c in range(1, 3):
        print('.', end='')
        sleep(0.5)

    operacao = CrudJson().post()

print('\033[92m\nOperação executada com sucesso!\033[m')
