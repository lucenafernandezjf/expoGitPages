import MySQLdb
conn= MySQLdb.connect ("127.0.0.1",user,pass,"80")
cursor=conn.cursor()
q=cursor.execute("Select * from superheroes order by ...")
filas = q.fetchall()
if filas it not None:
	for fila in filas:
