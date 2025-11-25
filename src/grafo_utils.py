import collections
import heapq
import networkx as nx

#Função para ler o arquivo "brasilia_edge_info"
def carregaGrafo(caminho_arquivo_arestas):

    grafo = collections.defaultdict(dict)

    try:
        with open(caminho_arquivo_arestas, 'r') as f:
            for linha in f:
                partes = linha.split()

                no_origem = int(partes[1])
                no_destino = int(partes[4])
                peso_aresta = float(partes[7])

                grafo[no_origem][no_destino] = peso_aresta
                grafo[no_destino][no_origem] = peso_aresta
                
    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado no caminho: {caminho_arquivo_arestas}")
        return {}
        
    return dict(grafo)

def carregaPosicoes(caminho_arquivo_arestas):
    pos = {}

    with open(caminho_arquivo_arestas, 'r') as f:
        for linha in f:
            partes = linha.split()

            no1 = int(partes[1])
            x1  = float(partes[2])
            y1  = float(partes[3])

            no2 = int(partes[4])
            x2  = float(partes[5])
            y2  = float(partes[6])

            # guarda a primeira coordenada conhecida de cada nó
            if no1 not in pos:
                pos[no1] = (x1, y1)
            if no2 not in pos:
                pos[no2] = (x2, y2)

    return pos

#Função para encontrar o caminho mais curto, quantos caminhos curtos existem e quais são os ANTECESSORES em cada caminho curto
def dijkstra(grafo, no_inicial):

    Pilha_S = [] #Pilha que armazena os nós na ordem em que são visitados
    
    Antecessores = collections.defaultdict(set) #defaultdic: permite que acesse uma chave que não existe em um dicionário e crie um valor padrão para ela
    
    Caminhos_Mais_Curtos = {no: 0 for no in grafo} 

    Distancia = {no: float('inf') for no in grafo} 
    

    Distancia[no_inicial] = 0.0
    Caminhos_Mais_Curtos[no_inicial] = 1

    Fila_Prioridade = [(0.0, no_inicial)] 

    while Fila_Prioridade:
        dist_u, u = heapq.heappop(Fila_Prioridade)
        
        if dist_u > Distancia[u]:
            continue
            
        Pilha_S.append(u) 

        for v, peso_aresta in grafo[u].items():
            
            nova_distancia = Distancia[u] + peso_aresta
            
            if nova_distancia < Distancia[v]:
                Distancia[v] = nova_distancia

                Caminhos_Mais_Curtos[v] = Caminhos_Mais_Curtos[u]
                Antecessores[v] = {u}
                heapq.heappush(Fila_Prioridade, (Distancia[v], v))
                
            elif nova_distancia == Distancia[v]:
                Caminhos_Mais_Curtos[v] += Caminhos_Mais_Curtos[u]
                Antecessores[v].add(u)
            
            
    return Pilha_S, Distancia, Antecessores, Caminhos_Mais_Curtos


def grafo_networkx(grafo):

    G = nx.Graph() #Criando o grafo com networkx
    
    for no_origem, vizinhos in grafo.items():
        for no_destino, peso in vizinhos.items():
            if no_origem < no_destino:
                G.add_edge(no_origem, no_destino, weight=peso)
    
    return G