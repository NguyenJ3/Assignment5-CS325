def amount(A, S):
    A.sort()
    result = []
    combination = []
    for i in range(len(A)):
        if i > 0 and A[i] == A[i - 1]:
            continue
        combination.append(A[i])
        target = S - A[i]
        if target == 0:
            result.append(list(combination))
        elif target > 0:
            for j in range(i + 1, len(A)):
                if j > i + 1 and A[j] == A[j - 1]:
                    continue
                combination.append(A[j])
                target -= A[j]
                if target == 0:
                    result.append(list(combination))
                elif target > 0:
                    continue
                else:
                    break
                # remove the last element from the combination if the target sum is not equal to 0
                combination.pop()
        else:
            # remove the last element from the combination if the target sum is not equal to 0
            combination.pop()
            continue
    return result