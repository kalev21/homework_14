from typing import Any
from re import sub
from re import findall
import collections

# def count_unique_elems(arr: list[Any]) -> int:
#     # Задача_1
#     # arr_1 = []
#     # for num in arr:
#     #     if num not in arr_1:
#     #         arr_1.append(num)
#     # return len(arr_1)

    # Задача_2
# def get_10_popular_password(file: str) -> Any:
#     pop_password = []
#     with open(file, 'r') as f:
#         for line in f:
#             pop_password.append(line.split(';')[-1].rstrip('\n'))
#     return collections.Counter(pop_password).most_common(10)

    # Задача_3
def censor_link(string: str) -> str:
    return sub(r'(http[s]://)?(www.)?([a-z]\w+\.)+([a-z]{2,})', '******', string)

def main():
    # Задача_1
    # arr = [1, 5, 1, 2, 3, 9, 23, 4]
    # print(count_unique_elems(arr))

    # Задача_2
    # pop_pass = 'pwd.txt'
    # print(f'Топ-10 самых популярных паролей: \n{get_10_popular_password(pop_pass)}')

    # Задача_3
    links = [
        'vk.com',
        'www.vk.com',
        'http:vk.com',
        'httpsvk.com',
        'https:mail.net',
        'lesson.su',
        'ссылка на www.ru'
    ]
    for replace in links:
        print(censor_link(replace))

if __name__ == '__main__':
    main()