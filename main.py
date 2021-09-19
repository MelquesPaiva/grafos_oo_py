import sys
from src.graph import Graph

# Recuperando nome do arquivo passado no parâmetro
file = open(sys.argv[1])
graph = Graph()

# Primeira linha de configuração do nó
graphConfig = file.readline().split(' ')
amountNods = graphConfig[0]

nodeList = []

for line in file:
    line = line.replace('\n', '')
    nodeData = line.split(' ')

    # Adicionando nó ao grafo
    graph.addNode(nodeData[0])

    # Adicionando conexão do respectivo nó
    graph.addEdge(nodeData[0], nodeData[1], nodeData[2])

file.close()
