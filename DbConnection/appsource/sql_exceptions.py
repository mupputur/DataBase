class ConnectExceptions:
    def __str__(self):
        return "Failed connect to create connection to database"


class CreateTableException:
    def __str__(self):
        return "Failed to create table in database"


class DeleteTableException:
    def __str__(self):
        return "Failed connect to delete table in database"


class InsertRecordException:
    def __str__(self):
        return "Failed to insert record in database"


class DeleteRecordException:
    def __str__(self):
        return "Failed to delete record in database"


class FetchRecordsException:
    def __str__(self):
        return "Failed to Fetch records from database"


class FetchRecordException:
    def __str__(self):
        return "Failed to Fetch record from database"
