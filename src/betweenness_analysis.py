from .grafo_utils import dijkstra

def calculaCentralidade(grafo):

    nos = list(grafo.keys())
    N = len(nos)
    centralidade = {no: 0.0 for no in nos} 

    for noOrigem in nos:
        pilha, distancia, antecessores, caminhosMaisCurtos = dijkstra(grafo, noOrigem)
        
        if not pilha:
            continue
            
        dependencia = {no: 0.0 for no in nos} 

        while pilha:
            noAtual = pilha.pop()
            
            for antecessor in antecessores[noAtual]:   
                if caminhosMaisCurtos[noAtual] != 0:
                    contribuicao = (caminhosMaisCurtos[antecessor] / caminhosMaisCurtos[noAtual]) * (1.0 + dependencia[noAtual])
                    dependencia[antecessor] += contribuicao
            
            if noAtual != noOrigem:
                centralidade[noAtual] += dependencia[noAtual]
            
    if N > 2:
        fator_normalizacao = (N - 1) * (N - 2) / 2.0
    else:
        fator_normalizacao = 1.0 

    centralidade_normalizada = {
        no: valor / fator_normalizacao 
        for no, valor in centralidade.items()
    }
    
    return centralidade_normalizada