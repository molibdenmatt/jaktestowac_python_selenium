name = 'Bob'
workplace = 'office'
# Concatenation method
print('My name is ' + name + ' and I am working at the ' + workplace + '!')
# Old school method. Do not use.
print('My name is %s and I am working at the %s!' % (name, workplace))
# pyformat method:
print('My name is {} and I am working at the {}!'.format(name, workplace))
# f string
print(f'My name is {name} and I am working at the {workplace}!')

