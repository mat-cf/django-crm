import mysql.connector

# prepare DB connection
database = mysql.connector.connect(
  host = '172.23.32.1',
  user = 'root',
  passwd = 'password',
  auth_plugin='mysql_native_password' # this needed because of the new password encription method
)

# create a cursor object
cursor_object = database.cursor()

# create the database
cursor_object.execute('CREATE DATABASE elderco')
print('All done!') 