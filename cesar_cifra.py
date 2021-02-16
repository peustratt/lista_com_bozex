"""
>>> cripto(2, 'VQREQFGT')
'TOPCODER'
>>> cripto(10, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
'QRSTUVWXYZABCDEFGHIJKLMNOP'
>>> cripto(0, 'TOPCODER')
'TOPCODER'
>>> cripto(25, 'ZWBGLZ')
'AXCHMA'
>>> cripto(1, 'DBNPCBQ')
'CAMOBAP'
>>> cripto(4, 'LIPPSASVPH')
'HELLOWORLD'
"""

alfabetox = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto = []

for letra in alfabetox:
    alfabeto.extend(letra.upper())

def cripto(n, string):
    message = []
    splitada = []

    for letra in string:
        splitada.extend(letra)
    for letra in splitada:
        for index, a in enumerate(alfabeto):
            if letra == a:
                    message.extend(alfabeto[index - n])

    return ''.join(message)



