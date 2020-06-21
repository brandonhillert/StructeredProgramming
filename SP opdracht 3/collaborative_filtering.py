import psycopg2

"""
Opdracht: SP opdracht 3.Business rules voor Recommendation Engine 
Author: Brandon Hillert
This is based on customer’s behaviors, activities
or preferences and predicting what customers will like 
based on their similarity to others
"""

conn = psycopg2.connect("dbname=sp_opdracht_3 user=postgres password=admin")
cur = conn.cursor()


def create_table():
    cur.execute("DROP TABLE IF EXISTS collaborative_filtering;")
    cur.execute('CREATE TABLE collaborative_filtering ('
                'last_viewed_product varchar PRIMARY KEY,'
                'new_product varchar);')
    conn.commit()


create_table()
