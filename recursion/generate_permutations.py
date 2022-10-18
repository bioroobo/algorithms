def gen_bin(M, prefix=''):
    """ Простой способ генерации для двоичной СС"""
    if M==0:
        print(prefix)
    else:
        #gen_bin(M-1, prefix+'0')
        #gen_bin(M-1, prefix+'1')
        #тоже самое только в цикле
        for digit in '0', '1':
            gen_bin(M-1, prefix + digit)


def generate_number(N:int, M:int, prefix=None):
    """ Генерирует все числа (с лидирующими нулями)
        в N-ричной системе счисления (N<=10) длины M
        N - Основание системы счисления
        M - количество чисел"""
    prefix = prefix or []
    if M == 0:
        print (prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop() # убрать последнюю цифру


def find(number, A):
    """ ищет number в A и возвращает True, если такой есть, False -- если такого нет"""
    for x in A :
        if number == x:
            return True
    return False

def generate_permutations(N:int, M:int=-1, prefix=None):
    """ Генерация всех перестановок N чисел в M позициях,
        с префиксом prefix"""
    M = N if M == -1 else M #это соответствует следующей записи: 
    #if M == -1:
    #    M = N # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        #print(prefix)
        # если красивее, то можно так распечатать:
        #print(prefix[0], prefix[1], prefix[2])
        #что соответствует:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop() # убрать последнюю цифру

################################################
generate_number(2,3)
gen_bin(3)

generate_permutations(3)

