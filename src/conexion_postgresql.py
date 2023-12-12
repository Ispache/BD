import psycopg2

conn = psycopg2.connect("dbname=examen1 host=localhost port=5432 user=postgres password=mapache")

cur = conn.cursor()

cur.execute("SELECT * FROM tarea7")

cur.close()
conn.close()
print("conexión exitosa")
       