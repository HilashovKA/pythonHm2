from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Номер элемента: ', get_numbers(numbers))

x = int(input('Введите первую позицию: '))
y = int(input('Введите вторую позицию: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Общий элемент: {numbers[x -1]} * {numbers[y -1]} =', mult)