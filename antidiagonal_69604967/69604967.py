def print_diagonal(A):
    
    n = len(A)
    m = len(A[0])
    result = []
    length = min(n, m)

    # Top-left to top-right
    for k in range(m):
        result.append([0 for _ in range(length)])
        i = 0
        j = k
        while j >= 0 and i < n:
            result[-1][i] = A[i][j]
            i = i + 1
            j = j - 1

    # Top-right to bottom-right
    for k in range(1,n): 
        result.append([0 for _ in range(length)])      
        i = k
        j = m - 1
        while j >= 0 and i < n:
            result[-1][i - k] = A[i][j]
            i = i + 1
            j = j - 1
    return result
        
A = [[1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12]]
print(print_diagonal(A))