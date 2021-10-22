# N,M = map(int,input().split())
# x = list(map(int,input().split()))
# x.sort()
# def binary_search(array,target,start,end):
#   while start <= end:
#     mid = (start+end) // 2
#     if array[mid] == target:
#       return target
#     elif array[mid] > target:
#       end = mid - 1
#     else:
#       start = mid + 1
#   return target

# for i in range(max(x),0,-1):
#   count = 0
#   result = binary_search(x,i,0,N-1)
#   for j in range(len(x)):
#     if x[j] >= result:
#       count += x[j] - result 
#     else:
#       continue
#   if count >= M:
#     break
# print(result)

n, m =list(map(int,input().split(' ')))

array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while(start<=end):
  total = 0
  mid = (start+end) //2
  for x in array:
    if x>mid:
      total += x-mid
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
  
print(result)
