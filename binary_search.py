import random

def binary_search(n: int, arr: list) -> int:
    """
    This function take n and arr, than search in left or right middle of arr the n.
    Difficult of this algorithm is O(log(N)) < O(N)
    :param n: number for search in arr
    :param arr: sorted list of numbers
    :return: index of arr, where we can paste the n
    """
    if len(arr) == 0:
        return 0

    left = 0
    right = len(arr)

    while left < right:
        middle = (left + right) // 2        # Divide the arr for 2 parts

        if arr[middle] < n:                 # search, there is the n
            left = middle + 1               # if n in right part, left part is drop
        else:
            right = middle                  # else right part is drop

    return left


def generate_data(n, length):
    """
    This function used for generate test data for binary_search
    :param n: number of returned arrays
    :param length: len of returned arrays
    :return: arrays
    """
    start = 20
    end = 50
    for i in range(n):
        arr = [random.randint(start, end)
               for i in range(length)]
        k = random.randint(start, end)
        start = end
        end += 20
        yield sorted(arr), k


test_data = generate_data(5, 10)

for pair in test_data:
    arr, n = pair
    print('Answer for ({0}, {1}) is {2}'.format(n, arr, binary_search(n, arr)))