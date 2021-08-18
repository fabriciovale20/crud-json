from main import CrudJson
import json

class Delete():
    def delete_json(self, buscar):  # Deletar cadastrado no arquivo JSON
        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
        for c in range(0, len(dados)):
            if dados[c]['nome'] == buscar:
                del dados[c]
                with open('arquivo_json.json', 'w', encoding='utf8') as f:
                    return json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))