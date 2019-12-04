import SQLite_init


liteDb = SQLite_init.SQL("test.db")
liteDb.initialize()
text = """Insert into companies (name, key, email)
        values ('zalupa', 'APIKEY', 'mail')"""
liteDb.sqlite_query(text)
liteDb.sqlite_query("select * from companies")

