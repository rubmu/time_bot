import telebot
import SQLite_init
class time_bot:
    bot_token = '1045946181:AAGp9K8O-MhZSFuOoSK87CYLt7hMe2VkT0Y'
    sql = SQLite_init.SQL("test.db")


    def start(self):
        self.bot = telebot.TeleBot(self.bot_token)

    def working(self):
        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            #self.bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
            checker = self.check_user_if_exist(message.chat.id)
            if checker==True:
                self.bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
            else:
                self.bot.send_message(message.chat.id, 'Добрый день, Вас приветствует чат-бот желаете зарегистрироваться или войти?')
                self.user_choise()



        self.bot.polling()

    def check_user_if_exist(self, chat_id):
        query = "select chat_id from employees where chat_id = " + str(chat_id)
        print(query)
        result = self.sql.sqlite_query(query)
        if result == []:
            return False
        else:
            return True

    def user_choise(self):
        @self.bot.message_handler(commands=['Зарегистрироваться'])
        def registration(message):
            print("Зарегистрироваться")

        @self.bot.message_handler(commands=['Войти'])
        def registration(message):
            print("Войти")
