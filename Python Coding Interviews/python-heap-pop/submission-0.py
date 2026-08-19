import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    ls_pops = []
    while heap: 
        e = heapq.heappop(heap)
        ls_pops.append(e)
    return ls_pops


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
