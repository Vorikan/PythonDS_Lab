import pandas as pd

# 1. Завантаження даних
df = pd.read_csv('transaction_analysis_data.csv')

# 2. Обчислення середнього доходу для кожного міста
city_avg = df.groupby('City')['Transaction_Amount'].mean().reset_index()
city_avg.columns = ['Місто', 'Середній дохід']
print("\nСередній дохід по містах:")
print(city_avg.to_string(index=False))

# 3. Місто з найвищим і найнижчим доходом
max_city = city_avg.loc[city_avg['Середній дохід'].idxmax()]
min_city = city_avg.loc[city_avg['Середній дохід'].idxmin()]
print(f"\nМісто з найвищим доходом: {max_city['Місто']} ({max_city['Середній дохід']:.2f})")
print(f"Місто з найнижчим доходом: {min_city['Місто']} ({min_city['Середній дохід']:.2f})")

# 4. Кількість транзакцій за місяць
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
monthly_counts = df.groupby(df['Transaction_Date'].dt.to_period('M'))['Transaction_ID'].count().reset_index()
monthly_counts.columns = ['Місяць', 'Кількість транзакцій']
print("\nКількість транзакцій за місяць:")
print(monthly_counts.to_string(index=False))