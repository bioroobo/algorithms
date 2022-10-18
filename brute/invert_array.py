def invert_array(A:list, N:int):
    """ Обращение массива (поворот задом-наперед)
        в рамках индексов от 0 до N-1
    """
    for i in range(N//2):
        A[i], A[N-1-i] = A[N-1-i], A[i]

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print('#test1 - OK')
    else:
        print('#test1 - FAIL')

    A2 = [0, 0, 0, 0, 10, 0, 0, 0]
    print(A2)
    invert_array(A2, 5)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('#test2 - OK')
    else:
        print('#test2 - FAIL')


########################################
test_invert_array()
