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

# kruskal: 입출력 모두 Edge list

mst = []

# def key_f(edge):
# 	return edge[2]
# 한번쓰고 말 비교 key function을 만드는것은 별로임. lambda식으로 정렬하자
edges.sort()
s_edges = sorted(edges, key=lambda e: e[2])	# edges 리스트를 정렬하여 s_edges에 저장, 다만 객체지향적 관점에서 형태가 별로임 # sort의 튜플간 비교(기본값): 첫번째 원소의 크기로 비교함

# roots = []
# for i in range(num_vertex):
# 	roots.append(i)
roots = [i for i in range(num_vertex)]	# i에 대한 집합, 초기 root는 자기 자신을 가짐(union-find에서)

def getRoot(v):
	# return roots[v] -> 만으로는 제대로된 결과X, 루트를 계속 따라들어가봐야함
	r = roots[v]
	if r == v:
		return r
	roots[v] = getRoot(r)		# 경로 압축
	return roots[v]


def connect(v1, v2):
	# roots[v1] = v2	# 여기도 마찬가지로 제대로된 결과 X, 루트를 계속 따라가지 않는다면 둘중 하나의 트리가 끊어져버림
	r1 = getRoot(v1)	# v1의 루트를 쭉 따라가 구함
	r2 = getRoot(v2)	# v2의 루트를 쭉 따라가 구함
	roots[r1] = r2
	pass


# while? for? : loop를 돌 대상이 있다면 for, 조건이 만족될때까지 loop를 돌면 while
# 기존의 코드에서는 while 사용(ch4_1_mst_kruskal), 이번에는 for루프를 사용
# for: 정렬된 리스트에 대해서 수행하다가 완성된다면 break
for edge in s_edges:
	s, e, w = edge	# start, end, weight, start와 end의 root가 같다면 같은트리에 존재 -> 사이클
	# 1. if makes cycle: continue	-> 사이클이 형성된다면 mst에 추가하지 않음. 아래와 같이 수행
	if getRoot(s) == getRoot(e): continue
	mst.append(edge)
	# 2. connected two vertices	-> 두개의 정점을 이어준다. 아래와 같이 수행
	connect(s,e)
	if len(mst) == num_vertex - 1: break	# 정점수 이상으로 mst에 담지 않는다


print(mst)


