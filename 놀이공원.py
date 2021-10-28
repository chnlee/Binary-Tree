# 결국 처음 이분탐색으로 접근해서 총 탑승시간을 구하려던 의도는 맞출 수 있어서 좋았다.
# 그러나 이 문제의 핵심은 이분탐색도 물론이거니와 바로 전 시간대 탑승한 사람의 수를 구한 후, 그 시간대에 탑승한 사람을 index별로 구하여, 더 이상 0으로 떨어지지 않을 때의 index를 구하는것이다.
# 이분탐색 뿐만 아니라 전 시간대의 사람 수를 구하는 문제이다.
N, K = map(int,input().split())
x = list(map(int,input().split()))
if N<K:
  print(N)
else:
  start = 0
  end = max(x) * N
  result = 0
  while(start <= end):
    mid = (start + end) // 2
    temp = K
    for i in x:
      temp += mid// i
    if temp >= N:
      result = mid
      end = mid -1
    else:
      start = mid + 1

  #result-1에 탑승한 아이들의 숫자를 계산한다.
  count = K 
  for i in x:
    count += (result - 1) // i
  for i in range(K):
    #t시간에 탑승한 아이
    if result % x[i] == 0:
      count += 1
    if count == N:
      print(i+1)
      break
    

