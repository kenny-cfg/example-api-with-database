import mysql.connector
from config import USER, PASSWORD, HOST


db_name = 'people'


def _connect_to_db():
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
        # Connect to the database
        with _connect_to_db() as db_connection:
            # Instantiate a cursor object (so that I can run a query against the database)
            with db_connection.cursor() as cur:
                print("Connected to DB: %s" % db_name)
                # Construct SQL
                query = "select id, name, place_of_birth from user"
                # Execute the SQL
                cur.execute(query)
                # Get the results of the SQL
                result = cur.fetchall()
                users = []
                for item in result:
                    db_id = item[0]
                    name = item[1]
                    place_of_birth = item[2]
                    users.append({
                        "id": db_id,
                        "name": name,
                        "placeOfBirth": place_of_birth
                    })
                return users
    except Exception:
        raise RuntimeError("Failed to read data from DB")


def create_user(name, place_of_birth):
    try:
        # Connect to the database
        with _connect_to_db() as db_connection:
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
    users_returned = get_all_users()
    print(users_returned)
