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

class MST:
  def __init__(self, nv):
    self.roots = []
    self.edges = []
    self.nv = nv
  def append(self, s, e, w):
    if s <= e:
      self.edges.append((s,e,w))
    else:
      self.edges.append((e,s,w))
    self.edges.sort(key=lambda e:e[0]*1000+e[1])

  def full(self):
    return len(mst.edges) == num_vertex - 1
  def onSameTree(self, u, v):
    return self.getRoot(u) == self.getRoot(v)
  def getRoot(self, v):
    r = self.roots[v]
    if r == v:
      return r
    self.roots[v] = self.getRoot(r)  # 경로 압축
    return self.roots[v]
  def connect(self, u, v):
    r1 = self.getRoot(u)  # v1의 루트를 쭉 따라가 구함
    r2 = self.getRoot(v)  # v2의 루트를 쭉 따라가 구함
    self.roots[r1] = r2
  def __repr__(self):
    return str(self.edges)

mst = MST(num_vertex)

s_edges = sorted(edges, key=lambda e:e[2])
mst.roots = [i for i in range(num_vertex)]


for edge in s_edges:
	s, e, w = edge
	if mst.onSameTree(s,e): continue
	mst.edges.append(edge)
	mst.connect(s,e)
	if mst.full(): break	# 정점수 이상으로 mst에 담지 않는다



print(mst.edges)



