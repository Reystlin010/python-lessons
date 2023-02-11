from typing import Optional


def numbers_to_text(numbers: str) -> Optional[str]:
    '''Функция преобразует строки формата "222 33 4444" в текст,
    как если бы он был набран на кнопочном телефоне
    '''

    legend = {
        '1': '.,?!:;',
        '2': 'абвг',
        '3': 'дежз',
        '4': 'ийкл',
        '5': 'мноп',
        '6': 'рсту',
        '7': 'фхцч',
        '8': 'шщъы',
        '9': 'ьэюя',
        '0': ' '
        }
    result= []
    for element in numbers.split():
        if len(element) > len(legend[element[0]]) or len(set(element)) > 1:
            return None
        result.append(legend[element[0]][len(element) - 1])
    return ''.join(result)

print(numbers_to_text(input()))