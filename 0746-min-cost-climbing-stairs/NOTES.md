# example 2
[1,100,1,1,1,100,1,1,100,1]
n = 10
arr = [0,0,0,0,0,0,0,0,0,0]
arr[0] = cost[0] = 1
arr[1] = cost[1] = 100

for i in range(2,10):
      arr[i] = cost[i] + min(arr[i-1], arr[i-2])

i=2 arr[2] = cost[2] + min(arr[1], arr[0])
     arr[2] = 1 + min(1,100)
     arr[2] = 1 + 1 = 2

 i=3 arr[3] = cost[3] + min(arr[2], arr[1])
     arr[3] = 1 + min(2,100)
     arr[3] = 1 + 2 = 3

 i=4 arr[4] = cost[4] + min(arr[3], arr[2])
     arr[4] = 1 + min(3,2)
     arr[4] = 1 + 2 = 3

 i=5 arr[5] = cost[5] + min(arr[4], arr[3])
     arr[5] = 100 + min(3,3)
     arr[5] = 100 + 3 = 103

 i=6 arr[6] = cost[6] + min(arr[5], arr[4])
     arr[6] = 1 + min(103,3)
     arr[6] = 1 + 3 = 4****

 i=7 arr[7] = cost[7] + min(arr[6], arr[5])
     arr[7] = 100 + min(4,103)
     arr[7] = 1 + 4 = 5

 i=8 arr[8] = cost[8] + min(arr[7], arr[6])
     arr[8] = 100 + min(5,4)
     arr[8] = 100 + 4 = 104

 i=9 arr[9] = cost[9] + min(arr[8], arr[7])
     arr[9] = 1 + min(104,5)
     arr[9] = 1 + 5 = 6

 return min(arr[n-1], arr[n-2])
 return min(arr[9], arr[8])
 [1,100,2,3,3,3,103,4,5,104,6]
