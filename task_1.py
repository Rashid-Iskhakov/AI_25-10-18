# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок
# в этой строке. Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib
# или встроенную функцию hash()


my_string = 'papa'

def search_substr (s):
    hash_list = []
    hash_list.append(hash(s))
    count_subs = 0

    for i in range(len(s)):
        j = len(s)
        while j > i:
            if hash(s[i:j]) not in hash_list:
                hash_list.append(hash(s[i:j]))
                count_subs += 1
            j -= 1

    return count_subs

x = search_substr(my_string)
print(x)
