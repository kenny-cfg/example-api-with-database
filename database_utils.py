import mysql.connector
from config import USER, PASSWORD, HOST


def _connect_to_db(db_name):
    # Boilerplate code to connect to a mysql database, uses the auth details
    # in config.py
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
        # Connect to the database
        with _connect_to_db(db_name) as db_connection:
            # Make a cursor (an object with which we can execute a SQL query)
            with db_connection.cursor() as cur:
                print("Connected to DB: %s" % db_name)

                # Construct SQL query
                query = f"""
                insert into user (name, place_of_birth)
                values ('{name}', '{place_of_birth}')
                       """ # TODO: Really really insecure

                # Run SQL query against database
                cur.execute(query)
                # Tell mySQL that you're done
                db_connection.commit()
    except Exception:
        # If anything goes wrong
        raise RuntimeError("Failed to read data from DB")


if __name__ == '__main__':
    # Prove that we can talk to the database
    create_user('Kenny', 'Sunny Birmingham')