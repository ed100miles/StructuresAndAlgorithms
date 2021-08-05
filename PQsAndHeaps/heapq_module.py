"""Look at python standard lib heapq module
NOTE: heapq doesnt seperately manage associated values, elements serve as their own key.
"""

import heapq
import random

# heapq allows standard python list to be managed as a heap
heap = []

# Heappush: automatically satisfies heap-order property. O(log n)
print("Heappush's:")

for _ in range(10):
    heapq.heappush(heap, random.randint(1,100))
print(heap, end='\n\n')

# Heappop: pop and return min element and reestablish heap-order property O(log n)
print("Heappop's:")

print(heapq.heappop(heap))
print(heapq.heappop(heap), end='\n\n')

# Heappushpop: push element and pop and return min. O(log n)
# *if pushed element is smallest it's immediately popped and returned 
print("Heappushpop's:")

print(heapq.heappushpop(heap, 100))
print(heap)
print(heapq.heappushpop(heap, 0))
print(heap, end='\n\n')




# Heapify: transforms UL to satisfy heap-order property, O(n) using bottom-up construction
print("Heapify:")
unordered_list = [9, 5, 7, 6, 1, 2]
heapq.heapify(unordered_list)
print(unordered_list)

