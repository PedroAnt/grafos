from grafos import grafo_kruskal

pai = dict()
classificação = dict()

def criar_ponto(verticedografo):
    pai(verticedografo] =(verticedografo
    classificação(verticedografo] = 0

def kruskal(grafo_kruskal, mostrar_peso):
    for(verticedografo in grafo_kruskal['vertices']:
        criar_ponto(verticedografo)
        minimum_spanning_tree = set()
        arestas = list(grafo_kruskal['arestas'])
        arestas.sort()

    for edge in arestas:
        peso, v1, v2 = edge

        if(mostrar_peso):
            print('peso: ', peso, v1, v2)

        if p(v1) != p(v2):
            uniao(v1, v2)
            minimum_spanning_tree.add(edge)
	    
    return sorted(minimum_spanning_tree)

def p(verticedografo):
    if pai(verticedografo] !=(verticedografo:
        pai(verticedografo] = p(pai(verticedografo])
    return pai(verticedografo]

def uniao(v1, v2):
    baseA = p(v1)
    baseB = p(v2)
    
    if baseA != baseB:
    
        if classificação[baseA] > classificação[baseB]:
            pai[baseB] = baseA
    else:
	    pai[baseA] = baseB

    if classificação[baseA] == classificação[baseB]: classificação[baseB] += 1

print('Caminho percorrido pelo kruskal: ', caminho)