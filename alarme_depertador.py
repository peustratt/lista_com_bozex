"""
>>> calcular_tempo(1,5,3,5)
120
>>> calcular_tempo(23,59,0,34)
35
>>> calcular_tempo(21,33,21,10)
1417
>>> calcular_tempo(0,0,0,0)
None
"""


def calcular_tempo(h1, m1, h2, m2) -> int:
    time_1 = converter_hora_min(h1) + m1
    time_2 = converter_hora_min(h2) + m2
    if time_1 - time_2 == 0 or time_2 - time_1 == 0:
        pass
    elif time_1 < time_2:
        return time_2 - time_1
    else:
        return converter_hora_min(23-h1) + (60-m1) + converter_hora_min(h2)+m2


def converter_hora_min(h):

    return h*60

calcular_tempo(1,5,3,5)

