import SQLite_init
import time_bot

liteDb = SQLite_init.SQL("test.db")
liteDb.initialize()
bot = time_bot.time_bot()
bot.start()
bot.working()

