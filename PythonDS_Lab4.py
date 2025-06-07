import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
import yaml

# Зчитування конфігурації
with open("config_load.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

db = config['mysql']
csv_path = config['csv_file']
table_name = config['table']

# Завантаження CSV
df = pd.read_csv(csv_path, encoding="utf-8")

# Підключення до MySQL
conn = mysql.connector.connect(
    host=db['host'],
    user=db['user'],
    password=db['password'],
    database=db['database'],
    port=db['port']
)
cursor = conn.cursor()

# Створення таблиці
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    PassengerId INT,
    Survived TINYINT,
    Pclass INT,
    Name VARCHAR(255),
    Sex VARCHAR(10),
    Age FLOAT,
    SibSp INT,
    Parch INT,
    Ticket VARCHAR(50),
    Fare FLOAT,
    Cabin VARCHAR(50),
    Embarked VARCHAR(10)
)
""")

# Завантаження даних у таблицю
for _, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO {table_name} (
            PassengerId, Survived, Pclass, Name, Sex, Age,
            SibSp, Parch, Ticket, Fare, Cabin, Embarked
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row['PassengerId']),
        int(row['Survived']),
        int(row['Pclass']),
        row['Name'],
        row['Sex'],
        float(row['Age']) if pd.notna(row['Age']) else None,
        int(row['SibSp']),
        int(row['Parch']),
        row['Ticket'],
        float(row['Fare']) if pd.notna(row['Fare']) else None,
        row['Cabin'] if pd.notna(row['Cabin']) else None,
        row['Embarked'] if pd.notna(row['Embarked']) else None
    ))

conn.commit()



engine = create_engine(f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}")
df_from_mysql = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)
cursor.close()
conn.close()

# Вивід
print(df_from_mysql.head())
