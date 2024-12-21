def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_lis = [472, True, 'homework']
values_dic = {'a' : 897, 'b' : False, 'c' : 'Python'}
print_params(*values_lis)
print_params(**values_dic)
values_list_2 = [734.463, True]
print_params(*values_list_2, 42)