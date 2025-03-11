import numpy as np

# Створення одновимірного масиву з 200 випадкових чисел від -100 до 100
array = np.random.randint(-100, 101, 200)
print("Початковий масив:", array)

# Використання маски для фільтрації всіх додатніх чисел
positive_numbers = array[array > 0]
print("Додатні числа:", positive_numbers)

# Заміна всіх від’ємних значень на нулі
array[array < 0] = 0
print("Масив після заміни від’ємних значень на нулі:", array)

# Обчислення середнього значення отриманого масиву
average_value = np.mean(array)
print("Середнє значення отриманого масиву:", average_value)
