from main import CrudJson
import json

class Put():
    def put_json(self, buscar, alterar_nome, alterar_idade):  # Alterar cadastro no arquivo JSON
        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
        for c in range(0, len(dados)):
            if dados[c]['nome'] == buscar:
                dados[c]['nome'] = alterar_nome
                dados[c]['idade'] = alterar_idade
                with open('arquivo_json.json', 'w', encoding='utf8') as f:
                    return json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))