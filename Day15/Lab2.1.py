import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3308,
    user="root",
    password="",
    database="day15python"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW CREATE TABLE countries")
for row in mycursor:
    print(row)

sql = "INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)"
val = ("US", "Italy", 1)  # Change 'United States' to 'Italy'

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.close()
mydb.close()
