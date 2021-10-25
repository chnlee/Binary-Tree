import sys
input = sys.stdin.readline
N, K = map(int,input().split())
lan = list()
for i in range(N):
  a = int(input())
  lan.append(a)
start = 1
end = max(lan)
result = 0 
while(start<=end):
  mid = (start + end) //2
  total = 0
  for i in lan:
    total += i // mid
  if total < K:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result) 