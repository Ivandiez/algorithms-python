def euklidean_algorithm(a: int, b: int) -> int:
    """
    Function for search Greatest Common Factor (GCT) for two number a an b
    """
    while (a != 0) and (b != 0):
        if a < b:
            b %= a
        else:
            a %= b

    return a + b        # a + b == GCT


# The dict of (a,b): GCT - test data
test_data = {
    (10, 6): 2,
    (24, 5): 1,
    (27, 9): 9,
    (105, 30): 15,
    (240, 44): 4
}

# Testing algorithm
for pair in test_data:
    a, b = pair # a = pair[0], b = pair[1]
    answer = euklidean_algorithm(a, b)
    print('GCT({0}, {1}) - {2} : {3}'.format(pair[0], pair[1], answer, answer == test_data[pair]))
