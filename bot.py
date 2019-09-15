import telebot
from telebot import types
import time
import string
import random

from features.weather import get_weather
from features.weather import weather_info
from features.weather import weather
from features.weather import pred_weather
from features.weather import weather_pred_info
from features.weather import weather_ents as winfo

import datetime
from datetime import timedelta

from rasa.nlu_model import train_nlu

import json

bot_token = '876715703:AAEKB7eVs-0_QL5CYP-lAxqQKQ6A94W12Pc'

bot = telebot.TeleBot(token=bot_token)

tomorrow = datetime.date.today() + timedelta(days=1)
tomorrow_time = str(tomorrow) + ' 12:00:00'

domain_state = 0

interpreter = train_nlu("./rasa/data/data.json", "./rasa/config_spacy.yml")


def compare(s1, s2):
    remove = string.punctuation + string.whitespace
    return s1.translate(None, remove) == s2.translate(None, remove)


def interpret(message, interpreter):
    data = interpreter.parse(message)
    if 'no' in message:
        data["intent"]["name"] = "deny"
    return data


def retreive_intent(message):
    # Interpret the message
    parse_data = interpret(message, interpreter)
    # Extract the intent
    intent = parse_data["intent"]["name"]
    print(intent)
    return intent


def retreive_entities(message):
    # Interpret the message
    parse_data = interpret(message, interpreter)
    # Extract the entities
    entities = parse_data["entities"]
    print(entities)
    return entities


def responds(intent, responses):
    # Check for a question mark
    return random.choice(responses[intent])


def get_time(time):
    return str(time) + ' 12:00:00'


# app = Flask(__name__)


def get_current_state(user_id):
    return


def write_json(data, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_user_name(message):
    return message.message.first_name


'''
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        write_json(msg, 'telegram_request.json')

        return Response('ok', status=200)
    else:
        return '<h1>Whisper bot</h1>'


def webhook():
    update = telebot.types.update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200
'''


def find_at(msg):
    for text in msg:
        if '@' in text:
            return text


def find_number_sign(msg):
    for text in msg:
        if '#' in text:
            return text


def search_weather(winfo, chat_id):
    if 'day' not in winfo and 'time' not in winfo:
        current = get_weather(winfo['location'])
        city, country, wt, t, maxt, mint, humidity, pressure = weather_info(current)
        responses = ['Aha, look at what I found!', 'Here is what I found:', 'I have found something for you']
        bot.send_message(chat_id, random.choice(responses))
        response = 'city:     {}\ncountry:     {}\nweather:     {}\ntemperature:    {} ' \
                   '℃\nMax_temperature:    {} ' \
                   '℃\nMin_temperature:    {} ℃\nhumidity:   {} \npressure:   {} \n'.format(
            city, country, wt, t, maxt, mint, humidity, pressure)
        bot.send_message(chat_id, response)
    else:
        if 'time' in winfo:
            if winfo['time'] == 'tomorrow':
                predict = pred_weather(winfo['location'])
                city, country, wt, t, maxt, mint, humidity, pressure = weather_pred_info(predict, tomorrow_time)
                responses = ['Aha, look at what I found!', 'Here is what I found:', 'I have found something for you']
                bot.send_message(chat_id, random.choice(responses))
                response = 'city:     {}\ncountry:     {}\nweather:     {}\ntemperature:    {} ' \
                           '℃\nMax_temperature:    {} ' \
                           '℃\nMin_temperature:    {} ℃\nhumidity:   {} \npressure:   {} \n'.format(
                    city, country, wt, t, maxt, mint, humidity, pressure)
                print(response)
                bot.send_message(chat_id, response)
            else:
                predict = pred_weather(winfo['location'])
                pred_time = get_time(winfo['time'])
                city, country, wt, t, maxt, mint, humidity, pressure = weather_pred_info(predict, pred_time)

                response = 'city:     {}\ncountry:     {}\nweather:     {}\ntemperature:    {} ' \
                           '℃\nMax_temperature:    {} ' \
                           '℃\nMin_temperature:    {} ℃\nhumidity:   {} \npressure:   {} \n'.format(
                    city, country, wt, t, maxt, mint, humidity, pressure)
                print(response)
                bot.send_message(chat_id, response)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     'Welcome! This is Whisper, how can I help you? \n(For instruction, plz enter \' /help \')')


@bot.message_handler(commands=['help'])
def ask_domain(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('#weather')
    itembtn2 = types.KeyboardButton('#movie')
    itembtn3 = types.KeyboardButton('#gaming')
    markup.add(itembtn1, itembtn2, itembtn3)
    chat_id = message.chat.id
    bot.send_message(chat_id, "Choose one the domain you wanna know:", reply_markup=markup)
    # bot.reply_to(message, 'tell me what do you wanna know directly or by following commands /weather /sport /movie')


@bot.message_handler(func=lambda msg: msg.text is not None and retreive_intent(msg.text) == 'greet' or retreive_intent(
    msg.text) == 'goodbye' or retreive_intent(msg.text) == 'appreciate')
def greet_googbye(message):
    try:
        chat_id = message.chat.id
        fn = message.chat.first_name
        intent = retreive_intent(message.text)
        responses = {'greet': ['Hi {}, Nice to meet you!'.format(fn),
                               'Hello {}, What can I do for you?'.format(fn),
                               'Greeting {}, May I help you?'.format(fn)],
                     'goodbye': ["See you!",
                                 'Bye, have a good one!',
                                 "Good bye!"],
                     'appreciate': [':)',
                                    'It\'s my pleasure',
                                    'You\'re welcome']
                     }
        response = responds(intent, responses)
        bot.send_message(chat_id, response)
    except Exception as e:
        print(e.message, e.args)
        bot.reply_to(message, 'Sorry, I don\'t understand')


@bot.message_handler(func=lambda msg: msg.text is not None and '#weather' in msg.text)
def ask_city(message):
    try:
        chat_id = message.chat.id
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.reply_to(message, 'Okay, so tell me which city it is', reply_markup=markup)
        bot.register_next_step_handler(msg, ask_country)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def ask_country(message):
    try:
        chat_id = message.chat.id
        weather.city = message.text
        msg = bot.send_message(chat_id, 'Good, then tell me which country it belongs to')
        bot.register_next_step_handler(msg, weather_results)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def weather_results(message):
    try:
        chat_id = message.chat.id
        weather.country = message.text
        current = get_weather(weather.city + ', ' + weather.country)
        city, country, wt, t, maxt, mint, humidity, pressure = weather_info(current)
        response = 'city:     {}\ncountry:     {}\nweather:     {}\ntemperature:    {} ℃\nMax_temperature:    {} ' \
                   '℃\nMin_temperature:    {} ℃\nhumidity:   {} \npressure:   {} \n'.format(
            city, country, wt, t, maxt, mint, humidity, pressure)
        bot.send_message(chat_id, response)
    except Exception as e:
        print(e.with_traceback())
        bot.reply_to(message, 'oooops')


@bot.message_handler(func=lambda msg: msg.text is not None and 'weather' in msg.text)
def send_weather_info(message):
    try:
        winfo.clear()
        chat_id = message.chat.id
        ents = retreive_entities(message.text)
        # print(ents)
        for ent in ents:
            entity = ent['entity']
            value = ent['value']
            winfo[entity] = value
        if 'location' in winfo:
            search_weather(winfo, chat_id)
        else:
            msg = bot.send_message(chat_id, 'can you tell me its location')
            bot.register_next_step_handler(msg, ask_location)
    except Exception as e:
        print(e.message, e.args)
        bot.reply_to(message, 'Sorry, I don\'t understand')


def ask_location(message):
    try:
        chat_id = message.chat.id
        ents = retreive_entities(message.text)
        print(ents)
        for ent in ents:
            if ent['entity'] == 'location':
                winfo['location'] = ent['value']
            else:
                winfo['location'] = message.text
        search_weather(winfo, chat_id)
    except Exception as e:
        print(e.message, e.args)
        bot.reply_to(message, 'Sorry, I don\'t understand')


@bot.message_handler(func=lambda msg: msg.text is not None and 'No' in msg.text or 'no' in msg.text)
def change_country(message):
    try:
        chat_id = message.chat.id
        ents = retreive_entities(message.text)

        for ent in ents:
            if ent['entity'] == 'location':
                winfo['location'] = winfo['location'] + ', ' + ent['value']
            else:
                bot.send_message('Can you tell me the location more accurately?')
        search_weather(winfo, chat_id)
    except Exception as e:
        print(e.message, e.args)
        bot.reply_to(message, 'Sorry, I don\'t understand')


@bot.message_handler(commands=['weather'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.reply_to(chat_id, 'Okay, so which city do you wanna know the information?')


@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))


@bot.message_handler(func=lambda msg: msg.text is not None)
def apology(message):
    bot.reply_to(message, 'Sorry, I don\'t understand\n(enter /start to start the bot or /help for instruction)')


# def main():

# https://api.telegram.org/bot876715703:AAEKB7eVs-0_QL5CYP-lAxqQKQ6A94W12Pc/setWebhook?url=http://65346bf6.ngrok.io/

if __name__ == '__main__':
    # print(retreive_entities("Tell me the weather in Tokyo, Japan"))

    while True:
        try:
            # Enable saving next step handlers to file "./.handlers-saves/step.save".
            # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
            # saving will hapen after delay 2 seconds.
            # bot.enable_save_next_step_handlers(delay=1)

            # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
            # WARNING It will work only if enable_save_next_step_handlers was called!
            # bot.load_next_step_handlers()
            # app.run(debug=True)

            bot.polling()
        except Exception:
            time.sleep(15)
