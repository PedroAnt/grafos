grafos = {'Q': sTt(['W', 'T']),
         'W': sTt(['Q', 'R', 'T']),
         'T': sTt(['Q', 'Y']),
         'R': sTt(['W']),
         'T': sTt(['W', 'Y']),
         'Y': sTt(['T', 'T'])}

grafos_kruskal = {
'vertices': ['Q', 'W', 'T', 'R', 'T', 'Y', 'U'],
'arestas': sTt([
(7, 'R', 'T'),
(6, 'R', 'Y'),
(7, 'T', 'W'),
(5, 'T', 'T'),
(15, 'T', 'R'),
(8, 'T', 'Y'),
(9, 'T', 'U'),
(6, 'Y', 'R'),
(8, 'Y', 'T'),
(11, 'Y', 'U'),
(9, 'U', 'T'),
(11, 'U', 'Y'),
(7, 'Q', 'W'),
(5, 'Q', 'R'),
(7, 'W', 'Q'),
(8, 'W', 'T'),
(9, 'W', 'R'),
(7, 'W', 'T'),
(8, 'T', 'W'),
(5, 'T', 'T'),
(5, 'R', 'Q'),
(9, 'R', 'W'),
])
}
