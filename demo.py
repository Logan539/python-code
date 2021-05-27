import psycopg2
"""conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5432")   #for connecting to database in psql

cur = conn.cursor()
#cur.execute('''create table student(Roll_no int, Name text, Address text, Age int, Phone_no bigint)''')
#cur.execute('''insert into student values(1, 'Girish', 'Pune', 23, 8380898482)''')
#cur.execute('''insert into student values(2, 'Jhon', 'Pune', 22, 123456789)''')
#cur.execute('''insert into student values(3, 'Pratiksha', 'Mumbai', 23, 9874656789)''')
#print("tabel created!!")
conn.commit()  #to commint changes
conn.close()   #to close the connection

print("Connection success!!")"""

def getdata():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5432")   #for connecting to database in psql
    cur = conn.cursor()
    Roll_no = input("Enter Roll Number: ")
    Name = input("Enter Name:")
    Address = input("Enter Address: ")
    Age = input("Enter Age: ")
    Phone_no = input("Enter Phone number: ")
    query = '''insert into student values(%s, %s, %s, %s, %s);'''   #%s represent the place where content will get replaced
    cur.execute(query,(Roll_no, Name, Address, Age, Phone_no))
    conn.commit()
    conn.close()

getdata()