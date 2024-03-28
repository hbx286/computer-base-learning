
def selection_sort(arr: list):
    """
    选择排序
    对于0到n-1的数据, 找出1到n范围内最小值与0互换位置
    对于1到n-1的数据, 找出2到n范围内最小值与1互换位置
    ...
    对于n-2到n-1的数据, 找出n-1到n范围内最小值与n-2互换位置
    """
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp
    return arr


def bubble_sort(arr: list):
    """冒泡排序"""
    for k in range(len(arr) - 1, 0, -1):
        for i in range(k):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
    return arr


def bubble_sort_with_flag(arr: list):
    """冒泡排序"""
    for k in range(len(arr) - 1, 0, -1):
        flag = False
        for i in range(k):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
                flag = True
            print(arr)
        if not flag:
            break
    return arr


def insertion_sort(arr: list):
    """插入排序(未理解)"""
    for i in range(1, len(arr)):
        base = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > base:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = base
    return arr



if __name__ == '__main__':
    a = [5,4,6,10,1,3,7]
    # a = [6,5,4,3,2,1]
    print(insertion_sort(a))
    # print(bubble_sort_with_flag(a))
    # print(selection_sort(a))
    
    