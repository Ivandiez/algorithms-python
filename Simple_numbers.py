def eratosthenes_sieve(n: int) -> list:
    """
    This function take the natural number and return the list of simple numbers
    from 2 to input
    :param n: Natural number
    :return: list of simple numbers
    """
    numbers = list(range(2, n + 1))

    for i in range(2, int(n / 2)):
        t = 2 * i
        while t <= n:
            numbers[t - 2] = 0     # create a mask, that contains 1 and 0
            t += i

    numbers = list(set(numbers))    # remove repetitions
    numbers.remove(0)               # drop extra 0
    numbers.sort()

    return numbers


test_data = {
    10: [2, 3, 5, 7],
    28: [2, 3, 5, 7, 11, 13, 17, 19, 23],
    47: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
}

for number in test_data:
    answer = eratosthenes_sieve(number)
    print('List of simple numbers of {0} - {1} : {2}'.format(number, answer, answer == test_data[number]))