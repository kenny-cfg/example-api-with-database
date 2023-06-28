import mysql.connector
from config import USER, PASSWORD, HOST


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def create_user(name, place_of_birth):
    db_name = 'people'
    try:
        with _connect_to_db(db_name) as db_connection:
            with db_connection.cursor() as cur:
                print("Connected to DB: %s" % db_name)

                query = f"""
                insert into user (name, place_of_birth)
                values ('{name}', '{place_of_birth}')
                       """ # TODO: Really really insecure

                cur.execute(query)
                db_connection.commit()
    except Exception:
        raise RuntimeError("Failed to read data from DB")


if __name__ == '__main__':
    create_user('Kenny', 'Sunny Birmingham')