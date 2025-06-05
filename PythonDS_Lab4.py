import pandas as pd
import mysql.connector

# Завантаження CSV
df = pd.read_csv("titanic.csv", encoding="utf-8")

# Підключення до MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb",
    port=3306
)
cursor = conn.cursor()

# Створити таблицю
cursor.execute("""
CREATE TABLE IF NOT EXISTS titanic (
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

# Завантажити дані
for _, row in df.iterrows():
   cursor.execute("""
    INSERT INTO titanic (
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

# Зчитування даних з таблиці
import sqlalchemy
engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:root@localhost:3306/mydb")
df_from_mysql = pd.read_sql("SELECT * FROM titanic", con=engine)

# Закриття курсора і підключення
cursor.close()
conn.close()

# Виведення перших 5 рядків
print(df_from_mysql.head())
