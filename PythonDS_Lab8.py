import pandas as pd
from sqlalchemy import create_engine
import yaml

# Зчитування конфігурації
with open("config_analyze.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

db = config['mysql']
table_name = config['table']
numeric_cols = config['numeric_columns']
correlation_method = config['correlation_method']

# Підключення до бази
engine = create_engine(f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}")

# Зчитування таблиці
df = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)

# Вибір числових колонок
df_numeric = df[numeric_cols]

# Видалення пропущених
df_clean = df_numeric.dropna()

# Кореляційна матриця
correlation = df_clean.corr(method=correlation_method)

# Вивід
print("Кореляція з 'Survived':")
print(correlation['Survived'].sort_values(ascending=False))
