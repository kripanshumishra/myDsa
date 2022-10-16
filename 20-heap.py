# arr = [5, 7, 9, 1, 3]
arr = [[1,7],[2,5],[3,2]]

# arr = [[7,1],[5,2],[2,3]]
import heapq
heapq.heapify(arr)
print(arr)
# print(heapq.heappop(arr))
# print(arr)
# print(heapq.heappop(arr))
# print(arr)
arr1 = [[-1,7],[-2,5],[-3,2]]
heapq.heapify(arr1)
print(arr1)
#there is nothing like maxheap in python so what we can do is , we can interst element with - sign in heap 
#that will work completely fine