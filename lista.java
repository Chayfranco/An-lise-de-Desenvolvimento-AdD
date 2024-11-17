import java.io.*;

class Node {
    int valor;
    Node proximo;

    public Node(int valor) {
        this.valor = valor;
        this.proximo = null;
    }
}

class Lista {
    private Node inicio;

    public Lista() {
        this.inicio = null;
    }

    public void inserir(int valor, int posicao) {
        Node novoNode = new Node(valor);
        if (posicao == 0) {
            novoNode.proximo = inicio;
            inicio = novoNode;
            return;
        }

        Node atual = inicio;
        for (int i = 0; atual != null && i < posicao - 1; i++) {
            atual = atual.proximo;
        }

        if (atual == null) {
            return;
        }

        novoNode.proximo = atual.proximo;
        atual.proximo = novoNode;
    }

    public void Remover(int valor) {
        Node atual = inicio, anterior = null;

        while (atual != null) {
            if (atual.valor == valor) {
                if (anterior != null) {
                    anterior.proximo = atual.proximo;
                } else {
                    inicio = atual.proximo;
                }
                atual.proximo = null;
                return;
            }
            anterior = atual;
            atual = atual.proximo;
        }
    }

    public void exibir() {
        Node atual = inicio;
        System.out.print("Lista Atual: ");
        while (atual != null) {
            System.out.print(atual.valor + " ");
            atual = atual.proximo;
        }
        System.out.println();
    }
}

public class lista {
    public static void main(String[] args) {
        Lista lista = new Lista();

        try (BufferedReader leitor = new BufferedReader(new FileReader("arq3.txt"))) {
            // Leitura dos valores iniciais
            String[] valoresIniciais = leitor.readLine().split(" ");
            for (int i = 0; i < valoresIniciais.length; i++) {
                lista.inserir(Integer.parseInt(valoresIniciais[i]), i);
            }

            // Leitura do número de ações
            int totalAcoes = Integer.parseInt(leitor.readLine().trim());

            // Processamento das ações
            for (int i = 0; i < totalAcoes; i++) {
                String[] acao = leitor.readLine().trim().split(" ");
                switch (acao[0]) {
                    case "A" -> // Adicionar
                        lista.inserir(Integer.parseInt(acao[1]), Integer.parseInt(acao[2]));
                    case "R" -> // Remover
                        lista.Remover(Integer.parseInt(acao[1]));
                    case "P" -> // Mostrar
                        lista.exibir();
                    default -> System.out.println("Ação inválida.");
                }
            }
        } catch (IOException e) {
            System.err.println("Erro ao acessar o arquivo: " + e.getMessage());
        }
    }
}
