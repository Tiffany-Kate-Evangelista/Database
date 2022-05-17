import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Tifanny Kate\PycharmProjects\pythonProject\5.17.22 Database\Database2.accdb')
    print("Connected to a Database")

    record = connect.cursor()
    record.execute('select * from Table1')
    for row in record.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Error in Connection")