from pymysql import Connection
conn = Connection(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "zhishun.cai",
    database= "spark_sql"
)

print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
# conn.select_db("spark_sql")
# cursor.execute("create table test(id int)")

#
cursor.execute("select * from sys_user")
results:tuple[tuple] = cursor.fetchall()
for ele in results:
    print(ele)
conn.close()