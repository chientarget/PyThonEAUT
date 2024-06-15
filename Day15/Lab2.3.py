import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3308,
    user="root",
    password="",
    database="day15python"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES LIKE 'country_new'")
result = mycursor.fetchone()

if not result:
    mycursor.execute("""
    CREATE TABLE country_new (
        COUNTRY_ID INT PRIMARY KEY,
        COUNTRY_NAME VARCHAR(255),
        REGION_ID INT
    )
    """)

    sql = """
    INSERT INTO country_new (COUNTRY_ID, COUNTRY_NAME, REGION_ID)
    VALUES
        (1, 'India', 1001),
        (2, 'USA', 1007),
        (3, 'UK', 1003)
    """
    mycursor.execute(sql)
    mydb.commit()

mycursor.execute("SHOW TABLES LIKE 'countries'")
result = mycursor.fetchone()

if not result:
    mycursor.execute("""
    CREATE TABLE countries (
        country_id INT PRIMARY KEY,
        country_name VARCHAR(255),
        region_id INT
    )
    """)

insert_query = """
INSERT INTO countries (country_id, country_name, region_id)
SELECT country_id, country_name, region_id
FROM country_new;
"""
mycursor.execute(insert_query)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted into countries table.")

# Close the connection
mydb.close()