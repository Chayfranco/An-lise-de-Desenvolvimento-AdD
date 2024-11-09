class Lista:
    class No:
        def __init__(self, valor, proximo=None):
            self.valor = valor
            self.proximo = proximo

    def __init__(self):
        self.__cabeca = None
        self.__quantidade = 0

    def __len__(self):
        return self.__quantidade

    def __getitem__(self, posicao):
        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError('Posição Inválida.')
        
        atual = self.__cabeca
        for i in range(posicao):
            atual = atual.proximo
        return atual.valor
    
    def inserir(self, posicao, valor):
        novo = self.No(valor)
        if posicao <= 0 or self.__cabeca is None:
            novo.proximo = self.__cabeca
            self.__cabeca = novo
        else:
            atual = self.__cabeca
            for i in range(posicao - 1):
                if atual.proximo is None:
                    break
                atual = atual.proximo
            novo.proximo = atual.proximo
            atual.proximo = novo
        self.__quantidade += 1

    def remover(self, valor):
        atual = self.__cabeca
        anterior = None
        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.__cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.__quantidade -= 1
                return
            anterior = atual
            atual = atual.proximo

    def printar(self):
        atual = self.__cabeca
        while atual is not None:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()

def processar_arquivo(file_name):
    lista = Lista()
    with open(file_name, 'r') as file:
        linhas = file.readlines()
        
        
        elementos_iniciais = map(int, linhas[0].split())
        for valor in elementos_iniciais:
            lista.inserir(len(lista), valor)
        
        num_operacoes = int(linhas[1].strip())
       
        for i in range(2, 2 + num_operacoes):
            comando = linhas[i].strip().split()
            if comando[0] == 'A':
                lista.inserir(int(comando[2]), int(comando[1]))
            elif comando[0] == 'R':
                lista.remover(int(comando[1]))
            elif comando[0] == 'P':
                lista.printar()

processar_arquivo('arq.txt')
