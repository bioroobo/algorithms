# Обмен значениями между двумя переменными
a,b=1,2
print('starting value:         ', 'a=', a, '  b=', b)

# через одну переменную
c=a
a=b
b=c
print('through one variable:   ', 'a=', a, '  b=', b)

# питоновский синтаксис
a,b = b,a
print('exchange through sync : ', 'a=', a, '  b=', b)

# исключающее или
a = a ^ b
b = a ^ b
a = a ^ b
print('exchange XOR :          ', 'a=', a, '  b=', b)

