import sqlite3

def create_db():
    con = sqlite3.connect('db.sqlite')
    cur = con.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        score INTEGER,
        status TEXT,
        name TEXT
    ); 
    '''
    cur.execute(query)
    con.commit()
    con.close()
def insert_data(id, name_user):
    con = sqlite3.connect('db.sqlite')
    cur = con.cursor()

    cur.execute(f'INSERT INTO users (user_id, score, status, name) VALUES ({id}, 0,"user", "{name_user}");')
    con.commit()
    con.close()
def update_data(id, column, data):
    con = sqlite3.connect('db.sqlite')
    cur = con.cursor()
    sql_query = f"UPDATE users SET {column} = ? WHERE user_id = ?;"
    cur.execute(sql_query , (data, id,))
    con.commit()
    con.close()
def select_data(id):
    con = sqlite3.connect('db.sqlite')
    cur = con.cursor()
    data = cur.execute(f'''
    SELECT *
    FROM users
    WHERE user_id = {id}
    ''')
    data = data.fetchall()
    con.commit()
    con.close()
    return data
def datafr():
    con = sqlite3.connect('db.sqlite')
    cur = con.cursor()
    data = cur.execute(f'''
    SELECT *
    FROM users
    ''')
    data = data.fetchall()
    con.commit()
    con.close()
    return data
def user_database(id, name_user):
    data = datafr()
    for i in range(len(data)):
        if data[i][1] == id:
            return True
    insert_data(id,name_user)
    return False
def user(id):
    data = datafr()
    for i in range(len(data)):
        if data[i][1] == id:
            return True
    return False
