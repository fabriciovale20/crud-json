from main import CrudJson
import json

class Post():
    def post_json(self):  # Inserindo novos valores POST
        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
        dados.append({'nome': self.nome, 'idade': self.idade})
        with open('arquivo_json.json', 'w', encoding='utf8') as f:
            return json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))