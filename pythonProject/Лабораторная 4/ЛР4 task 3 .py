from catalog import number_operation
from catalog import string_operation
res_add= number_operation.addition(5, 3)
print(f'Сумма введённых чисел:{res_add}')
res_mul= number_operation.multiplication(5, 3)
print(f'Произведение введённых чисел: {res_mul}')
res_con= string_operation.concatenation('Zhest', 'Umniy')
print(f'Объединение введённых строк: {res_con}')
res_up= string_operation.upperer('маленькие превращаются в большие')
print(res_up)
res_low= string_operation.low('А БОЛЬШИЕ ПРЕВРАЩАЮТСЯ В МАЛЕНЬКИЕ')
print(res_low)