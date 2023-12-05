
def coinChange(change):
	exchange = {500:0, 100:0, 50:0, 10:0}
	sum = 0
	for c in exchange.keys():
		count = 0
		while True:
			sum += c
			count += 1
			if sum > change:
				sum -= c
				count -= 1
				exchange[c] = count
				break
			elif sum == exchange:
				break
		if sum == change:
			return exchange




coin = (500, 100, 50, 10)
change = int(input('>> '))
print(coinChange(change))
