# _2 Chained Matrix Multiplication

d = [5,9,3,7,2,6,3,9,3]	# 5*9, 9*3, 3*7, 7*2, 2*6, 6*3, 3*9, 9*3
mc = len(d) - 1	# 최초 부분문제 수

INF = float('inf')
C = [[0 for _ in d] for _ in d]	# 산술 연산의 횟수를 저장, 1-based index를 사용, d = mc + 1
P = [[0 for _ in d] for _ in d]	# 마지막 곱셈의 위치, 1-based index를 사용

for sps in range(2, mc + 1):		# sub-problem size, 2 ~ mc, mc도 포함(mc+1)
	for s in range(1, mc - sps + 2):	# s: start
		e = s + sps - 1							# e: end, e is inclusive
		mult = INF
		for k in range(s, e):				# k: 마지막 곱셈의 위치
			t = C[s][k] + C[k+1][e] + d[s-1] * d[k] * d[e]						# 임시거리: s-k 곱셈수 + (k+1)-e곱셈수 + (s-k)*(k-e)곱셈수 s행 * k열
			if mult > t:		# 갱신해야한다면
				mult = t
				P[s][e] = k
		C[s][e] = mult

def getMultStr(s,e):
	if s == e: return f'A{s}'
	p = P[s][e]
	return f'({getMultStr(s,p)} x {getMultStr(p+1, e)})'


print(f'곱셈수={C[1][mc]} 수식={getMultStr(1,mc)}')






