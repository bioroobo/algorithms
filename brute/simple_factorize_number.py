def is_simple_number(x):
    """ Определяет, является ли число простым.
        x - целое положительное число
        Если простое, то возвращает True, а иначе - False
        Простое число — натуральное (целое положительное) число, имеющее ровно два
        различных натуральных делителя — единицу и самого себя. 
    """
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor += 1
    return True


def factorize_number(x):
    """ Раскладывает число на множители.
        Печатает их на экран.
        x - целое положительное число
    """
    divisor = 2
    while x > 1 :
        if x % divisor == 0 :
            print(divisor, end=" ")
            x //= divisor
        else:
            divisor += 1





