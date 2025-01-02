from database.connection import Connection
import uuid

class ProductDatabase():
    def __main__(self):
        pass

    def save_product(self, product):
        try:
            c = Connection()
            my_sql_connection = c.connect_to_mysql()
            cursor = my_sql_connection.cursor()

            cursor.execute("""
            INSERT INTO product (id, product, department, price, idr_price, createdAt) VALUES (%s, %s, %s, %s, %s, %s);
            """, ("{}".format(product['id']), "{}".format(product['product']), "{}".format(product['department']),
                  "{}".format(product['price']), "{}".format(product['idr_price']), "{}".format(product['createdAt'])))

            my_sql_connection.commit()

            cursor.close()
            my_sql_connection.close()
        except:
            raise

    def get_agg_product(self):
        try:
            c = Connection()
            my_sql_connection = c.connect_to_mysql()
            cursor = my_sql_connection.cursor()
            cursor.execute("SELECT product.product, product.department, product.idr_price FROM `product` group by product, department order by idr_price ASC;")
            row = cursor.fetchall()
            cursor.close()
            my_sql_connection.close()
            return row
        except:
            raise