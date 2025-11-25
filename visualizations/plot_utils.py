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