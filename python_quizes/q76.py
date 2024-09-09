def positions(n):
    return [2**i - 1 for i in range(n)]

def get_msg_with_parity_bits(n, k):
    ham_postitions = positions(n)
    res = [0 for l in range(n + k)]
    msg_index = 0
    for i in range(len(res)):
        if i in ham_postitions:
            res[i] = 1
    return res

print("positions(3): ", positions(3))
print("get_msg_with_parity_bits(3, 3): ", get_msg_with_parity_bits(3, 3))
print("positions(4): ", positions(4))
print("get_msg_with_parity_bits(4, 3): ", get_msg_with_parity_bits(4, 3))
print("positions(5): ", positions(5))
print("get_msg_with_parity_bits(5, 4): ", get_msg_with_parity_bits(5, 4))
