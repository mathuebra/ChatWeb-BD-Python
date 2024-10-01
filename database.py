import sqlite3 as sql
from .database import database_functions

class Database():
    def __init__(self, database_path):
        self.database = database_path
        self.conn = None
        self.cursor = None
        self.connected = False

    def connect(self):
        self.conn = sql.connect(self.database)
        self.cursor = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        self.conn.close()
        self.connected = False

    def execute(self, sql, parms=None):
        if self.connected:
            if parms is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, parms)
            return True
        else:
            return False
        
    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False
        
    def fetchall(self):
        return self.cursor.fetchall()

    def insert(self, table, columns, values):
        placeholders = ', '.join(['?'] * len(values))
        columns_str = ', '.join(columns)
        sqlquery = f'''INSERT INTO {table} ({columns_str}) VALUES ({placeholders})'''

        self.connect()
        self.execute(sqlquery, values)
        self.persist()
        self.disconnect()

    def update(self, table, columns, values, condition=None):
        placeholders = ', '.join([f"{col} = ?" for col in columns])
        
        if condition is None:
            sqlquery = f"UPDATE {table} SET {placeholders}"
        else:
            sqlquery = f"UPDATE {table} SET {placeholders} WHERE {condition}"
        
        self.connect()
        self.execute(sqlquery, values)
        self.persist()
        self.disconnect()

    def delete(self, table, condition):
        sqlquery = f"DELETE FROM {table} WHERE {condition}"

        self.connect()
        self.execute(sqlquery)
        self.persist()
        self.disconnect()

    def select(self, table, columns, condition, params=()):
        columns = ", ".join(columns)
        sqlquery = f"SELECT {columns} FROM {table} WHERE {condition}"
        
        self.connect()
        self.execute(sqlquery, params)
        result = self.fetchall()
        self.disconnect()

        return result
    
    def verify_login(self, email, password):
        result = self.select('USUARIO', ['ID_USER'], f"EMAIL = ? AND SENHA = ?", [email, password])
        return result[0] # Retorna elemento ao invés de tupla