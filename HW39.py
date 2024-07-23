from pprint import pprint
import inspect


def introspection_info(obj):
    print('Тип объекта:', type(obj))
    pprint(f'Методы и атрибуты объекта: {dir(obj)}')
    print('Проверка на модуль - ', inspect.ismodule(obj))
    print('Проверка на класс - ', inspect.isclass(obj))
    print('Родной файл - ',inspect.getmodule(obj))



introspection_info(introspection_info)
