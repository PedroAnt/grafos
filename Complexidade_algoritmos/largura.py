from grafos import grafo

print('Grafo: ', grafo)

def caminho(grafo, atual, busca):
    caminho = [(atual, [atual])]
    while caminho:
        (vertice, caminho) = caminho.pop(0)
        for proximo in grafo[vertice] - set(caminho):
            if proximo == busca:
                yield caminho + [proximo]
            else:
                caminho.append((proximo, caminho + [proximo]))

caminhospossiveis = list(caminho(grafo, 'A', 'B'))
print('Caminhos possiveis: ', caminhospossiveis)               

def Busca(grafo, atual):
    visitado, caminho = set(), [atual]
    while caminho:
        vertice = caminho.pop(0)
        if vertice not in visitado:
            visitado.add(vertice)
            caminho.extend(grafo[vertice] - visitado)
    return visitado

resultadobusca = Busca(grafo, 'A')
print('Resultado da busca feita por largura: ', resultadobusca)