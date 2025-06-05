import pandas as pd

# 1. Створення DataFrame з даних клієнтів та замовлень
customers_df = pd.read_csv('customer_data.csv')
orders_df = pd.read_csv('order_data.csv')

# 2. Злиття DataFrame за Customer_ID
merged_df = pd.merge(customers_df, orders_df, on='Customer_ID')

# 3. Фільтрація клієнтів віком >30 з замовленнями >100
filtered_df = merged_df[(merged_df['Age'] > 30) & (merged_df['Order_Amount'] > 100)]

# 4. Обчислення загальної суми замовлень для відфільтрованих клієнтів
total_orders = filtered_df.groupby(['Customer_ID', 'Name', 'Age'])['Order_Amount'].sum().reset_index()
total_orders.columns = ['ID Клієнта', 'Ім\'я', 'Вік', 'Загальна сума замовлень']

# Виведення результатів
print("Клієнти віком >30 років з замовленнями >100:")
print(filtered_df[['Customer_ID', 'Name', 'Age', 'Order_Amount']].to_string(index=False))

print("\nЗагальна сума замовлень для цих клієнтів:")
print(total_orders.sort_values('Загальна сума замовлень', ascending=False).to_string(index=False))

# Додатковий аналіз
print(f"\nКількість унікальних клієнтів, які відповідають критеріям: {total_orders.shape[0]}")
print(f"Загальний обсяг продажів для цих клієнтів: {total_orders['Загальна сума замовлень'].sum():.2f}")