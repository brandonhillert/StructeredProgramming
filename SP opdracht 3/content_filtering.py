import psycopg2

"""
Opdracht: SP opdracht 3.Business rules voor Recommendation Engine 
Author: Brandon Hillert
This is based on items liked by the customer and keywords used to describe the items. 
It also takes into consideration the preferences chosen by the customer
"""

conn = psycopg2.connect("dbname=sp_opdracht_3 user=postgres password=admin")
cur = conn.cursor()


def create_table():
    cur.execute("DROP TABLE IF EXISTS content_algoritme;")
    cur.execute('CREATE TABLE content_algoritme ('
                'id varchar PRIMARY KEY,'
                'product1 varchar,'
                'product2 varchar,'
                'product3 varchar,'
                'product4 varchar,'
                'product5 varchar);')
    conn.commit()


def type_algoritme(product, type):
    # Query die alle ids ophaalt waar die id != product en category_idcatergory = categorie
    cur.execute("SELECT id FROM products"
                " WHERE type = '{}' AND id != '{}'".format(type, product)
                )
    lijst = cur.fetchall()

    # Stopt alle id's in een lijst, en haalt daar 5 willekeurige waardes uit
    lijst_producten = []
    for i in lijst:
        list(i)
        lijst_producten.append(i[0])

    if len(lijst_producten) < 5:
        return [product, product, product, product, product, product]
    else:
        prod1 = lijst_producten[0]
        prod2 = lijst_producten[1]
        prod3 = lijst_producten[2]
        prod4 = lijst_producten[3]
        prod5 = lijst_producten[4]

        return [product, prod1, prod2, prod3, prod4, prod5]


def fill_table():
    cur.execute('SELECT id, type FROM products')
    lijst_producten = cur.fetchall()

    count = 0

    for ids in lijst_producten:
        product = list(ids)

        if product[0] == "38647-It'sglowtime":
            product[0] = "38647-It''sglowtime"

        if product[1] == "Auto's":
            product[1] = "Autos"

        lijst_prods = type_algoritme(product[0], product[1])

        try:
            cur.execute("INSERT INTO content_algoritme(id, product1, product2, product3, product4, product5)"
                        "VALUES ('{}','{}','{}','{}','{}','{}')".format(lijst_prods[0], lijst_prods[1], lijst_prods[2],
                                                                        lijst_prods[3], lijst_prods[4], lijst_prods[5]))
        except:
            print(product[0], product[1])
        conn.commit()

        count += 1
        if count % 1000 == 0:
            print(count, "/34000 producten zijn ingeladen")

    print("Producten zijn ingeladen")


def main_loop_content_filtering():
    create_table()
    print("Tabel is aangemaakt")
    print("Producten worden ingeladen...")
    fill_table()
    print("Einde algoritme")
    cur.close()


main_loop_content_filtering()
