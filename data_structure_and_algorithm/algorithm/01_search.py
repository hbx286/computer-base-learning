
def binary_search(value: int, arr: list[int]) -> int:
    """二分查找"""
    i, j = 0, len(arr) - 1
    while i < j:
        index = (i + j) // 2
        print(i, j, index)
        if value > arr[index]:
            i = index + 1
        elif value < arr[index]:
            j = index
        else:
            return index
    return -1


# def binary_search(value: int, arr: list[int]) -> int:
#     """二分查找"""
#     i, j = 0, len(arr) - 1
#     while i <= j:
#         index = (i + j) // 2
#         print(i, j, index)
#         if value > arr[index]:
#             i = index + 1
#         elif value < arr[index]:
#             j = index - 1
#         else:
#             return index
#     return -1


if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(binary_search(9, a))
    
    