import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import networkx as nx
import os

def visualizaGrafoOriginal(grafo, pos, nomeArquivo):
    
    fig, ax = plt.subplots(figsize=(20, 16))
    
    # desenhando as arestas
    nx.draw_networkx_edges(
        grafo, pos,
        alpha=0.5,
        width=1.2,
        edge_color='#666666',
        ax=ax
    )
    
    # desenhando os nos
    nx.draw_networkx_nodes(
        grafo, pos,
        node_color='#1f77b4', 
        node_size=100,         
        alpha=0.7,
        ax=ax
    )
    
    titulo = f'Rede Viária de Brasília - Estrutura Original\n'
    titulo += f'{grafo.number_of_nodes()} interseções e {grafo.number_of_edges()} vias\n'
    titulo += f'Visualização sem análise de centralidade'
    plt.title(titulo, fontsize=16, weight='bold', pad=20)
    plt.axis('off')
    plt.tight_layout()
    outPutPath = os.path.join('outputs', nomeArquivo)
    plt.savefig(outPutPath, format='pdf', bbox_inches='tight')
    plt.close()


def visualizaGrafoCentralidade(grafo, centralidade, pos, topDez, nomeArquivo):
    centralidadeNo = []
    for node in grafo.nodes():
        centralidadeNo.append(centralidade.get(node, 0))
    
    # ordenando pra pegar os top 10
    topNos = sorted(centralidade.items(), key=lambda x: x[1], reverse=True)[:topDez]
    topNosIds = [node for node, _ in topNos]
        
    fig, ax = plt.subplots(figsize=(20, 16))
    
    valMin = min(centralidadeNo)
    valMax = max(centralidadeNo)
    norm = mcolors.Normalize(vmin=valMin, vmax=valMax)
    cmap = plt.get_cmap('YlOrRd')
    
    # tamanho dos nos baseado na centralidade
    noSize = []
    for node in grafo.nodes():
        tam = 300 + 100 * centralidade.get(node, 0)
        noSize.append(tam)
    
    nx.draw_networkx_edges(
        grafo, pos,
        alpha=0.5,
        width=1.2,
        edge_color='black',
        ax=ax
    )
    
    nodes = nx.draw_networkx_nodes(
        grafo, pos,
        node_color=centralidadeNo,
        node_size=noSize,
        cmap=cmap,
        alpha=0.8,
        vmin=valMin,
        vmax=valMax,
        ax=ax
    )
    
    # destacando os top 10 com tamanho maior e borda
    topCentralidades = [centralidade[no] for no in topNosIds]
    topTamanhos = []
    for no in topNosIds:
        tam = 300 + 2000 * centralidade[no]
        topTamanhos.append(tam)
    
    nx.draw_networkx_nodes(
        grafo, pos,
        nodelist=topNosIds,
        node_color=topCentralidades,
        node_size=topTamanhos,
        cmap=cmap,
        alpha=1.0,
        edgecolors='black',
        linewidths=3,
        ax=ax
    )
    
    labels = {}
    for no in topNosIds:
        labels[no] = str(no)
        
    nx.draw_networkx_labels(
        grafo, pos,
        labels,
        font_size=10,
        font_weight='bold',
        font_color='black',
        font_family='sans-serif',
        ax=ax
    )
    
    #adicionando colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label('Centralidade de Intermediação', fontsize=14, weight='bold', labelpad=20)
    
    #titulo geral
    titulo = f'Rede Viária de Brasília - Análise de Centralidade de Intermediação\n'
    titulo += f'Top {topDez} interseções mais críticas destacadas com borda preta\n'
    titulo += f'Tamanho e cor dos nós proporcionais à centralidade'
    plt.title(titulo, fontsize=16, weight='bold', pad=20)
    
    plt.axis('off')
    plt.tight_layout()
    outPutPath = os.path.join('outputs', nomeArquivo)
    plt.savefig(outPutPath, format='pdf', bbox_inches='tight')
    plt.close()

    #Grafo de core-periphery
def visualizaKCore(grafo, classificacao, pos, nomeArquivo):
    periferia = classificacao['nosPeriferia']
    centro = classificacao['nosCentro']

    fig, ax = plt.subplots(figsize=(20, 16))

    nx.draw_networkx_edges(grafo, pos, alpha=0.5, width=1.2, edge_color='#474143', ax=ax)
    nx.draw_networkx_nodes(
        grafo, pos,
        nodelist=periferia,
        node_color='#FF6444',
        node_size=200,
        alpha=0.8,
        linewidths=1.5,
        label=f'Periferia',
        ax=ax
    )

    nx.draw_networkx_nodes(
        grafo, pos,
        nodelist=centro,
        node_color='#00ADA9',
        node_size=300,
        alpha=0.9,
        linewidths=2,
        label=f'Centro',
        ax=ax
    )

    ax.legend(loc='upper right', fontsize=18, edgecolor='#474143', title='Classificação Core-Periphery',title_fontsize=18, markerscale=1.5, labelspacing=1.2, borderpad=1.2)
    plt.title(f'Rede Viária de Brasília - Estrutura Core-Periphery\n', fontsize=24, weight='bold')
    plt.axis('off')
    plt.tight_layout()
    output_path = os.path.join('outputs', nomeArquivo)
    plt.savefig(output_path, format='pdf', bbox_inches='tight')
    plt.close()

#Mapa de calor da centralidade de proxmidade
def visualizaCentralidadeProximidade(grafo, centralidadesProximidade, pos, nomeArquivo):
    fig, ax = plt.subplots(figsize=(20, 16))    
    centralidadeNos = []
    for node in grafo.nodes():
        centralidadeNos.append(centralidadesProximidade.get(node, 0))

    maiorCentralidade = max(centralidadeNos)
    nosDificilAcesso = []
    for node in grafo.nodes():
        valor = maiorCentralidade - centralidadesProximidade.get(node, 0)
        nosDificilAcesso.append(valor)

    minVal = min(nosDificilAcesso)
    maxVal = max(nosDificilAcesso)
    norm = mcolors.Normalize(vmin=minVal, vmax=maxVal)
    cmap = plt.get_cmap('Purples') 
    
    node_sizes = []
    for node in grafo.nodes():
        dif = maiorCentralidade - centralidadesProximidade.get(node, 0)
        tam = 100 + 300 * (dif / maiorCentralidade)
        node_sizes.append(tam)
    
    nx.draw_networkx_edges(grafo, pos, alpha=0.5, width=1.2, edge_color='#474143', ax=ax)
    nx.draw_networkx_nodes(
        grafo, pos,
        node_color=nosDificilAcesso,
        node_size=node_sizes,
        cmap=cmap,
        alpha=0.8,
        vmin=minVal,
        vmax=maxVal,
        ax=ax
    )
    
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label('Dificuldade de Acesso', fontsize=18, weight='bold', labelpad=20)
    
    plt.title(f'Rede Viária de Brasília - Análise de Acessibilidade\n', fontsize=24, weight='bold')
    plt.axis('off')
    plt.tight_layout() 
    output_path = os.path.join('outputs', nomeArquivo)
    plt.savefig(output_path, format='pdf', bbox_inches='tight')
    plt.close()


#Mapa de calor da vulnerabilidade das arestas da rede
def visualizaVulnerabilidade(grafoNetworkx, listaVulnerabilidadeAresta, pos, nomeArquivo):    
    dictVulnerabilidadeAresta = {}
    for (noh_1, noh_2), vulnerabilidadeAresta in listaVulnerabilidadeAresta:
        if grafoNetworkx.has_edge(noh_1, noh_2):
            dictVulnerabilidadeAresta[(noh_1, noh_2)] = vulnerabilidadeAresta
        elif grafoNetworkx.has_edge(noh_2, noh_1):
            dictVulnerabilidadeAresta[(noh_2, noh_1)] = vulnerabilidadeAresta

    edges = list(grafoNetworkx.edges())
    
    listaValoresVulnerabilidade = []
    for (noh_1, noh_2) in edges:
        val = dictVulnerabilidadeAresta.get((noh_1, noh_2), 0.0)
        listaValoresVulnerabilidade.append(val)

    fig, ax = plt.subplots(figsize=(10, 8))

    nx.draw_networkx_nodes(
        grafoNetworkx,
        pos,
        node_size=20,
        node_color='lightgray',
        ax=ax
    )

    #Coloracao arestas proporcional a vulnerabilidade
    cmap_reds = plt.get_cmap('Reds')
    edges_collection = nx.draw_networkx_edges(
        grafoNetworkx,
        pos,
        edgelist=edges,
        edge_color=listaValoresVulnerabilidade,
        edge_cmap=cmap_reds,
        width=2,
        ax=ax
    )

    vMin = min(listaValoresVulnerabilidade)
    vMax = max(listaValoresVulnerabilidade)
    norm = mcolors.Normalize(vmin=vMin, vmax=vMax)
    sm = cm.ScalarMappable(cmap=cmap_reds, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ax=ax, label='Vulnerabilidade da Aresta')
    ax.axis('off')
    ax.set_title('Mapa de Vulnerabilidade da Rede Viária de Brasília')
    plt.tight_layout()
    output_path = os.path.join('outputs', nomeArquivo)
    plt.savefig(output_path, format='pdf', bbox_inches='tight')
    plt.close()


#Histograma para identificação da dispersão de vulnerabilidades na rede
def histogramaVulnerabilidade(listaVulnerabilidadeAresta, nomeArquivo):
    listaValoresVulnerabilidade = []
    for (_, vulnerabilidadeAresta) in listaVulnerabilidadeAresta:
        listaValoresVulnerabilidade.append(vulnerabilidadeAresta)

    plt.figure(figsize=(8, 5))
    plt.hist(listaValoresVulnerabilidade, bins=30, edgecolor='black')
    plt.xlabel('Vulnerabilidade da Aresta')
    plt.ylabel('Frequência')
    plt.title('Distribuição das Vulnerabilidades de Arestas')
    plt.tight_layout()
    output_path = os.path.join('outputs', nomeArquivo)
    plt.savefig(output_path, format='pdf', bbox_inches='tight')
    plt.close()