import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Tifanny Kate\PycharmProjects\pythonProject\5.17.22 Database\Database2.accdb')
    print("Connected to a Database")

except pyodbc.Error as e:
    print("Error in Connection")