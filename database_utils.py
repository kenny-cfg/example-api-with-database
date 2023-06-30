import mysql.connector
from config import USER, PASSWORD, HOST, PORT

db_name = 'people'


def _connect_to_db():
    # Boilerplate code to connect to a mysql database, uses the auth details
    # in config.py
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=db_name,
            port=PORT
        )
        return cnx
    except DbConnectionError as err:
        print("A problem creating a connection:", err)

class DbConnectionError(Exception):
    pass

def get_single_user(id_of_user):
    try:
        # Connect to the database
        with _connect_to_db() as db_connection:
            # Instantiate a cursor object (so that I can run a query against the database)
            with db_connection.cursor() as cur:
                print("Connected to DB: %s" % db_name)
                # Construct SQL
                query = f"select id, name, place_of_birth from user where id = {id_of_user}"  # INSECURE -- SQL injection
                # Execute the SQL
                cur.execute(query)
                # Get the results of the SQL
                result = cur.fetchall()
                for item in result:
                    db_id = item[0]
                    name = item[1]
                    place_of_birth = item[2]
                    return {
                        "id": db_id,
                        "name": name,
                        "placeOfBirth": place_of_birth
                    }
    except Exception:
        raise RuntimeError("Failed to read data from DB")



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
    user_returned = get_single_user(1)
    print(user_returned)
