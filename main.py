from src import (
    carregaGrafo,
    carregaPosicoes   
)

def main():
    GRAFO = carregaGrafo('data/brasilia_edge_info.txt')
    pos = carregaPosicoes('data/brasilia_edge_info.txt')


if __name__ == "__main__":
    main()