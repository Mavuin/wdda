# Using the required modul "sqlite3" to run the sql queries
import sqlite3

# creating a connection to the database "wdda_teil_A_database.db"
connection = sqlite3.connect("wdda_teil_A_database.db")
cur = connection.cursor()


# Class creation for the below methods
class SqlQueries:

    # This method executes an SQL statement that counts all the firms with a total funding according to the input
    def query_funding_count(self):
        print("\nTask 2 from SQL Exercises")
        amount = int(input("Enter a valid funding amount: "))
        cur.execute("SELECT count (*) FROM wdda_view WHERE totalfunding > ?", (amount,))
        number_of_companies = cur.fetchone()[0]
        print("Number of companies according to the given input:", number_of_companies)

    # This method runs a SQL statement that counts all the unique regions in the DB
    def query_unique_regions(self):
        print("\nTask 6 from SQL Exercises")
        cur.execute("SELECT count(DISTINCT region) as regions FROM region")
        regions = cur.fetchone()[0]
        print("The number of unique regions in the DB:", regions)


def main():

    call = SqlQueries()
    call.query_funding_count()
    call.query_unique_regions()


if __name__ == "__main__":
    main()
