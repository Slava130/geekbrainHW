# 1 вариант

def person_data(**kwargs):
    """функция, принимает несколько параметров, описывающих данные пользователя, возвращает данные о пользователе
    словарём """
    return kwargs
print(person_data(name = 'Ivan', city ='Limerick', email = '123@mail.ru', phone=34567, surname='Ivanov', year=1875))

# 2 вариант

def person_data(name, surname, year, city, email, phone):
    """функция, принимает несколько параметров, описывающих данные пользователя,возвращает данные о пользователе картежем
    """
    return name, surname, year, city, email, phone

name, surname, year, city, email, phone = person_data(name='Ivan', city='Limerick', email='123@mail.ru', phone=34567, surname='Ivanov', year=1875)

print(name, surname, year, city, email, phone)


# 3 вариант

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите номер телефона: ')

def my_func (name, surname, year, city, email, telephone):
    """функция, принимает несколько параметров, описывающих данные пользователя, возвращает данные о пользователе
        списком """
    return '_'.join([name, surname, year, city, email, telephone])
print(my_func(surname = surname, name = name, year = year, city = city, email = email, telephone =phone ))