import mysql.connector

def access_data():
    try:
        # Establishing a connection to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='summaraize',
            user='root',
            password='Suhas@2324'
        )

        if connection.is_connected():
            print('Connected to MySQL database')

        # Creating a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example query: Selecting data from a table
        query = "desc interests"
        cursor.execute(query)

        # Fetching and printing all rows from the result set
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except mysql.connector.Error as e:
        print(f'Error accessing MySQL database: {e}')

    finally:
        # Closing cursor and connection when done
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print('Connection closed.')

def add_interest(email, interest):
    # Implement database query to insert email and interest into the database
    # Example for MySQL:
    # cursor.execute("INSERT INTO interests (useremailid, interests) VALUES (%s, %s)", (email, interest))
    # connection.commit()
    pass  # Placeholder, replace with actual database query

if __name__ == "__main__":
    access_data()
