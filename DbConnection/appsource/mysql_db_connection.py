import mysql.connector
import pickle


class MysqlConnection:

    def __init__(self, hostname='localhost', username='root', password=None, database_name='class_db'):
        if password is None:
            f = open(r'C:\Users\vejen\PycharmProjects\DbConnection\appsource\password.pkl', 'rb')
            password = pickle.load(f)
            f.close()
        self.cur = None
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database_name = database_name
        self._connect()

    def is_connection_exist(self):
        pass

    def _connect(self):
        password = self.password
        try:
            if not self.is_connection_exist():
                self.con = mysql.connector.connect(host=self.hostname, user=self.username, password=password,
                                                   database=self.database_name)
                self.cur = self.con.cursor()
                print("connected")
                return True
        except Exception as e:
            raise Exception("Exception arise " + str(e))

    def create_table(self, table_name, *table_fields):
        """
        Ex:CREATE table<table name>("'column1','column2',....")
        :param table_name:
        :param table_values:
        :return:
        """
        x = ""
        for i in table_fields:
            x = x + i + ","
            y = x[:-1]
            try:
                query = "create table " + table_name + "(" + y + ")"
                self.cur.execute(query)
                self.con.commit()
                print("Table created check in database")
                return True
            except Exception as e:
                return e

    def delete_table(self, table_name):
        """
        EX: DROP TABLE <table name>
        :param table_name:
        :return:
        """
        try:
            query = "DROP TABLE " + table_name
            self.cur.execute(query)
            self.con.commit()
            print("Table deleted check in database")
            return True
        except:
            raise Exception("Table not available in ", table_name)

    def insert_record(self, table_name, *table_values):
        """
        EX: INSERT INTO <table name> VALUES ("'column1','column2',....")
        :param table_name:
        :param table_values:
        :return:
        """
        x = ""
        for i in table_values:
            x = x + i + ","
            y = x[:-1]
            try:
                query = "INSERT INTO " + table_name + " VALUES" + "(" + y + ")"
                self.cur.execute(query)
                self.con.commit()
                print("Record created")
                return True
            except Exception as e:
                raise Exception(e)

    def delete_record(self, table_name, stream, stream_value):
        """
        EX: DELETE FROM <table name> WHERE <stream> = <stream_value>
        :param table_name:
        :param stream:
        :param stream_value:
        :return:
        """
        try:
            query = "DELETE FROM {} WHERE {} = '{}'".format(table_name, stream, stream_value)
            self.cur.execute(query)
            self.con.commit()
            print("record deleted check in database")
            return True
        except:
            raise Exception ("No such record in:", table_name)

    def fetch_all_records(self, query):
        """
        EX: SELECT * FROM ("table name")
        :param query:
        :return:
        """
        try:
            self.cur.execute(query)
            data = self.cur.fetchall()
            for values in data:
                print(values)
            return True
        except:
            raise Exception("No records to fetch")

    def fetch_one_record(self, query):
        """
        EX: SELECT * FROM ("table name")
        :param query:
        :return:
        """
        try:
            self.cur.execute(query)
            data = self.cur.fetchone()
            for values in data:
                print(values)
        except:
            raise Exception("No records to fetch")

    def fetch_many_records(self, query, number_of_records):
        """
        EX: SELECT * FROM ("table name", number of records)
        :param query:
        :param number_of_records:
        :return:
        """
        try:
            self.cur.execute(query)
            data = self.cur.fetchmany(number_of_records)
            for values in data:
                print(values)
        except:
            raise Exception("No records to fetch")


if __name__ == "__main__":
    obj = MysqlConnection()
    # tbl_inp = "vaillage varchar (50),pass_year int,qualification varchar (20),stream varchar(20)"
    # obj.create_table('venkat4', tbl_inp)
    rcrd_inp = "'ramakrishnapuram1','2040','B.tech','civil'"
    obj.insert_record('venkat4', rcrd_inp)
    # obj.fetch_many_records("select * from venkat4", 2)
    # obj.delete_record("venkat4", "pass_year", "2021")
    # obj.delete_table("venkat10")
    #obj.is_record_exist()
    #print(x)
