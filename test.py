import config
import telebot
import os
import time

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['test'])
def fileids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1]=='ogg':
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)

if __name__ == '__main__':
    bot.polling(none_stop=True)