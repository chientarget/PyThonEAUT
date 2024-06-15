import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3308,
    user="root",
    password="",
    database="day15python"
)
mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")


# ex1
# mycursor.execute("""
# CREATE TABLE countries (
#     country_id INT PRIMARY KEY,
#     country_name VARCHAR(255),
#     region_id INT
# )
# """)

#
# # ex2
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS countries (
#     country_id INT PRIMARY KEY,
#     country_name VARCHAR(255),
#     region_id INT
# )
# """)

# #ex3
# mycursor.execute("""
# CREATE TABLE countries (
#     country_id INT PRIMARY KEY,
#     country_name VARCHAR(255) CHECK (country_name IN ('Italy', 'India', 'China')),
#     region_id INT
# )
# """)
#
# # #ex4
# Create the job_history table
mycursor.execute("""
CREATE TABLE job_history (
    employee_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    job_id VARCHAR(10),
    department_id INT,
    PRIMARY KEY (employee_id, start_date),
    FOREIGN KEY (job_id) REFERENCES jobs(JOB_ID)
)
""")



for x in mycursor:
    print(x)