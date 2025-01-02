from database.connection import Connection
import uuid

class UserDatabase():
    def __main__(self):
        pass

    def save_user(self, nik, role, password):
        try:
            c = Connection()
            my_sql_connection = c.connect_to_mysql()
            cursor = my_sql_connection.cursor()

            _id = self.get_uuid()

            cursor.execute("""
            INSERT INTO user (id, nik, role, password) VALUES (%s, %s, %s, %s);
            """, ("{}".format(_id), "{}".format(nik), "{}".format(role), "{}".format(password)))

            my_sql_connection.commit()

            cursor.close()
            my_sql_connection.close()
        except:
            raise

    def get_user_by_nik(self, nik):
        try:
            c = Connection()
            my_sql_connection = c.connect_to_mysql()
            cursor = my_sql_connection.cursor()

            cursor.execute("SELECT * from user where nik = %s;",("{}".format(nik),))
            row = cursor.fetchone()
            cursor.close()
            my_sql_connection.close()
            return row
        except:
            raise

    def get_uuid(self):
        return uuid.uuid4()