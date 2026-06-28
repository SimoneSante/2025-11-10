from database.DB_connect import DBConnect

from model.store import Store

from model.order import Order


class DAO():
    @staticmethod
    def getAllStores():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * from stores"

        cursor.execute(query)

        for row in cursor:
            results.append(Store(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_nodi(c):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select o.*, SUM(oi.quantity) as quantity
                    from orders o,  order_items oi
                    where o.store_id =%s and oi.order_id =o.order_id 
                    group by oi.order_id """

        cursor.execute(query, (c,))
        for row in cursor:
            results.append(Order(**row))
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_archi(c,b):
        conn = DBConnect.get_connection()
        c=int(c)
        b=int(b)
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select o.order_id as id1, o1.order_id as id2, datediff(o1.order_date ,o.order_date) as k
                    from orders o, orders o1
                    where o.store_id =%s and o1.store_id=%s  
                    and o.order_id != o1.order_id and o.order_date<o1.order_date 
                    and datediff(o1.order_date ,o.order_date)<=%s"""
        params=(c, c, b)
        cursor.execute(query, params)
        for row in cursor:
            results.append((row["id1"],row["id2"],row["k"]))
        cursor.close()
        conn.close()
        return results