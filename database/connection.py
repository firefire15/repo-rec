import mysql.connector


class Connection():

    def connect_to_mysql(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='rec_jds'
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