def find_k(n):
    k = 0
    while 2**k < n + k + 1:
        k += 1
    return k

def ham_position(k):
    return [2**i - 1 for i in range(k)]

def get_parity_list(k, n, P):
    parity_list = []
    for i in range(P+1, k+n +1):
        if i & P == P:
            parity_list.append(i-1)
    return parity_list


def get_parity(message: str, parity_list):
    parity = 0
    for P in parity_list:
        parity += int(message[P])
    # print(f"parity for {parity_list} is {parity%2}")
    return parity % 2

def get_msg_with_parity(message: str, ham_postitions, k):
    res = [-1 for l in range(len(message) + k)]
    msg_index = 0
    for i in range(len(res)):
        if i not in ham_postitions:
            res[i] = message[msg_index]
            msg_index += 1
    return res

def hamming_code(message: str):
    n = len(message)
    k = find_k(n)
    positions = ham_position(k)
    res = get_msg_with_parity(message, positions, k)
    for P in positions:
        parity_list = get_parity_list(k, n, P+1)
        # print(f"parity_list for {P+1} is {parity_list}")
        parity = get_parity(res, parity_list)
        res[P] = parity
    res = [str(i) for i in res]
    return ''.join(res)

print("original code: ", '1011', "hamming code: ", hamming_code('1011'))
print("original code: ", '1111', "hamming code: ", hamming_code('1111'))
print("original code: ", '1001', "hamming code: ", hamming_code('1001'))


