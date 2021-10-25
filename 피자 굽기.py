#결국 이문제는 피자의 쌓인 위치, 쌓였는지의 여부가 중요한 법이다.
D, N = map(int,input().split())
oven = list(map(int,input().split()))
doughs = list(map(int,input().split()))

for i in range(1,len(oven)):
  if oven[i] > oven[i-1]:
    oven[i] = oven[i-1]

pilled_loc = 0
start, end = 0, len(oven) -1

for dough in doughs:
  is_pilled = False

  while start <=end:
    mid = (start+end) //2
    diameter = oven[mid]
    if dough >= diameter:
      pilled_loc = mid
      start = mid +1
      is_pilled = True
    else:
      end = mid - 1
  
  if not is_pilled:
    pilled_loc = -1
    break
  
  start =0
  end = pilled_loc-1


if pilled_loc == -1:
  print(0)

else:
  print(pilled_loc+1) 