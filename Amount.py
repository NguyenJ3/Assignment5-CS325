def amount(A, S):
    # sort the list A in ascending order
    A.sort()
    # initialize the result list to store the combinations
    result = []
    # initialize the combination list to store the current combination
    combination = []
    
    for i in range(len(A)):
        if i > 0 and A[i] == A[i - 1]:
            continue 
        
    combination.append(A[i])

    target = S - A[i]

    if target == 0: 
        result.append(list(combination)) #appends the target to the list 
    elif target > 0: 
        pass 
    else: 
        break 
    combination.pop()
    