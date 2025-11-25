import csv
import os

def exportar_tabela_geral(caminho_arquivo_original, dados_nos, dados_arestas, nome_arquivo_saida='tabela_geral_dados.csv'):
    output_path = os.path.join('outputs', nome_arquivo_saida)
    
    # Colunas do arquivo
    header = [
        'edge_num', 'Node_1', 'X_1', 'Y_1', 'Node_2', 'X_2', 'Y_2', 'length',
        'C-betweenness_1', 'C-betweenness_2',
        'C-closness_1', 'C-closness_2',
        'K-core_1', 'K-core_2',
        'Edge_vunerability'
    ]
    
    linhas_saida = []
    
    try:
        with open(caminho_arquivo_original, 'r') as f:
            for linha in f:
                partes = linha.split()
                if len(partes) < 8: continue
                
                # Extrai dados originais
                edge_num = partes[0]
                node_1 = int(partes[1])
                x_1 = partes[2]
                y_1 = partes[3]
                node_2 = int(partes[4])
                x_2 = partes[5]
                y_2 = partes[6]
                length = partes[7]
                
                # Busca métricas do Nó 1
                metrics_n1 = dados_nos.get(node_1, {})
                bet_1 = metrics_n1.get('betweenness', 0.0)
                close_1 = metrics_n1.get('closeness', 0.0)
                kcore_1 = metrics_n1.get('k_core', 0)
                
                # Busca métricas do Nó 2
                metrics_n2 = dados_nos.get(node_2, {})
                bet_2 = metrics_n2.get('betweenness', 0.0)
                close_2 = metrics_n2.get('closeness', 0.0)
                kcore_2 = metrics_n2.get('k_core', 0)
                
                # Busca métrica da Aresta (tenta (u,v) e (v,u))
                vuln = dados_arestas.get((node_1, node_2))
                if vuln is None:
                    vuln = dados_arestas.get((node_2, node_1), 0.0)

                nova_linha = {
                    'edge_num': edge_num,
                    'Node_1': node_1, 'X_1': x_1, 'Y_1': y_1,
                    'Node_2': node_2, 'X_2': x_2, 'Y_2': y_2,
                    'length': length,
                    'C-betweenness_1': bet_1, 'C-betweenness_2': bet_2,
                    'C-closness_1': close_1, 'C-closness_2': close_2,
                    'K-core_1': kcore_1, 'K-core_2': kcore_2,
                    'Edge_vunerability': vuln
                }
                linhas_saida.append(nova_linha)
                
    except FileNotFoundError:
        print(f"ERRO: Arquivo original não encontrado: {caminho_arquivo_original}")
        return

    # Escreve o CSV
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(linhas_saida)
    
    print(f"Arquivo gerado com sucesso: {output_path}")
