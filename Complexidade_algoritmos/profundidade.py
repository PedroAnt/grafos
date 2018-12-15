from grafos import grafo

print('Grafo: ', grafo)

def buscar(grafo, atual, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(atual)
    for next in grafo[atual] - visitado:
        buscar(grafo, next, visitado)
    return visitado
    
resultado = buscar(grafo, 'C')
print('Resultado da busca: ', resultado)

def caminho(grafo, atual, objetivo):
    stack = [(atual, [atual])]
    while stack:
        (vertice, path) = stack.pop()
        for next in grafo[vertice] - set(path):
            if next == objetivo:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

caminhos = list(caminho(grafo, 'A', 'F'))
print('Possíveis caminhos: ', caminhos)