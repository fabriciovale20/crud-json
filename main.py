import json
from time import sleep

cadastro = []


class CrudJson():
    def resposta(self):
        global resp
        print('=' * 40)
        resp = int(input('Qual operação deseja realizar? \n'
                         '\033[97m1.\033[m Redefinir arquivo JSON\n'
                         '\033[97m2.\033[m Ler JSON\n'
                         '\033[97m3.\033[m Novo cadastro\n'
                         '\033[97m4.\033[m Buscar cadastro\n'
                         '\033[97m5.\033[m Alterar cadastro\n'
                         '\033[97m6.\033[m Deletar cadastro\n'
                         '\033[97m0.\033[m Sair\n'
                         '\033[97mResposta:\033[m '))


    def pergunta_dados(self):
        global nome, idade, buscar, alterar

        if resp == 3:
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
        elif resp == 4:
            buscar = str(input('Pesquisar nome: '))
        elif resp == 5:
            buscar = str(input('Alterar cadastro de nome: '))
        elif resp == 6:
            buscar = str(input('Informe nome do cadastrado a ser \033[91mdeletado\033[m: '))

    def sucess(self):
        print('\033[92m\nOperação realizada com sucesso!\033[m')
        sleep(2)

    def create(self, dados):  # Criado arquivo JSON
        print('\033[36mRedefinindo arquivo JSON', end='')
        for c in range(0, 3):
            print('.', end='')
            sleep(0.5)
        print()

        with open('arquivo_json.json', 'w', encoding='utf8') as f:
            if resp != 1:
                dados.append({'nome': nome, 'idade': idade})
            json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))
        self.sucess()

    def read(self):  # Lendo arquivo JSON
        print('\033[36mLendo arquivo JSON', end='')
        for c in range(0, 3):
            print('.', end='')
            sleep(0.5)
        print('\033[m')

        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
        print('\033[97mCadastros Arquivo JSON\033[m')
        if len(dados) == 0:
            print('\033[91mNão há nenhum registro no arquivo JSON!\033[m')
        else:
            for c in range(0, len(dados)):
                print(f'{c+1}. {dados[c]["nome"]}, {dados[c]["idade"]} anos')
            self.sucess()

    def post(self):  # Inserindo novos valores POST
        self.pergunta_dados()

        print('\033[36mInserindo novo cadastro no arquivo JSON', end='')
        for c in range(0, 3):
            print('.', end='')
            sleep(0.5)
        print()

        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
        dados.append({'nome': nome, 'idade': idade})
        with open('arquivo_json.json', 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))

        self.sucess()

    def get(self):  # Consultando arquivo JSON
        global cont

        cont = 0
        self.pergunta_dados()

        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
        for c in range(0, len(dados)):
            if dados[c]['nome'] == buscar:
                cont += 1
                print(f'Nome: {dados[c]["nome"]}, {dados[c]["idade"]} anos')
        if cont == 0:
            print(f'\033[91mNenhum cadastro encontrado com o nome {buscar}\033[m')

    def put(self):  # Alterar cadastro no arquivo JSON
        CrudJson().get()

        if cont > 0:
            print('\033[94mInsira as informações abaixo:')
            sleep(1)

            alterar_nome = str(input('Nome atualizado: '))
            alterar_idade = int(input('Idade atualizada:\033[m '))


            with open('arquivo_json.json', 'r', encoding='utf8') as f:
                dados = json.load(f)
            for c in range(0, len(dados)):
                if dados[c]['nome'] == buscar:
                    dados[c]['nome'] = alterar_nome
                    dados[c]['idade'] = alterar_idade
                    with open('arquivo_json.json', 'w', encoding='utf8') as f:
                        json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))
                        self.sucess()

    def delete(self):  # Deletar cadastrado no arquivo JSON
        CrudJson().get()

        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)
        for c in range(0, len(dados)):
            if dados[c]['nome'] == buscar:
                del dados[c]
                with open('arquivo_json.json', 'w', encoding='utf8') as f:
                    json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))
                    print('\033[36mDeletando', end='')
                    for c in range(0, 3):
                        print('.', end='')
                        sleep(0.5)
                    print('\033[m')
                self.sucess()

while True:
    try:
        opcao = CrudJson().resposta()

    except:
        print('\033[91mDigite uma opção válida\033[m')
    else:
        if resp == 1:  # Create (Cria arquivo JSON)
            operacao = CrudJson().create(cadastro)

        elif resp == 2:  # Read (Lê e imprime no terminal a lista com Nome e Idade de todos cadastro no arquivo JSON)
            novo_cadastro = CrudJson().read()

        elif resp == 3:  # Post (Insere um novo cadastro com Nome e Idade informado no terminal)
            operacao = CrudJson().post()

        elif resp == 4:  # Get (Busca o cadastrado através do Nome informado e mostra a lista no terminal)
            operacao = CrudJson().get()

        elif resp == 5:  # Put (Realiza a alteração de uma cadastro já existente fornecido no terminal)
            operacao = CrudJson().put()

        elif resp == 6:  # Delete (Deleta o cadastro informado no terminal)
            operacao = CrudJson().delete()

        elif resp == 0:  # Finalizar código
            break

print('\033[97m\nEncerrando programa\033[m', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(0.5)
print('\033[97m\nPROGRAMA FINALIZADO!!!\033[m')
