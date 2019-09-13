def grafo():
    N,inicio,final = map(lambda i: int(i),input().split(" "))
    if N < 2 or N > 10**5:
        print("ERRO")

    else:
        if inicio != final:
            grafo = [[] for j in range(N)]
            for j in range(N-1):
                P,S,V = map(lambda i: int(i),input().split(" "))
                grafo[P-1].append((S-1,V))
                grafo[S-1].append((P-1,V))
        else:
            print("ERRO")

    eq_caminho(grafo,inicio-1,final-1)

def eq_caminho(grafo,inicio,final):
    G = []
    Percorrido = [0 for j in range(len(grafo))]
    for j in grafo[inicio]:
        G.append(j)
        Percorrido[j[0]] = 1
    vivi = G[0]

    G.pop(0)
    while vivi[0] != final:
        for j in grafo[vivi[0]]:
            if Percorrido[j[0]] is 0:
                Percorrido[j[0]] = 1
                G.append((j[0],vivi[1]+j[1]))
        vivi = G[0]
        G.pop(0)

    return print(vivi[1])

grafo()
