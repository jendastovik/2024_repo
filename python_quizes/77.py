def get_parity_list(k, n, P):
    parity_list = []
    for i in range(P, k+n +1):
        if i & P == P:
            parity_list.append(i-1)
    return parity_list

print("get_parity_list(4, 3, 1): ", get_parity_list(4, 3, 1))
print("get_parity_list(4, 3, 2): ", get_parity_list(4, 3, 2))
print("get_parity_list(4, 3, 4): ", get_parity_list(4, 3, 4))

