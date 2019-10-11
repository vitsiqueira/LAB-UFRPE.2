#a ideia é calcular o menor caminho utilizando o algoritmo de dijkstra, assim pagando sempre o menor frete possível.
#o grafo deve ser mostrado no código antes da sua execução.
graph = {'a':{'b':4, 'd':3},
        'b':{'e':1},
        'c':{'f':5}, 
        'e':{'d':3, 'f':2}}
n1 = (input("Início: ")).lower()
n2 = (input("Fim: ")).lower()
def djikstra(graph, start, end):
    ant = {}
    dist_min = {}
    unseenNo = graph
    caminho = []
    inf = 999999
    for no in unseenNo:
        dist_min[no] = inf
    dist_min[start] = 0

    while unseenNo:
        minNo = None
        for no in unseenNo:
            if minNo is None:
                minNo = no
            elif dist_min[no] < dist_min[minNo]:
                minNo = no

        for childNo, valor in graph[minNo].items():
            if valor + dist_min[minNo] < dist_min[childNo]:
                dist_min[childNo] = valor + dist_min[minNo]
                ant[childNo] = minNo
        unseenNo.pop(minNo)

    currentNo = end
    while currentNo != start:
        try:
            caminho.insert(0, currentNo)
            currentNo = ant[currentNo]
        except KeyError:
            print("IMPOSSIVEL.")
            break
    caminho.insert(0, start)
    if dist_min[end] != inf:
        print("Menor caminho: " + str(dist_min[end]))
        print("Caminho: " + str(caminho))

djikstra(graph, n1, n2)
