import unittest
from appsource.mysql_db_connection import MysqlConnection


class TestMysqlDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.db = MysqlConnection()

    def test_1_create_table(self):
        resp_table = self.db.create_table('venkat6', "vaillage varchar (50),pass_year int,qualification varchar (20),"
                                                     "stream varchar(20)")
        expected = True
        self.assertEqual(expected, resp_table, "failed to create Table")

    def test_2_delete_table(self):
        resp_table = self.db.delete_table("venkat5")
        expected = True
        actual = resp_table
        self.assertEqual(expected, actual, "failed to delete Table")

    def test_3_insert_record(self):
        resp_table = self.db.insert_record('venkat4', "'ramakrishnapuram1',2022,'B.tech','Civil'")
        expected = True
        actual = resp_table
        self.assertEqual(expected, actual, "failed to insert Table")

    def test_4_delete_record(self):
        resp_table = self.db.delete_record("venkat4", "pass_year", "2022")
        expected = True
        actual = resp_table
        self.assertEqual(expected, actual, "failed to delete Table")


if __name__ == "__main__":
    unittest.main()
