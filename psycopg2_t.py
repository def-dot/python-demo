import psycopg2

# Define your connection parameters
db_params = {
    'dbname': 'toutiao',
    'user': 'postgres',
    'password': 'sj1107',
    'host': '156.232.13.203',
    'port': '65432'
}

# Establish the connection
try:
    conn = psycopg2.connect(**db_params)
    print("Connection successful")
except Exception as e:
    print(f"An error occurred: {e}")

# Use the connection to create a cursor and interact with the database
try:
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT version();")

    # Fetch and print the result of the query
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    # Always close the cursor and connection when done
    cursor.close()
    conn.close()
except Exception as e:
    print(f"An error occurred: {e}")
