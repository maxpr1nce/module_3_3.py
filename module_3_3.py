def print_params(a=1, b='строка', c=True):
    print(f'a = {a}, b = {b}, c = {c}')

print_params()
print_params(10)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [42, 'hello', [1, 2, 3]]
values_dict = {'a': 100, 'b': 'world', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [10, 'abc']
print_params(*values_list_2, 42)