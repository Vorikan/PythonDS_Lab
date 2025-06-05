import pandas as pd

# Завантаження даних
df = pd.read_csv('extended_sales_data.csv')

# Виведення даних
print("Перші 5 рядків:")
print(df.head())
print("\nОстанні 5 рядків:")
print(df.tail())

# Видалення пропущених значень та дублікатів
print("\nКількість рядків до очищення:", len(df))
print("Кількість дублікатів перед видаленням:", df.duplicated().sum())
df_cleaned = df.dropna().drop_duplicates()
print("Кількість рядків після очищення:", len(df_cleaned))

# Заміна пропущених значень на середнє
mean_amount = round(df['Purchase_Amount'].mean(), 2)
print("\nСереднє значення Purchase_Amount:", mean_amount)
df_filled = df.copy()
df_filled['Purchase_Amount'] = df_filled['Purchase_Amount'].fillna(mean_amount)
print("\nПерші 5 рядків після заміни пропущених значень:")
print(df_filled.head())

# Збереження результатів
df_cleaned.to_csv('cleaned_sales_data.csv', index=False)
df_filled.to_csv('filled_sales_data.csv', index=False)