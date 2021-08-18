from main import CrudJson
import json

class Get():
    def read_json(self):  # Lendo arquivo JSON
        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
        print('\033[97mCadastros Arquivo JSON\033[m')
        if len(dados) == 0:
            print('\033[91mNão há nenhum registro no arquivo JSON!\033[m')
        else:
            for c in range(0, len(dados)):
                print(f'{dados[c]["nome"]}, {dados[c]["idade"]} anos')

    def get_json(self, buscar):  # Consultando arquivo JSON
        cont = 0

        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
        for c in range(0, len(dados)):
            if dados[c]['nome'] == buscar:
                cont += 1
                print(f'Nome: {dados[c]["nome"]}, {dados[c]["idade"]} anos')
        if cont == 0:
            print(f'Nenhum cadastro encontrado com o nome {buscar}')