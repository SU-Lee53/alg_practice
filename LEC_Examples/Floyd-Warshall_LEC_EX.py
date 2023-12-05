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
INF = float('inf')	# 미리 INF를 선언해놓고 불필요한 변환을 없앰
D = [[INF for _ in range(num_vertex)] for _ in range(num_vertex)]	# 비용을 저장할 2차원 배열
V = [[ -1 for _ in range(num_vertex)] for _ in range(num_vertex)]	# 경유지 저장할 2차원 배열, -1이면 직접 가는경우


# 초기화 루프
# 올때의 가치는 갈때의 가치의 60퍼센트임을 가정
for s,e,w in edges:	# start, end, weight
	D[s][e] = w
	D[e][s] = w * 6 // 10

# Floyd-Warshall Main Loop

for k in range(num_vertex):	# 경유지 1
	for s in range(num_vertex):	# 시작점
		if s == k: continue		# 시작점이 경유지와 같다면 고려X
		for e in range(num_vertex):	#도착점
			if e == k or e == s: continue	# 도착점이 경유지거나 시작점과 같으면 고려X
			if D[s][e] > D[s][k] + D[k][e]:	# s에서 e로 가는데 k를 들러서 가는것이 더 가깝다면 갱신
				D[s][e] = D[s][k] + D[k][e]
				V[s][e] = k	# s에서 e로 갈때는 k를 들러가야함

def getPath(s,e):
	k = V[s][e]
	if k == -1:	# 직접 가는 방법이면
		return f'=>{e}'
	return getPath(s,k) + getPath(k,e)

for s in range(num_vertex):
	for e in range(num_vertex):
		if s == e: continue
		path = getPath(s,e)
		cost = D[s][e]
		print(f'{s}{path} ({cost})')


