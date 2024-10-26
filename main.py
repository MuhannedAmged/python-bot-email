import telebot
from telebot import types
from tempmail import EMail

email = EMail()
address = email.address

API_TOKEN = "7613524639:AAF9nEq0vTkVLGUGQH5e4NIUWkhm9iZacW8";
bot = telebot.TeleBot(API_TOKEN)
photo_path = "Formal_Email.png"

@bot.message_handler(commands=['start'])
def start_command(message):
    # ------------------------------------------------
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    # ------------------------------------------------

    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Get An Email", callback_data="button1")
    button2 = types.InlineKeyboardButton("Inbox", callback_data="button2")
    button3 = types.InlineKeyboardButton("Change Email", callback_data="button3")
    button4 = types.InlineKeyboardButton("Info All Msg", callback_data="button4")
    markup.add(button1, button2, button3, button4)
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=f"Hello {first_name + " " + last_name}, welcome to the Emails bot. The bot gives a random email to create accounts for Facebook, Twitter, Snapchat, etc.", reply_markup=markup)


def handle_button1(call):
    bot.send_message(call.message.chat.id, f"EMAIL: {address}")
def handle_button2(call):
    msg = email.wait_for_message()
    from_address = msg.from_addr
    text_body = msg.text_body
    bot.send_message(call.message.chat.id, f"{from_address}\n{text_body}")
def handle_button3(call):
    global email
    global address
    email = EMail()
    address = email.address
    bot.send_message(call.message.chat.id, f"New email: {address}")
def handle_button4(call):
    inboxs = email.get_inbox()
    # inboxs.
    for inbox in inboxs:
        bot.send_message(call.message.chat.id, f"ID: {inbox.id}\nFrom: {inbox.from_addr}\nTo: {email.address}\nSubject: {inbox.subject}\nDate: {inbox.date_str}")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "button1":
        handle_button1(call)
    elif call.data == "button2":
        handle_button2(call)
    elif call.data == "button3":
        handle_button3(call)
    elif call.data == "button4":
        handle_button4(call)


bot.polling()