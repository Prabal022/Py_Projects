import sqlite3

conn = sqlite3.connect('dict_dbase.db')

#creat Cursor
cu = conn.cursor()

#Create Table for first time use

#cu.execute("CREATE TABLE data_dict (word text, defination text)")

#cu.execute ("INSERT INTO data_dict VALUES ('Temp','sample')")

cu.execute ("SELECT * FROM data_dict")

print(cu.fetchall())

conn.commit()

conn.close()