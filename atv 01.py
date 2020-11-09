def decimal_binario(num):
    return bin(num)[2:]


def decimal_octal(num):
    return oct(num)[2:]


def decimal_hexa(num):
    return hex(num)[2:]


def tabela(num):
    print(f'{num:<10}{decimal_binario(num):15}{decimal_octal(num):10}{decimal_hexa(num):10}')


print('DECIMAL   BINÁRIO        OCTAl     HEXADECIMAL')
print('-------   -------        -----     -----------')


for i in range(0, 256):
    tabela(i)


