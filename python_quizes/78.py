def find_k(n):
    k = 0
    while 2**k < n + k + 1:
        k += 1
    return k

def positions(n):
    return [2**i - 1 for i in range(n)]

def get_msg_with_parity(message: str, ham_postitions, k):
    res = [-1 for l in range(len(message) + k)]
    msg_index = 0
    for i in range(len(res)):
        if i not in ham_postitions:
            res[i] = message[msg_index]
            msg_index += 1
    return res


print("original code: ", '1011', "hamming code: ", get_msg_with_parity('1011', positions(4), find_k(4)))
print("original code: ", '0110', "hamming code: ", get_msg_with_parity('0110', positions(4), find_k(4)))