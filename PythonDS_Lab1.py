import numpy as np

# Створення двовимірного масиву 3x3 з випадкових цілих чисел від 1 до 100
array = np.random.randint(1, 101, size=(3, 3))
print("Початковий масив:")
print(array)

# Обчислення суми всіх елементів масиву
total_sum = np.sum(array)
print(f"\nСума всіх елементів масиву: {total_sum}")

# Знаходження максимального та мінімального значення в масиві, а також їхніх індексів
max_value = np.max(array)
min_value = np.min(array)
max_index = tuple(map(int, np.unravel_index(np.argmax(array), array.shape)))  
min_index = tuple(map(int, np.unravel_index(np.argmin(array), array.shape)))  
print(f"\nМаксимальне значення: {max_value} (індекс: {max_index})")
print(f"Мінімальне значення: {min_value} (індекс: {min_index})")

# Сортування масиву по кожному рядку
sorted_array = np.sort(array, axis=1)
print("\nВідсортований масив по кожному рядку:")
print(sorted_array)
