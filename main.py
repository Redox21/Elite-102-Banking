import mysql.connector
import functions as fun

# Database Connection
# Make Sure to update database, otherwise you can't reestablish a connection.
mydb = mysql.connector.connect(user="root", database="empolyes", password="0148Uapm@*Ss")
mycursor = mydb.cursor()


# Query to fetch all rows from 'accounts' table
query = "SELECT * FROM accounts"
# Executing the query
mycursor.execute(query)


# Fetching all rows and printing them
for item in mycursor.fetchall():
    print(item)

def main():
    # Call the menu function
    fun.menu()  

if __name__ == "__main__":
    main()

# Closing cursor and connection
mycursor.close()
mydb.close()

# id, useraccount, accountnumber, accountpin, netbalance, acounttype

# userAccountInput = input("Enter a valid username: ")

# def checkAccount():
#     if userAccountInput == empolyes