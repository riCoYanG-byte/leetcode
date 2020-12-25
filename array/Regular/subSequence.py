def isValidSubsequence(array, sequence):
    # Write your code here.
    po1 = 0
    po2 = 0
    while po1 < len(array) and po2 < len(sequence):
        if array[po1] == sequence[po2]:
            po2 = po2 + 1
        po1 = po1 + 1

    return po2 == len(sequence)


