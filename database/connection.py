import mysql.connector


class Connection():

    def connect_to_mysql(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',  # Replace with your MySQL host
                user='root',  # Replace with your MySQL username
                password='',  # Replace with your MySQL password
                database='rec_jds'  # Replace with your database name
            )
            if connection.is_connected():
               return connection
            else:
                print("Error while connecting to MySQL")
                return 0
        except:
            print("Error while connecting to MySQL")
            return 0

c = Connection()
c.connect_to_mysql()