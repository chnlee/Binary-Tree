N = int(input())
K = int(input())

# 결국 K번째의 수 : B[K]는 절대로 K보다 작거나 같은 수보다 크지못함을 이해해야 이 문제를 풀 수 있다.
# 이문제의 핵심은 굳이 배열로 전개하지 않더라도 이분탐색으로 문제를 풀 수 있다는 것이다. 
# 아직 100% 이해된 것은 아니지만, 그래도 얼추 이해한 상태로 코드를 작성해보겠다.
# 시작은 1, 끝은 K이다.
# 끝이 K인 이유가 중요한데, K 번째 수는 절대로 K를 넘을 수 없다. 
# 예를 들어 B[7]은 7을 넘을 수 없다
# 이는 당연한 결과이다.
start = 1
end = K
while start <= end:
  mid = (start + end) // 2
  # mid의 값을 설정하고, 이제 temp에다가 mid보다 작거나 같은 수를 담아보자
  temp = 0
  for i in range(1,N+1):
    # mid보다 작거나 같은 수는 mid를 각 열마다 i로 나눈 값이다.
    #그렇지만 이 떄, i가 너무 작거나, mid가 너무 큰 경우 N을 넘어가 버린다. 따라서 N으로 제한을 둘 필요가 있다.
    temp += min(mid//i, N)
  #만약 temp가 K를 넘어버리면, 즉, mid보다 작거나 같은 수가 K를 넘어버리면 그 mid값이 정답임을 알 수 있다.
  if temp >= K:
    result = mid
    end = mid -1
  else:
    start = mid +1  

print(result)
