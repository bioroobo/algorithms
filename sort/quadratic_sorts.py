# The Quadratic Sorting Algorithms: Insertion, Selection and Bubble Sort.

def insertion_sort(lst):
    """ Сортировка вставками.
        Индекс массива i задает начало элемента итерации сравнений значений пар элементов
        Это будет выглядеть, как сдвиг текущей метки на массиве – метка от которой будет идти
        сравнение до конца массива.
        В этом передвижении i будем сравнивать элементы от A[i-1] до последнего A[N-1].
        Т.е. вводим ещё один индекс j, который будет принимать значения на каждой итерации i:
        от i-1 до N-2.
        Сравниваем текущий элемент A[j] со следующим A[j+1]. Если A[j] > A[j+1],
        то меняем значения местами: A[j],A[j+1]= A[j+1],A[j]
    """
    n = len(lst)
    for i in range(1,n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    comment = """
    #код Хирьянова через while:
    N = len(A)
    for top in range(1,N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    """

 
def selection_sort(lst):
    """ 1.берем A[0]. Последовательно сравниваем все элементы и меняем значение с A[0],
        если A[j] < A[0]. Таким образом при первом проходе в A[0] будет наименьшее значение.
        2.Повторяем с A[1] до предпоследнего элемента (последний будет уже на своем месте)
    """
    n = len(lst)
    for i in range(n-1):
        for j in range(i+1,n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


def bubble_sort(lst):
    """ 1.Берем два элемента A[0] и A[1] – сравниваем и при необходимости меняем(если A[0]>A[1]).
        Проходим с начала и до конца по-парно. В результате в последнем элементе будет самое
        большое значение.
        2.Повторяем с начала и до предпоследнего – теперь в предпоследнем будет наибольшее из
        пройденных
        3.проходим до тех пор, пока останется сравнить только A[0] и A[1]
    """
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
               
    comment = """
    #код Хирьянова:
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    """


# -----------------------------------------
def test_quadratic_sort(sort_algorithm):

    a = [4,2,5,1,3]
    a_sort = [1,2,3,4,5]
    sort_algorithm(a)
    print(sort_algorithm.__name__, '#test1: ', end='')
    print('OK' if a==a_sort else 'FAIL')

    a = [4,1,4,1,3]
    a_sort = [1,1,3,4,4]
    sort_algorithm(a)
    print(sort_algorithm.__name__, '#test2: ', end='')
    print('OK' if a==a_sort else 'FAIL')

# -----------------------------------------



###### RUN TEST ###########################
if __name__ == '__main__':
    test_quadratic_sort(insertion_sort)
    test_quadratic_sort(selection_sort)
    test_quadratic_sort(bubble_sort)
