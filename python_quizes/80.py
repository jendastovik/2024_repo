def F(N:list):
    if len(N) == 1:
        return N[0]
    else:
        M = F(N[1:])
        if N[0] > M:
            return N[0]
        else:
            return M
        
print(f"F([1, 2, 3, 4, 5]): {F([1, 2, 3, 4, 5])}")
print(f"F([5, 4, 3, 2, 1]): {F([5, 4, 3, 2, 1])}")
print(f"F([13,10, 5, 7, 9, 3, 2, 6, 8, 1]): {F([13,10, 5, 7, 9, 3, 2, 6, 8, 1])}")