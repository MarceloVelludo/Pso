from PSO import pso

maxIt = 1000
ac1 = 2
ac2 = 2
vMax = 5
vMin = -5



x, v, melhoresSolucoes, valoresMinimos, valoresMedios = pso(maxIt, ac1, ac2, vMax, vMin)

print("\nResultados:")
print("\nx:\n", x)
print("\nv:\n", v)
print("\nMelhores Soluções:\n", melhoresSolucoes)
print("\nValores Minimos:", valoresMinimos)
print("\nValores Médios:", valoresMedios)