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

                noOrigem = int(partes[1])
                noDestino = int(partes[4])
                pesoAresta = float(partes[7])

                grafo[noOrigem][noDestino] = pesoAresta
                grafo[noDestino][noOrigem] = pesoAresta
                
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

    pilha = [] #Pilha que armazena os nós na ordem em que são visitados
    
    antecesores = collections.defaultdict(set) #defaultdic: permite que acesse uma chave que não existe em um dicionário e crie um valor padrão para ela
    
    caminhosMaisCurtos = {no: 0 for no in grafo} 

    distancia = {no: float('inf') for no in grafo} 
    

    distancia[no_inicial] = 0.0
    caminhosMaisCurtos[no_inicial] = 1

    filaPrioridade = [(0.0, no_inicial)] 

    while filaPrioridade:
        dist, u = heapq.heappop(filaPrioridade)
        
        if dist > distancia[u]:
            continue
            
        pilha.append(u) 

        for v, pesoAresta in grafo[u].items():
            
            novaDistancia = distancia[u] + pesoAresta
            
            if novaDistancia < distancia[v]:
                distancia[v] = novaDistancia

                caminhosMaisCurtos[v] = caminhosMaisCurtos[u]
                antecesores[v] = {u}
                heapq.heappush(filaPrioridade, (distancia[v], v))
                
            elif novaDistancia == distancia[v]:
                caminhosMaisCurtos[v] += caminhosMaisCurtos[u]
                antecesores[v].add(u)
            
            
    return pilha, distancia, antecesores, caminhosMaisCurtos


def grafo_networkx(grafo):

    G = nx.Graph() #Criando o grafo com networkx
    
    for noOrigem, vizinhos in grafo.items():
        for noDestino, peso in vizinhos.items():
            if noOrigem < noDestino:
                G.add_edge(noOrigem, noDestino, weight=peso)
    
    return G