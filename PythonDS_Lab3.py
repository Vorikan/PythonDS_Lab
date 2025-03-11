import numpy as np

# Створення масиву 15x15 з числами від 1 до 225
array = np.arange(1, 226).reshape(15, 15)
print("Масив 15x15:")
print(array)

# Обчислення суми по кожному стовпцю
column_sums = array.sum(axis=0)
print("\nСума по кожному стовпцю:")
print(column_sums)

# Знаходження стандартного відхилення
std_deviation = np.std(array)
print("\nСтандартне відхилення елементів масиву:")
print(std_deviation)

# Транспонування масиву
transposed_array = array.T
print("\nТранспонований масив:")
print(transposed_array)
