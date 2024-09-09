def find_k(n):
    k = 0
    while 2**k < n + k + 1:
        k += 1
    return k

def ham_position(k):
    return [2**i - 1 for i in range(k)]

def get_parity_list(k, n, P):
    parity_list = []
    for i in range(k+n):
        if i & P == P:
            parity_list.append(i)
    return parity_list


def get_parity(message: str, parity_list):
    parity = 0
    for P in parity_list:
        parity += int(message[P-1])
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
    ham_postitions = ham_position(k)
    res = get_msg_with_parity(message, ham_postitions, k)
    for P in ham_postitions:
        parity_list = get_parity_list(k, n, P)
        parity = get_parity(res, parity_list)
        res[P] = parity
    res = [str(i) for i in res]
    return ''.join(res)

print("original code: ", '1011', "hamming code: ", hamming_code('1011'))
print("original code: ", '0110', "hamming code: ", hamming_code('0110'))
print("original code: ", '101010', "hamming code: ", hamming_code('101010'))


