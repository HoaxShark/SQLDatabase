import sqlite3


class Database:

    def __init__(self):
        self.isRunning = True
        # create or open a file called my_db
        self.db = sqlite3.connect('my_db')
        # get cursor object
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT,
                        email TEXT unique, password TEXT)
                        ''')
        # commit the change
        self.db.commit()
        print('Table created')

    def add_user(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        # Insert user
        self.cursor.execute('''INSERT INTO users(name, phone, email, password)
                          VALUES(?,?,?,?)''', (name, phone, email, password))
        self.db.commit()
        print('User inserted')

    def select_one(self):
        self.cursor.execute('''SELECT name, email, phone FROM users''')
        user1 = self.cursor.fetchone()  # retrieve the first row
        print(user1[0])  # Print the first column retrieved(user's name)

    def select_all(self):
        self.cursor.execute('''SELECT name, email, phone FROM users''')
        all_rows = self.cursor.fetchall()
        for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns email column.
            print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

    def select_name(self):
        username = input("Enter username to search: \n")
        self.cursor.execute('''SELECT name, email, phone, password FROM users WHERE name=?''', (username,))
        user1 = self.cursor.fetchone()  # retrieve the first row
        print('Name: ' + user1[0] + '\nPhone: ' + user1[1] + '\nEmail: ' + user1[2] +
              '\nPassword: ' + user1[3])  # Print the first column retrieved(user's name)

    def update_all(self):
        old_name = input("Enter current name: ")
        name = input("Enter new name: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        password = input("Enter new password: ")
        # Insert user
        self.cursor.execute('''UPDATE users SET name = ?, phone = ?, email = ?, password =? WHERE name = ? ''', (name, phone, email, password, old_name))
        self.db.commit()
        print('User updated')

    def main_loop(self):
        while self.isRunning:
            print(" 1: create \n 2: add \n 3: select one \n 4: select all \n 5: select by name \n 6: update all \n x: quit")
            input_command = input("What would you like to do?\n")

            if input_command == '1':
                self.create_table()

            if input_command == '2':
                self.add_user()

            if input_command == '3':
                self.select_one()

            if input_command == '4':
                self.select_all()

            if input_command == '5':
                self.select_name()

            if input_command == '6':
                self.update_all()

            if input_command == 'drop':
                self.cursor.execute('''DROP TABLE users''')

            if input_command == 'x':
                self.db.close
                self.isRunning = False


if __name__ == '__main__':
    database = Database()
    database.main_loop()
