from src import dijkstra

#Implementação da análise de acessibilidade através do conceito de core-periphery, onde utilizamos o algoritmo de k-core decomposition e
#da analise da proximidade onde utilizamos a centralidade de proximidade

# Algoritmo de K-Core Decomposition para calcular o core number de cada nó
# O core number de um nó é o maior valor de k para o qual o nó ainda permanece no k-core
def calculaKCore(grafo):
    graus = {}
    for no in grafo.keys():
        vizinhos = grafo[no]
        graus[no] = len(vizinhos)
    
    numerosCore = {}
    for no in grafo:
        numerosCore[no] = graus[no] #o core inicial de cada nó são os graus originais do grafo
    
    removidos = {no: False for no in grafo} #criamos um controle de nós "removidos"
    
    for i in range(len(grafo)):
        # busca o não removido com menor core, que será o core atual avaliado
        menor = None
        for no in grafo:
            if removidos[no] == False:
                if menor is None or numerosCore[no] < numerosCore[menor]:
                    menor = no
        
        removidos[menor] = True #marcamos ele como removido
        
        #tiramos ele da contagem de core de seus vizinhos, pois se um nó foi removido, seu vizinhos decaem de grau
        for vizinho in grafo[menor]:
            if not removidos[vizinho] and numerosCore[vizinho] > numerosCore[menor]:
                numerosCore[vizinho] -= 1
    
    return numerosCore

def classificaCentroPeriferia(numerosCore):
    corePerifieria = 1

    classificacao = {
        'nosPeriferia': [],
        'nosCentro': [],

    }

    for no, coreNum in numerosCore.items():
        if coreNum == corePerifieria:  
            classificacao['nosPeriferia'].append(no) 
        else:
            classificacao['nosCentro'].append(no)

    return classificacao

def calculaCentralidadeProximidade(grafo):
    nos = list(grafo.keys())
    proximidade = {}

    #Para cada nó, calcula sua distância para todos os outros
    for no in nos:
        _, distancia, _,_ = dijkstra(grafo, no)

        distanciasValidas = []
        for dist in distancia.values():
            if dist != float('inf') and dist > 0:
                distanciasValidas.append(dist)
        
        if len(distanciasValidas) > 0:
            distanciaMedia = sum(distanciasValidas) / len(distanciasValidas)
            proximidade[no] = 1 / distanciaMedia
        else:
            proximidade[no] = 0

    return proximidade