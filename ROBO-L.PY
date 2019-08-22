# COMO F = 1 METRO PARA FRENTE E T = 1 METRO PARA TRÁS, DEVEMOS CONTAR A QUANTIDADE DE VEZES QUE CADA COMANDO APARECE E DEPOIS
# SUBTRAÍ-LOS DESCOBRINDO ASSIM QUAL A POSIÇÃO FINAL QUE O ROBÔ SE ENCONTRA.

# MENU COM OS COMANDOS NECESSÁRIOS PARA A EXECUÇÃO DO PROGRAMA 
print("""Digite os comandos:
* F = para mover-se 1 metro para a frente
* T = para mover-se 1 metro para trás""") 
V = input("::: ").upper() # INPUT QUE CHAMA OS COMANDOS PARA OS MOVIMENTOS FEITOS PELO ROBÔ | UPPER PARA DEIXAR TUDO EM LETRA MAIÚSUCULA

f = V.count("F") # CONTAR A QUANTIDADE DE F
t = V.count("T") # CONTAR A QUANTIDADE DE T

if f > t: # CONDIÇÃO PARA EXECUTAR A EQUAÇÃO
    posição = f - t # EQUAÇÃO PARA SABERMOS A POSIÇÃO DO ROBÔ
    print("O robô está na posição de nº{}".format(posição))

elif t > f: # CONDIÇAO PARA EXECUTAR A EQUAÇÃO 
    posição = t - f # EQUAÇÃO PARA SABERMOS A POSIÇÃO DO ROBÔ
    print("O robô está na posição de nº{}".format(posição))

elif t == f: # CONDIÇÃO CASO O VALOR DE T FOR IGUAL AO VALOR DE F, OU SEJA, POSIÇÃO FINAL = A POSIÇÃO INICIAL
    print("A posição final é igual a posição inicial, pois T é igual F.")