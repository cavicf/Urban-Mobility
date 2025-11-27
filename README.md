# Planejamento Urbano e Mobilidade em Redes Viárias

Este repositório contém um estudo sobre a estrutura e o comportamento da rede viária de uma região de Brasília, utilizando ferramentas de **Teoria dos Grafos**. O objetivo principal é investigar propriedades estruturais, localizar pontos críticos, identificar regiões de difícil acesso e compreender como a malha urbana se organiza sob diferentes métricas topológicas.

---

# Apresentação em Vídeo  
Para uma explicação detalhada sobre o trabalho e seus resultados, assista à nossa [apresentação em vídeo](https://youtu.be/9aEze6osuNE?si=1hyCjPnBq4rPMGNf)

---

## Objetivos do Trabalho

O estudo busca analisar a rede de Brasília a partir de métricas fundamentais de análise de redes complexas. As principais metas foram:

- Investigar a **estrutura de conectividade** da rede por meio de métricas clássicas.
- Identificar **arestas vulneráveis** e entender seu impacto na eficiência global da rede.
- Estudar a **centralidade** dos nós para reconhecer regiões estratégicas.
- Analisar o padrão **core–periphery**, destacando áreas estruturais centrais e periféricas.
- Avaliar a **acessibilidade global**, indicando regiões que exigem percursos mais longos ou possuem acesso limitado.
- Integrar diferentes métricas para compreender fragilidades e potenciais demandas de mobilidade urbana.

---

## Métricas e Análises Realizadas

O estudo foi dividido em diferentes etapas, com foco nas seguintes análises:

### **1. Centralidade de Betweenness**
Quantifica a importância dos nós como intermediários nas rotas mais curtas.  
Nesta etapa, os nós mais estratégicos foram identificados e mapeados visualmente.

### **2. Vulnerabilidade das Arestas**
Avaliação do impacto da remoção individual de arestas sobre a **eficiência global** da rede.  
A análise revelou quais conexões são críticas para a manutenção da conectividade urbana.

### **3. Estrutura Core–Periphery (K-Core Decomposition)**
Classificação dos nós em dois grupos estruturais:
- **Centro**: vértices altamente conectados localmente.
- **Periferia**: regiões com menor participação estrutural na rede.

### **4. Centralidade de Proximidade**
Métrica baseada na distância média entre um vértice e todos os outros.  
Permite identificar regiões de difícil acesso, distantes dos principais corredores de mobilidade.  
  
Esses pontos representam regiões especialmente críticas na malha urbana.

---

## Estrutura do Repositório

```
├── data/
│   ├── brasilia.net
│   ├── brasilia_edge_info.txt
|   ├── README.txt
│
├── outputs/
│   ├── 1_grafo_original_brasilia.pdf
│   ├── 2_grafo_centralidade_brasilia.pdf
│   ├── 3_grafo_core_periphery.pdf
│   ├── 4_grafo_centralidade_proximidade.pdf
│   ├── 5_grafo_vulnerabilidade.pdf
│   ├── 6_hist_vulnerabilidade.pdf
│   ├── tabela_geral_dados.csv
│
├── slides/
│   ├── Planejamento Urbano e Mobilidade em Redes Viárias.pdf
|
├── src/
│   ├── accessibility_analysis.py
│   ├── betweenness_analysis.py
│   ├── grafo_utils.py
│   ├── vulnerability_analysis.py
|
├── visualizations/
│   ├── plot_utils.py
|
├── main.py
├── ArtigoCientifico.pdf
└── README.md
```

---

## Como Executar o Projeto

### **1. Instale as dependências**
É necessário ter **Python 3.8+** instalado.

No terminal:

```bash
pip install matplotlib networkx numpy
```

### **2. Execute o arquivo principal**

```bash
python3 main.py
```

O script irá:
- carregar os dados da rede,
- realizar todos os cálculos,
- gerar os grafos e figuras,
- salvar as figuras dentro da pasta `ouputs/`
- gerar arquivo de síntese dos resultados na pasta `ouputs/`.

---

## Autores

Este trabalho foi desenvolvido como parte da disciplina **Grafos – UNIFEI**, pelos seguintes estudantes:

- **2024001197 – Camily Victal Finamor**  
- **2024008189 – João Victor Jacometti de Assis**  
- **2024002372 – Luís Gustavo Riso Santos**  
- **2024002292 – Rodolfo Alberti Silva**  

---

## Referências

A base teórica para o estudo inclui, entre outros:

- Latora, V.; Nicosia, V.; Russo, G. *Complex Networks: Principles, Methods and Applications.* Cambridge University Press, 2017.
- Crucitti, P.; Latora, V.; Porta, S. *Centrality measures in spatial networks of urban streets.* Phys. Rev. E 73, 036125 (2006).
- Porta, S.; Crucitti, P.; Latora, V. *The network analysis of urban streets: a primal approach.* Env. & Planning B, 2006.

O dataset utilizado faz parte do material suplementar do livro de Latora et al. (2017).

---

## Observação Final

Este repositório visa contribuir para estudos urbanos baseados em redes e para o entendimento da mobilidade estruturada em malhas viárias reais.  
Sugestões, dúvidas ou contribuições são bem-vindas!
