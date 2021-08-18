from main import CrudJson
import json

class Create:
    def create_json(self, dados, resp, nome, idade):  # Criado arquivo JSON
        with open('arquivo_json.json', 'w', encoding='utf8') as f:
            if resp != 1:
                dados.append({'nome': self.nome, 'idade': self.idade})
            return json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))
