number = int(input('Введите число'))
sum = 0
while number != 0:
    last_num = number % 10
    sum = sum + last_num
    number = number // 10
print(sum)
