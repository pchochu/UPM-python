import psycopg2
import json

class DB(object):
    def __init__(self):
        self.conn = psycopg2.connect(host="172.17.0.2", database="matching", user="root", password="docker")

    def __del__(self):
        self.conn.close()

    def query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            self.conn.commit()
            return cursor.fetchall()

    def dropTable(self, table):
        with self.conn.cursor() as cursor:
            cursor.execute('DROP TABLE {}'.format(table))
            self.conn.commit()

    def getCellphones(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM cellphones')
            self.conn.commit()
            return cursor.fetchall()
    
    def getAttributes(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM attributes')
            self.conn.commit()
            return cursor.fetchall()
    
    def createDatabase(self, name):
        self.createTables()
        self.impCellphonesIntoDB(name)
        self.impAttributesIntoDB()

    def createTables(self):
        with self.conn.cursor() as cursor:
            sql = """DROP TABLE cellphones;
                    DROP TABLE attributes;

                    CREATE TABLE cellphones(
                    cellphone_id serial PRIMARY KEY,
                    brand VARCHAR (50) NOT NULL,
                    name VARCHAR (100) NOT NULL
                    );
                    
                    CREATE TABLE attributes(
                    attribute_id serial PRIMARY KEY,
                    attribute VARCHAR (10) NOT NULL
                    );
                    """
            cursor.execute(sql)
            self.conn.commit()

    def impCellphonesIntoDB(self, name):
        f = open('/home/peter/projects/matching/data/' + name)
        data = json.load(f)
        for d in data:
                with self.conn.cursor() as cursor:
                    sql = """INSERT INTO cellphones(brand, name) VALUES(%s, %s);"""
                    data = (d['brand'], d['name'])
                    cursor.execute(sql, data)
                    self.conn.commit()

    def impAttributesIntoDB(self):        
        f = open('/home/peter/projects/matching/data/smartphone_attributes.txt', 'r')
        attributes = f.readline().split(';')
        for a in attributes:
            with self.conn.cursor() as cursor:
                sql = "INSERT INTO attributes(attribute) VALUES('{}');".format(a)
                cursor.execute(sql)
                self.conn.commit()

