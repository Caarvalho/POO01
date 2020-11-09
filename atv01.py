def printDecimal(num):
    print(f'{num:<10}', end=' ')


def printBinario(num):
    print(f'{bin(num)[2:]:15}', end=' ')


def printOctal(num):
    print(f'{oct(num)[2:]:10}', end=' ')

def printHexadecimal(num):
    print(f'{hex(num)[2:]:>5}')


def imprimirTabela():
    for num in range(0, 256):
        printDecimal(num)
        printBinario(num)
        printOctal(num)
        printHexadecimal(num)


print('DECIMAL    BINÁRIO         OCTAl          HEXADECIMAL')
print('-------    -------         -----          -----------')
imprimirTabela()


