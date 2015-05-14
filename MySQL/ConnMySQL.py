__author__ = 'Yue'


import MySQLdb

conn=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="tong")

cursor=conn.cursor()

sql="select * from massagist limit 10"

cursor.execute(sql)

results=cursor.fetchall()

print results

conn.close()