import heapq

"""
Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for all k, counting elements from 0. For the sake of comparison, non-existing elements are considered to be infinite. The interesting property of a heap is that a[0] is always its smallest element
"""
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print("largest 3 element is ",heapq.nlargest(3,nums))
print("smallest 3 element is ",heapq.nsmallest(3,nums))

heap = list(nums)
print("original list is ",heap)
heapq.heapify(heap)
print("queue is ",heap)

