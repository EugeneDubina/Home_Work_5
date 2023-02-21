def sum(i):
    if i == 1:
        return 1
    return sum(i - 1) + (-0.5) ** (i - 1)


n = int(input('Введите количество элементов: '))
print(f'Сумма элементов равна {sum(n)}.')