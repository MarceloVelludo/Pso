import numpy as np

def funcao(x, y):
    print("\nRecebido:\n")
    print("x:", x)
    print("\ny:", y)
    print("calculo:", ((1-x)**2 + 100*(y-(x**2))**2))
    print("(1-x)", (1-x))
    print("(1-x)**2", (1-x)**2)
    print("x**2", x**2)
    print("y-(x**2)", y-(x**2))
    print("(y-(x**2))**2", (y-(x**2))**2)
    return ((1-x)**2 + 100*(y-(x**2))**2)

def vizinhos(individuo, tamanhoPopulacao):
    vizinhos = np.zeros(2)

    vizinhos[0] = individuo + 1
    vizinhos[1] = individuo - 1

    if((individuo + 1) > tamanhoPopulacao-1 ):
        vizinhos[0] = 0
    if((individuo - 1) < 0 ):
        vizinhos[1] = tamanhoPopulacao-1

    return vizinhos

def pso(maxIt, ac1, ac2, vMax, vMin):


    ##Inicializando as variaveis: População -> x, Velocidades -> v, iteracao.
    ##A população x é inicializada de acordo com os limites impostos pelo problema,
    ##o qual determinava seu dominio de -5 a 5.
    ##A velocidade foi escolhida arbitrariamente
    valorMinimo = np.zeros(maxIt)
    valorMedio = np.zeros(maxIt)
    x = np.random.uniform(low=-5, high=5, size=(25, 2))
    v = np.random.uniform(low=vMin, high=vMax, size=(25, 2))
    iteracao = 1
    melhorDesempenhoIndividual = np.zeros((25,1))
    vId = len(v)
    j = np.zeros(2)

    while iteracao < maxIt:

        vetorAleatorio1 = np.random.uniform(low=0, high=ac1, size=(25, 2))
        vetorAleatorio2 = np.random.uniform(low=0, high=ac2, size=(25, 2))
        for index, i in enumerate(melhorDesempenhoIndividual):
            melhorDesempenhoIndividual[index] = funcao(x[index][0], x[index][1])

        for individuo in range(len(x)):
            if (funcao(x[individuo][0],x[individuo][1]) < melhorDesempenhoIndividual[individuo]):
                melhorDesempenhoIndividual[individuo][0] = funcao(x[individuo][0], x[individuo][1])

            g = individuo
            ##Vizinhos
            vizinhosVar = vizinhos(individuo, len(x))

            for vizinho in vizinhosVar:
                if funcao([vizinho.astype(int)][0], x[vizinho.astype(int)][1]) < funcao(x[g][0], x[g][1]):
                        g = vizinho.astype(int)

        print("\n---------------------------")
        print("***Iteração:", iteracao)
        print("\nv:", v)
        print("\nvetorAleatorio1:", vetorAleatorio1)
        print("\nmelhorDesempenhoIndividual:", melhorDesempenhoIndividual)
        print("\nx:", x)
        print("\nvetorAleatorio2:", vetorAleatorio2)
        print("\n---------------------------")
       ## print("\nnp.multiply(vetorAleatorio1, (melhorDesempenhoIndividual[individuo] - x[individuo])):", np.multiply(vetorAleatorio1, np.add(x[melhorDesempenhoIndividual[individuo][1]], -x[individuo])))
        v[individuo] = v[individuo] + np.multiply(vetorAleatorio1[individuo], (melhorDesempenhoIndividual[individuo] - x[individuo])) + np.multiply(vetorAleatorio2[individuo], (funcao(x[g][0], x[g][1]) - x[individuo]))
        if (v[individuo].any() > vId) or (v[individuo].any() < vId):
            v[individuo] = vId
        x[individuo] = x[individuo] + v[individuo]

        total = 0
        ##Media
        for desempenho in melhorDesempenhoIndividual:
            total += desempenho
        valorMedio[iteracao] = (total/25)
        ##Minimo
        valorMinimo[iteracao] = melhorDesempenhoIndividual[0]
        for desempenho in melhorDesempenhoIndividual:
            if(valorMinimo[iteracao] > desempenho ):
                valorMinimo[iteracao] = desempenho
        iteracao += 1
    return x, v, melhorDesempenhoIndividual, valorMinimo, valorMedio