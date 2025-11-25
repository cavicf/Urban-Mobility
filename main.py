from src import (
    carregaGrafo,
    carregaPosicoes,
    calculaCentralidade,
    calculaKCore,
    classificaCentroPeriferia,
    calculaCentralidadeProximidade,
    grafo_networkx,       
    vulnerabilidade_rede,
    exportar_tabela_geral
)

from visualizations import (
    visualizaGrafoOriginal, 
    visualizaGrafoCentralidade, 
    visualizaKCore,
    visualizaCentralidadeProximidade,
    visualizaVulnerabilidade,
    histogramaVulnerabilidade,
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

    ###Análise de vulnerabilidade de rede
    listaVulnerabilidadeAresta = vulnerabilidade_rede(GRAFO)
    
    ordenacaoVulnerabilidades = sorted(
        listaVulnerabilidadeAresta,
        key=lambda item: item[1],   #item = ((noh_1, noh_2), vulnerabilidadeAresta)
        reverse=True
    )

    #Classificacao das arestas mais vulneraveis
    print("\nTop 10 arestas mais vulneráveis:")
    limite = min(10, len(ordenacaoVulnerabilidades))
    for i in range(limite):
        (noh_1, noh_2), vulnerabilidadeAresta = ordenacaoVulnerabilidades[i]
        print(f"{i+1:2d}. Aresta ({noh_1}, {noh_2}) -> vulnerabilidade = {vulnerabilidadeAresta:.6f}")
    print()
    valoresVulnerabilidade = [vulnerabilidadeAresta for _, vulnerabilidadeAresta in listaVulnerabilidadeAresta]
    somaVulnerabilidades = sum(valoresVulnerabilidade)
    mediaVulnerabilidade = somaVulnerabilidades / len(valoresVulnerabilidade)
    print(f"Média de Vulnerabilidade das Arestas: {mediaVulnerabilidade}")
    print()
    print("\nLista completa de arestas (da mais para a menos vulnerável):")
    for i, ((noh_1, noh_2), vulnerabilidadeAresta) in enumerate(ordenacaoVulnerabilidades, start=1):
        print(f"{i:3d}. Aresta ({noh_1}, {noh_2}) -> vulnerabilidade = {vulnerabilidadeAresta:.6f}")
    print()
    visualizaVulnerabilidade(grafoNetworkx, listaVulnerabilidadeAresta, pos, '3_grafo_vulnerabilidade.pdf')
    histogramaVulnerabilidade(listaVulnerabilidadeAresta, '4_hist_vulnerabilidade.pdf')


    ###Análise de core-periphery e centralidade de proximidade, com visualização comparativa
    numerosCore = calculaKCore(GRAFO)
    classificacao = classificaCentroPeriferia(numerosCore)

    print("Nós de Periferia:", classificacao['nosPeriferia'])
    print("Nós de Centro:", classificacao['nosCentro'])
    print()
    centralidadesProximidade = calculaCentralidadeProximidade(GRAFO)
    print("Centralidade de Proximidade dos Nós:")
    print(centralidadesProximidade)

    visualizaKCore(grafoNetworkx, classificacao, pos, '5_grafo_core_periphery.pdf')
    visualizaCentralidadeProximidade(grafoNetworkx, centralidadesProximidade, pos, '6_grafo_centralida_proximidade.pdf')

    #Exportação da arquivo com todos os dados consolidados das analises feitas
    todosNos = set(nosCentralizados.keys()) | set(centralidadesProximidade.keys()) | set(numerosCore.keys())
    dadosNos = {}
    
    for n in todosNos:
        dadosNos[n] = {
            'betweenness': nosCentralizados.get(n, 0.0),
            'closeness': centralidadesProximidade.get(n, 0.0),
            'k_core': numerosCore.get(n, 0)
        }
    
    dadosArestas = {}
    for (u, v), val in listaVulnerabilidadeAresta:
        dadosArestas[(u, v)] = val
        
    print("\nGerando arquivo CSV com dados consolidados...")
    exportar_tabela_geral(
        caminho_arquivo_original='data/brasilia_edge_info.txt',
        dados_nos=dadosNos,
        dados_arestas=dadosArestas,
        nome_arquivo_saida='tabela_geral_dados.csv'
    )

if __name__ == "__main__":
    main()