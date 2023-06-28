import mysql.connector
from config import USER, PASSWORD, HOST


db_name = 'people'

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


def get_all_users():
    try:
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "select id, name, place_of_birth from user"

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        users = []
        for item in result:
            id = item[0]
            name = item[1]
            place_of_birth = item[2]
            users.append({
                "id": id,
                "name": name,
                "placeOfBirth": place_of_birth
            })
        cur.close()
        print(users)

    except Exception:
        raise RuntimeError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def create_user(name, place_of_birth):
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
                       """  # TODO: Really really insecure - SQL injectable

                # Run SQL query against database
                cur.execute(query)
                # Tell mySQL that you're done
                db_connection.commit()
    except Exception:
        # If anything goes wrong
        raise RuntimeError("Failed to read data from DB")


if __name__ == '__main__':
    # Prove that we can talk to the database
    get_all_users()
