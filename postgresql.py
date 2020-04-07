import psycopg2
con = psycopg2.connect(host='localhost', database='postgres',
user='postgres', password='123456')
cur = con.cursor()
cur.execute('select * from empresa')
recset = cur.fetchall()
for rec in recset:
    print (rec)
con.close()