# import module
import telebot
import ctypes
import os
import re


API_KEY = '' //isi dengan API telegram bot kalian
TCHAT_ID = '' //isi dengan chat id telegram kalian

bot = telebot.TeleBot(API_KEY)

Message = 'Message'
DisplayMessage = False
Directory = ''

# Define Display Message Output
def SendMessage(Message):
    ctypes.windll.user32.MessageBoxW(0, Message, u', 0x40')

# Jika Display Message Aktif
if DisplayMessage is True:
    if not os.path.exists(Directory + 'DisplayMessage'):
        open(Directory + 'DisplayMessage', 'a').close()
        SendMessage(Message)

@bot.message_handler(regexp='/Message')
def Message(command):
    try:

        Message = re.split('/Message ', command.text, \
            flags=re.I)[1]
        bot.reply_to(command, 'Pesan telah terkirim!', \
            parse_mode='Markdown')
        SendMessage(Message)

    except:
        bot.send_message(TCHAT_ID, 'Masukkan pesan Anda\n\n*› \
            /Message*', parse_mode='Markdown')

bot.polling()
