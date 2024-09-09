def check_message(message: str):
    num = 0
    for i in range(1, len(message)):
        if message[i] == '1':
            num += 1
    return num%2 == int(message[0])


print("checking code: 100111001011001110010110011100101")
print("value: ", check_message('100111001011001110010110011100101'))

print("checking code: 011101111101110111110111001111")
print("value: ", check_message('011101111101110111110111001111'))
    