"""
4. Валидность скобок
Дана строка X, состоящая только из символов “{“, “}”, “[“, “]”, “(“, “)”. Программа должна вывести True, в том случае если все открытые скобки закрыты. Например: “[()]{}”, все открытые скобки закрыты закрывающимися скобками, потому вывод будет True. В случае же, если строка будет похожа на: “{{{}”, то вывод будет False, т.к. не все открытые скобки закрыты.

Пример 1:
Ввод: x = “[{}({})]”
Вывод: True

Пример 2:
Ввод: x = “{]”
Вывод: False

Пример 3:
Ввод: x = “{“
Вывод: False

Гарантируется, что введенная строка X будет содержать только скобки и не будет пустой.
"""

def pair_staples(x1, x2):
    """Определяет, являются ли скобки парой"""
    if x1+x2 == '()' or x1+x2 == '[]' or x1+x2 == '{}':
        return True
    else:
        return False


def valid_staples(x):
    if len(x) % 2 != 0:
        return False

    valid = True
    while x and valid:
        valid = False
        for n in range(len(x) - 1):
            if pair_staples(x[n], x[n+1]):
                x = x[:n] + x[n+2:]
                valid = True
                break
    
    if x:
        return False
    else:
        return True


print(valid_staples('[{}({})]'))
print(valid_staples('({[}])'))
print(valid_staples('()[]'))
print(valid_staples('{(}'))
