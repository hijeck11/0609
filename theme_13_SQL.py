#
import psycopg2

conn = psycopg2.connect(
    dbname="homework_13",
    user="anton",
    password="password",
    host="127.0.0.1",
    port="5432"
)
print('connect')

cur_1 = conn.cursor()
# insert_query = "INSERT INTO citys(town, population, country) VALUES (%s, %s, %s)"
# data_to_insert = ('Madrid', 3223000, 'Spanish')
# cur_1.execute(insert_query, data_to_insert)
# insert_query = "INSERT INTO citys(town, population, country) VALUES (%s, %s, %s)"
# data_to_insert = ('Kiev', 2900000, 'Ukraine')
# cur_1.execute(insert_query, data_to_insert)
# cur_1.execute("SELECT * FROM citys")
cur_2 = conn.cursor()
# cur_2.execute("SELECT * FROM citys2")
select_sum_query = "SELECT SUM(population) FROM citys2"
cur_2.execute(select_sum_query)
# results_1 = cur_1.fetchall()
results_2 = cur_2.fetchall()
conn.commit()
# cur_1.close()
cur_2.close()
conn.close()
# for row_1 in results_1:
#     print(row_1)
for row_2 in results_2:
    print(row_2)
#
