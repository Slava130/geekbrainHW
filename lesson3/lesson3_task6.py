def int_func(words):
    import re
    a = words
    if re.search(r'[^a-z]', a):
        return 'слова должны быть написаны латинскими прописными буквами'
    else:
        return a.title()


b = input('Введите слова через пробел с маленкой буквы:  ').split()
for item in b:
    print(int_func(item), end=' ') 
