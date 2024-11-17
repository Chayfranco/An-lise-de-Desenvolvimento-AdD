class Lista:
    class No:
        def __init__(self, valor, proximo=None):#dois atributos essenciais p um nó
            self.valor = valor 
            self.proximo = proximo

    def __init__(self):#crio os atributos principais da minha lista
        self.__cabeca = None
        self.__quantidade = 0
    
    def __len__(self):#para determinar a quantidade de elementos
        return self.__quantidade

    def __getitem__(self, posicao):#p consegyur acessar os elementos pela posição
        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError('Posição Inválida.')
        
        atual = self.__cabeca
        for i in range(posicao):
            atual = atual.proximo
        return atual.valor
    
    def inserir(self, posicao, valor):
        novo = self.No(valor) #crio o meu elemento que desejo inserir
        if posicao <= 0 or self.__cabeca is None:
            novo.proximo = self.__cabeca
            self.__cabeca = novo
        else:
            atual = self.__cabeca#percorrer começando pela cabeça
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
                
                atual.proximo = None
                atual.valor = None
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
    lista = Lista()  # Cria uma instância da classe Lista
    with open(file_name, 'r') as file:  # Abre o arquivo para leitura
        linhas = file.readlines()  # Lê todas as linhas do arquivo
        
        # Processa os elementos iniciais da lista
        elementos_iniciais = map(int, linhas[0].split())  # Converte a primeira linha em uma lista de inteiros
        for valor in elementos_iniciais:
            lista.inserir(len(lista), valor)  # Insere cada valor na lista na última posição
        
        num_operacoes = int(linhas[1].strip())  # Converte a segunda linha para obter o número de operações
        
        # Processa as operações
        for i in range(2, 2 + num_operacoes):  # Para cada operação no arquivo
            comando = linhas[i].strip().split()  # Divide a linha de comando em partes (por espaço)
            if comando[0] == 'A':  # Comando para adicionar
                lista.inserir(int(comando[2]), int(comando[1]))  # Insere na posição especificada
            elif comando[0] == 'R':  # Comando para remover
                lista.remover(int(comando[1]))  # Remove o valor especificado
            elif comando[0] == 'P':  # Comando para imprimir
                lista.printar()  # Imprime a lista


processar_arquivo('arq3.txt')

