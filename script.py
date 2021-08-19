import json
from time import sleep

cadastro = []


class CrudJson:
    # Função para escolher a opção do usuário
    def resposta(self):
        global resp

        print()
        print('\033[1:34m=\033[m' * 40)
        print('{:^55}'.format('\033[1:30:107m   Escolha uma das opção abaixo   \033[m'))
        print('\033[1:34m=\033[m' * 40)
        resp = int(input('\033[97m1.\033[m Redefinir arquivo JSON\n'
                         '\033[97m2.\033[m Ler JSON\n'
                         '\033[97m3.\033[m Novo cadastro\n'
                         '\033[97m4.\033[m Buscar cadastro\n'
                         '\033[97m5.\033[m Alterar cadastro\n'
                         '\033[97m6.\033[m Deletar cadastro\n'
                         '\033[97m0.\033[m Sair\n'
                         '\033[97mOpção:\033[m '))

    # Função para salvar dados de entrada NOME e IDADE
    def pergunta_dados(self):
        global nome, idade, buscar, alterar

        if resp == 3:
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
        elif resp == 4:
            buscar = str(input('Buscar por: '))
        elif resp == 5:
            buscar = str(input('Alterar cadastro de nome: '))
        elif resp == 6:
            buscar = str(input('Informe nome do cadastrado a ser \033[91mdeletado\033[m: '))

    # Função para emetir sucesso ao final operação escolhida
    def sucess(self):
        print('\033[92m\nOperação realizada com sucesso!\033[m')
        sleep(2)

    # Função tratativa de erros
    def erros(self):
        print("\033[1:91mAVISO!!!\033[m\n"
              "\033[91mArquivo JSON não criado ou inválido.\033[m\n"
              "Escolha a opção: \033[97m1-Redefinir arquivo JSON\033[m, em seguida tente novamente.")
        sleep(8)

    # Função para criar/redefinir arquivo_json
    def create_json(self, dados):
        with open('arquivo_json.json', 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))

    # Função de leitura para as demais funções
    def read_json(self):
        global dados

        with open('arquivo_json.json', 'r', encoding='utf8') as f:
            dados = json.load(f)

    # Função para salvar alterações no arquivo JSON
    def write_json(self):
        with open('arquivo_json.json', 'w', encoding='utf8') as f:
            if resp != 1 and resp != 5:
                dados.append({'nome': nome, 'idade': idade})
            return json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))

    # Criando/Redefinindo arquivo JSON - OPÇÃO 1
    def create(self, dados):
        print('\033[36mRedefinindo arquivo JSON', end='')
        for c in range(0, 3):
            print('.', end='')
            sleep(0.5)
        print('\033[m')

        self.create_json(cadastro)
        if resp != 1:
            dados.append({'nome': nome, 'idade': idade})
        self.sucess()

    # Lendo arquivo JSON - OPÇÃO 2
    def read(self):
        try:
            print('\033[36mLendo arquivo JSON', end='')
            for c in range(0, 3):
                print('.', end='')
                sleep(0.5)
            print('\033[m')

            self.read_json()
            print('\033[97mCadastros Arquivo JSON\033[m')
            if len(dados) == 0:
                print('\033[91mNão há nenhum registro no arquivo JSON!\033[m')
                sleep(2)
            else:
                for c in range(0, len(dados)):
                    print(f'{c + 1}. {dados[c]["nome"]}, {dados[c]["idade"]} anos')
                self.sucess()
        except FileNotFoundError:
            self.erros()

    # Inserindo novos valores (POST) - OPÇÃO 3
    def post(self):
        try:
            self.pergunta_dados()

            print('\033[36mInserindo novo cadastro no arquivo JSON', end='')
            for c in range(0, 3):
                print('.', end='')
                sleep(0.5)
            print()

            self.read_json()
            self.write_json()
            self.sucess()
        except FileNotFoundError:
            self.erros()

    # Consultando arquivo JSON (GET) - OPÇÃO 4
    def get(self):
        global cont
        try:
            cont = 0
            self.pergunta_dados()

            print('\033[36mBuscando', end='')
            for c in range(0, 3):
                print('.', end='')
                sleep(0.5)
            print('\033[m')

            self.read_json()
            for c in range(0, len(dados)):
                if dados[c]['nome'] == buscar:
                    cont += 1
                    print(f'Nome: {dados[c]["nome"]}, {dados[c]["idade"]} anos')
                    if resp == 2 or resp == 4:
                        self.sucess()
            if cont == 0:
                print(f'\033[91mNenhum cadastro encontrado com o nome {buscar}\033[m')
                sleep(2)
        except FileNotFoundError:
            self.erros()

    # Alterar cadastro no arquivo JSON (PUT) - OPÇÃO 5
    def put(self):
        try:
            CrudJson().get()

            if cont > 0:
                print('\033[94mInsira as informações abaixo:')
                sleep(1)

                alterar_nome = str(input('Nome atualizado: '))
                alterar_idade = int(input('Idade atualizada:\033[m '))

                for c in range(0, len(dados)):
                    if dados[c]['nome'] == buscar:
                        dados[c]['nome'] = alterar_nome
                        dados[c]['idade'] = alterar_idade
                        with open('arquivo_json.json', 'w', encoding='utf8') as f:
                            json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))
                        self.sucess()
        except FileNotFoundError:
            self.erros()

    # Deletar cadastrado no arquivo JSON (DELETE) - OPÇÃO 6
    def delete(self):
        try:
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
                    break
        except FileNotFoundError:
            print()


# Trativa de opções para execução das funções
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

        elif resp == 0:  # Finalizar código  - OPÇÃO 0
            break

print('\033[97m\nEncerrando programa\033[m', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(0.5)
print('\033[97m\nPROGRAMA FINALIZADO!!!\033[m')
