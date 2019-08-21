print("""Digite os comandos:
* F = para mover-se 1 metro para a frente
* T = para mover-se 1 metro para trás""")
V = input("::: ").upper()

f = V.count("F")
t = V.count("T")

if f > t:
    posição = f - t
    print("O robô está na posição de nº{}".format(posição))

elif t > f:
    posição = t - f
    print("O robô está na posição de nº{}".format(posição))

elif t == f:
    print("A posição final é igual a posição inicial, pois T é igual F.")