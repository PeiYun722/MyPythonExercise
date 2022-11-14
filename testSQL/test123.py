import pymysql

db=pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='class', charset='utf8')
    
with db.cursor() as cursor:
    sql = 'SELECT * from class.a1'
    
    cursor.execute(sql)

    data = cursor.fetchall()
    for i in data:
        print (i)
#關閉連線
db.close()