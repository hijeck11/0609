
import psycopg2

conn = psycopg2.connect(
    dbname="students",
    user="anton",
    password="password",
    host="127.0.0.1",
    port="5432"
)
print('connect')

cur_1 = conn.cursor()
cur_1.execute("SELECT * FROM univer")
cur_2 = conn.cursor()
cur_2.execute("SELECT * FROM classrooms")
results_1 = cur_1.fetchall()
results_2 = cur_2.fetchall()
conn.commit()
cur_1.close()
cur_2.close()
conn.close()
for row_1 in results_1:
    print(row_1)
for row_2 in results_2:
    print(row_2)
