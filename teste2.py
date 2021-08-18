class Testando:
    def ola(self):
        global n, a
        n = int(input('Teste: '))
        a = int(input('Teste2: '))
        print('Olá')
        return n

    def mundo(self):
        self.ola()
        print(f'{n}{a} Mundo')

Testando().mundo()
