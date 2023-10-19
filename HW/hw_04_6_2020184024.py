array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227,
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3,
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92,
       83,     100,      94,      40,       5,     458,     364,      26,      64,      35,
       90,     489,      72,     504,      88,      97,     226,     218,     186,      68,
]

def bubble_sort(arr):
  print('-' * 60)
  print('Bubble Sort')
  print(f'before: {arr}')
  count = len(array)

  for a in range(count - 1):
    for b in range(count - 1 - a):
      if arr[b] > arr[b+1]:
        arr[b], arr[b+1] = arr[b+1], arr[b]

  print(f'after : {arr}')

def select_sort(arr):
  print('-' * 60)
  print('Selection Sort')
  print(f'before: {arr}')
  count = len(arr)
  N = 0
  while N < count: # N개의 최솟값을 찾는다
    min_value = arr[N]
    min_at = N
    M = N+1
    while M < count: # 최솟값이 어디있는지 찾는다
      if min_value > arr[M]:
        min_value = arr[M]
        min_at = M
      M += 1
    arr[N], arr[min_at] = arr[min_at], arr[N]
    N += 1
  print(f'after : {arr}')

def insert_sort(arr):
  print('-' * 60)
  print('Insertion Sort')
  print(f'before: {arr}')
  count = len(arr)
  N = 1
  while N < count: # 1st loop: 1번째(두번째)부터 끝까지 주인공 시켜준다
    v = arr[N]
    M = N
    while M > 0: #2nd loop: 주인공을 가능한곳까지 왼쪽으로 보낸다
      if arr[M-1] > v:
        arr[M], arr[M-1] = arr[M-1], arr[M]
        M -= 1
      else:
        break
    N += 1

  print(f'after : {arr}')


def shell_sort(arr):
  print('-' * 60)
  print('Shell Sort')
  print(f'before: {arr}')
  count = len(arr)
  gap = len(arr) // 3

  while gap >= 1:            # 1: 캡을 점점 줄여서 1까지 돌린다
    N = gap
    while N < count:        # 2: 갭부터 끝까지 주인공 시켜준다
      v = arr[N]
      M = N
      while M > 0:    # 주인공을 가능한 곳 까지 왼쪽으로 보낸다
        if arr[M-gap] > v:
          arr[M], arr[M-gap] = arr[M-gap], arr[M]
          M -= gap
        else:
          break
      N += gap
    if gap == 2:
      gap = 1
    else:
      gap = gap // 3


  print(f'after : {arr}')


def main():
  bubble_sort(array[:])
  insert_sort(array[:])
  select_sort(array[:])
  shell_sort(array[:])

if __name__ == '__main__':
  main()