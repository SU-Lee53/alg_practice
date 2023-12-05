# _1: Floyd-Warshall
edges = [
  (0, 4, 463), (0, 11, 347), (0, 12, 410), (0, 20, 294), (0, 21, 360),
  (1, 5, 61), (1, 10, 343), (1, 17, 395), (2, 6, 162), (2, 10, 431),
  (2, 16, 135), (2, 17, 415), (2, 18, 281), (2, 23, 435), (3, 4, 59),
  (3, 15, 230), (3, 21, 118), (4, 11, 393), (4, 15, 273), (5, 9, 341),
  (5, 10, 333), (5, 23, 427), (6, 10, 268), (6, 12, 432), (6, 14, 465),
  (6, 16, 298), (6, 18, 278), (6, 19, 199), (7, 9, 120), (7, 13, 257),
  (7, 24, 410), (8, 11, 275), (8, 12, 111), (8, 15, 407), (8, 19, 420),
  (8, 20, 481), (9, 10, 341), (9, 23, 253), (9, 24, 357), (11, 15, 141),
  (12, 16, 194), (12, 19, 410), (12, 20, 370), (12, 22, 324), (13, 14, 375),
  (13, 17, 323), (13, 22, 318), (13, 23, 83), (14, 19, 350), (14, 24, 211),
  (15, 21, 177), (16, 18, 348), (16, 20, 421), (18, 24, 377), (19, 22, 211),
  (19, 23, 376), (22, 23, 400), (23, 24, 335),
]
num_vertex = 25
INF = float('inf')
D = [[INF for _ in range(num_vertex)] for _ in range(num_vertex)]
V = [[ -1 for _ in range(num_vertex)] for _ in range(num_vertex)]

for s,e,w in edges:
	D[s][e] = w
	D[e][s] = w * 6 // 10

for k in range(num_vertex):
	for s in range(num_vertex):
		if s == k: continue
		for e in range(num_vertex):
			if e == k or e == s: continue
			if D[s][e] > D[s][k] + D[k][e]:
				D[s][e] = D[s][k] + D[k][e]
				V[s][e] = k

def getPath(s,e):
	k = V[s][e]
	if k == -1:
		return f'=>{e}'
	return getPath(s,k) + getPath(k,e)

for s in range(num_vertex):
	for e in range(num_vertex):
		if s == e: continue
		path = getPath(s,e)
		cost = D[s][e]
		print(f'{s}{path} ({cost})')












