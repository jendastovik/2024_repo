def get_parity_list(k, n, P):
    parity_list = []
    for i in range(k+n):
        bin_i = bin(i)
        if i & P == P:
            parity_list.append(i)
    return parity_list

print("get_parity_list(4, 3, 1): ", get_parity_list(4, 3, 1))
print("get_parity_list(4, 3, 2): ", get_parity_list(4, 3, 2))
print("get_parity_list(4, 3, 3): ", get_parity_list(4, 3, 3))

