import numpy as np

def funcao(x, y):
    return ((1-x)**2 + 100*(y-(x**2))**2)

def vizinhos(individuo, tamanhoPopulacao):
    vizinhos = np.zeros(2)

    vizinhos[0] = individuo + 1
    vizinhos[1] = individuo - 1

    if((individuo + 1) > tamanhoPopulacao ):
        vizinhos[1] = 0
    if((individuo - 1) < 0 ):
        vizinhos[0] = tamanhoPopulacao

    return vizinhos

def pso(maxIt, ac1, ac2, vMax, vMin):

    ##Inicializando as variaveis: População -> x, Velocidades -> v, iteracao.
    ##A população x é inicializada de acordo com os limites impostos pelo problema,
    ##o qual determinava seu dominio de -5 a 5.
    ##A velocidade foi escolhida arbitrariamente
    x = np.random.uniform(low=-5, high=5, size=(25, 2))
    v = np.random.uniform(low=vMin, high=vMax, size=(25))
    iteracao = 1
    melhorDesempenhoIndividual = np.zeros(25)
    j = np.zeros(2)

    while iteracao < maxIt:
        for individuo in len(x):
            if (funcao(x[individuo][0],x[individuo][1]) < melhorDesempenhoIndividual[individuo]):
                melhorDesempenhoIndividual[individuo] = funcao(x[individuo][0], x[individuo][1])

            g = individuo
            ##Vizinhos
            vizinhos = vizinhos(individuo, len(x))

            for vizinho in vizinhos:
                if funcao(x[vizinho][0], x[vizinho][1]) > funcao(x[g][0], x[g][1]):
                        g = vizinho

        vetorAleatorio1 = np.random.uniform(low=0, high=ac1, size=(25))
        vetorAleatorio2 = np.random.uniform(low=0, high=ac2, size=(25))
        v[individuo] = v[individuo] + np.multiply(vetorAleatorio1, (melhorDesempenhoIndividual[individuo] - x[individuo])) + np.multiply(vetorAleatorio2, (melhorDesempenhoIndividual[individuo] - x[individuo]))
        x[individuo] = x[individuo] + v[individuo]
    iteracao += 1
    return