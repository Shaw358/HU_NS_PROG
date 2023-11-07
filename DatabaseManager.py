# This file is repsonsible for letting the other scripts use the database without clogging themselves
import psycopg2
import DatabaseManager # FIXME: This returns a warning but this works for now

cur = None

DbConnectionInfo = psycopg2.connect(
    dbname="db1",
    user="CMDR_Garbage@nszuildatabase",
    password="Destroyer358",
    host="nszuildatabase.postgres.database.azure.com",
    port="5432"
)


# ["DateTime", "User", "Message", "Station", "ModerationResult", "ModerationDate", "ModerationTime", "ModeratorName", "ModeratorEmail"]
def ConnectToDB():
    DatabaseManager.cur = DbConnectionInfo.cursor()


def ExecuteSQL_Query(query, parameters=None, returnVal=True):
    if parameters is None or parameters is False:
        DatabaseManager.cur.execute(query)
    else:
        DatabaseManager.cur.execute(query, parameters)

    Commit()

    result = None
    if returnVal:
        result = DatabaseManager.cur.fetchall()

    if result is not None and returnVal:
        return result
    else:
        print("No rows found or desired.")


def CloseConnection():
    DatabaseManager.cur.close()
    DatabaseManager.DbConnectionInfo.close()


def Commit():
    DbConnectionInfo.commit()
