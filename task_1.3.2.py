"""
2. Палиндром строки
Дана строка X, возвращайте True, если X является палиндромом.
Строка является палиндромом тогда, когда она читается одинаково как в обратном, так и в прямом направлении.
Например, является “taco cat” является палиндромом, в то время как “black cat” не является.
В данной задаче пробелы не учитываются.
Гарантируется, что исходная строка может содержать символы только нижнего регистра.
"""
x = input()
xx = ''.join(x.split())

def palindrom(x):
    if x == x[::-1]:
        return True
    else:
        return False

print(palindrom(xx))
