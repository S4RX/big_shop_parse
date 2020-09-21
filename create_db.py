import sqlite3
from sqlite3 import Error
#from full_silpo_shop_adress import full_silpo_shop_adress as fssa





def create_new_db(path_to_db):
    """ create a database connection to a SQLite database """
    #path_to_db = r"D:\project price\db\\" + str(db_file) + ".db"
    #create_connection(r"D:\project price\db\\" + db_file + ".db")
    #for adress in path_to_db:

    conn = None
    try:
        conn = sqlite3.connect(path_to_db)
        print(sqlite3.version)
    except Error as e:
        print(path_to_db)
    finally:
        if conn:
            conn.close()

def main():
    
    path_to_db = r"db\\Stock db.db"
    create_new_db(path_to_db)


if __name__ == '__main__':
    main()