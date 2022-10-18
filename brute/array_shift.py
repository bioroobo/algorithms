# циклический сдвиг влево - cycle shift left

N = 5
A = [0,1,2,3,4]
print('array A:',A)
tmp = A[0]
for i in range(N-1):
    A[i] = A[i+1]
A[N-1] = tmp
print('shift of array A to the left:', A)

# циклический сдвиг вправо - cycle shift right 
N = 5
B = [3,4,5,6,7]
print('array B:', B)
tmp = B[N-1]
for i in range(N-1, 0, -1):
    B[i] = B[i-1]
B[0] = tmp
print('shift of array B to the right:', B)
 



