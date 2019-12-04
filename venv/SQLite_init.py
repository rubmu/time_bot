#Класс для работы с базой данных SQLite

import sqlite3

class SQL:
    def __init__(self, name):
        self.dbname = name
        self.query = ""

    def initialize(self):
        conn = sqlite3.connect(self.dbname)  # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()

        # Создание таблицы
        cursor.execute("""CREATE TABLE IF NOT EXISTS companies
                          (id integer PRIMARY KEY, name text, key text,
                           email text)
                       """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS employees
                                  (id integer PRIMARY KEY, company_id integer, password text,
                                   name text)
                               """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS time_count
                                  (id integer PRIMARY KEY, id_employee integer, salary float,
                                   start_time text, end_time text)
                               """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks
                                          (id integer PRIMARY KEY, task_name text, task_deadline text,
                                           start_time text, end_time text)
                                       """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS employee_task
                                          (id integer PRIMARY KEY, id_employee integer, 
                                           start_time text, end_time text)
                                       """)
        print("Инициализация завершена")

    def sqlite_query(self, text):
        conn = sqlite3.connect(self.dbname)  # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        cursor.execute(text)
        conn.commit()
        print(cursor.fetchall())



