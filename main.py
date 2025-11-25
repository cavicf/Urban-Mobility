from src import (
    carregaGrafo,
    carregaPosicoes,
    calculaCentralidade,
    grafo_networkx   
)

from visualizations import (
    visualizaGrafoOriginal, 
    visualizaGrafoCentralidade
)


#Carregamento do grafo e visualização
def main():
    GRAFO = carregaGrafo('data/brasilia_edge_info.txt')
    pos = carregaPosicoes('data/brasilia_edge_info.txt')

    grafoNetworkx = grafo_networkx(GRAFO)
    visualizaGrafoOriginal(grafoNetworkx, pos, '1_grafo_original_brasilia.pdf')

    ###Análise de centralidade de intermediação e visualização comparativa
    nosCentralizados = calculaCentralidade(GRAFO)

    top10 = sorted(nosCentralizados.items(), key=lambda item: item[1], reverse=True)
    for no, score in top10:
        print(f"Nó {no} (Centralidade): {score:.6f}")
    print()
    totalCentralidade = sum(nosCentralizados.values()) 
    mediaCentralidade = totalCentralidade / len(nosCentralizados) 
    print(f"Média de Centralidade de Betweenness: {mediaCentralidade}")
    print()
    visualizaGrafoCentralidade(grafoNetworkx, nosCentralizados, pos, 10, '2_grafo_centralidade_brasilia.pdf')

if __name__ == "__main__":
    main()