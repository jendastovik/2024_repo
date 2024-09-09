def check_error(msg):
    index0 = 0
    index1 = int(len(msg) / 3)
    index2 = int(len(msg) / 3 * 2)

    for i in range(int(len(msg)/3)):
        if msg[index0] != msg[index1] or msg[index0] != msg[index2] or msg[index1] != msg[index2]:
            return True  
        index0 += 1
        index1 += 1
        index2 += 1
    return False

def correct_message(msg):
    index0 = 0
    index1 = int(len(msg) / 3)
    index2 = int(len(msg) / 3 * 2)
    final = ""

    for i in range(int(len(msg)/3)):
        if msg[index0] == msg[index1] or msg[index0] == msg[index2]:
            final += msg[index0]
        elif msg[index1] == msg[index2]:
            final += msg[index1]
        else:
            raise ValueError("Error")
        index0 += 1
        index1 += 1
        index2 += 1

    return final

print("checking code: 100111001011001110010110011100101")
print("value: ", check_error('100111001011001110010110011100101'))

print("checking code: 011101111101110111110111001111")
print("value: ", check_error('011101111101110111110111001111'))
print("corrected message: ", correct_message('011101111101110111110111001111'))


        



