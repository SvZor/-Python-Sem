# def copy(a: list) -> list:
#     return a[:]

# copy('abcd')


# data = {
#     'name' : 'john',
#     'age' : 20,
#     'salary' : 8000,
#     'city' : 'Boston'
# }

# data.setdefault ('saiary' , 7000)
# print(data)

def say_halloo (name, greeting = 'Hello'):
    return f'{greeting}, name'
# say_halloo (greeting = 'Hi' , 'John') № не верно, так как в функции константа закреплена
say_halloo ('John') # верно