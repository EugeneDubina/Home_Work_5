def numbers_count(n, even=0, odd=0):
    if n == 0:
        print(f'В данном числе четных цифр: {even}, нечетных цифр: {odd}')

    else:
        num = n % 10
        n = n // 10
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        return numbers_count(n, even, odd)


n = int(input("Введите натуральное число: "))
numbers_count(n)