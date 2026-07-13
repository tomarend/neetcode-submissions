from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    rev_list = []
    while len(arr) > 0:
        last_elem = arr.pop()
        rev_list.append(last_elem)
    
    return rev_list


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
