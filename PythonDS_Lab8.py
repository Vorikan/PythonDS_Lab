import pandas as pd
from sqlalchemy import create_engine

# Параметри з'єднання
user = "root"
password = "root"
host = "localhost"
port = "3306"
database = "mydb"

# Створення SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")

# Завантаження даних у DataFrame
query = "SELECT * FROM titanic"
df = pd.read_sql(query, con=engine)


df_numeric = df[['Age', 'Fare', 'Pclass', 'SibSp', 'Parch', 'Survived']]
df_clean = df_numeric.dropna()
correlation = df_clean.corr(method='pearson') 

# Вивід кореляції з 'Survived'
print("Кореляція з 'Survived':")
print(correlation['Survived'].sort_values(ascending=False))
