# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
translat = {'One': 'Один',
       'Two': 'Два',
       'Three': 'Три',
       'Four': 'Четыре'
       }
with open('my3.txt', 'r', encoding='utf-8') as my_file:
    new = []
    for i in my_file:
        i = i.split(' ')
        new.append(translat[i[0]] + ' ' + i[2])
        print(new)

with open('my4.txt', 'w', encoding='utf-8') as f:
    f.writelines(new)


print(new)