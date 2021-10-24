N = int(input())
x = list(map(int,input().split()))
x.sort()
def binary_search(array,target,start,end):
  while(start<=end):
    mid = (start+end) //2
    if array[mid] == target:
      return '1'
    elif array[mid]>target:
      end = mid - 1
    else:
      start = mid + 1
  return '0'
M = int(input())
y = list(map(int,input().split()))

for i in y:
  result = binary_search(x,i,0,N-1)
  print(result,end= " ")