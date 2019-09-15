import requests
from rasa.nlu_model import train_nlu
import string

# Initialize the empty dictionary and lists
params, suggestions, excluded = {}, [], []

weather_ents = {}


def compare(s1, s2):
    remove = string.punctuation + string.whitespace
    return s1.maketrans(dict.fromkeys(remove)) == s2.maketrans(dict.fromkeys(remove))


class weather:
    def __init__(self):
        self.city = None
        self.country = None
        self.main_weather = None
        self.temp = None
        self.temp_min = None
        self.temp_max = None
        self.pressure = None
        self.humidity = None


def weather_info(temp):
    city = temp['name']
    country = temp['sys']['country']
    weather = temp['weather'][0]['main']
    t = float('%.2f' % (temp['main']['temp'] - 273.15))
    maxt = float('%.2f' % (temp['main']['temp_max'] - 273.15))
    mint = float('%.2f' % (temp['main']['temp_min'] - 273.15))
    humidity = temp['main']['humidity']
    pressure = temp['main']['pressure']

    return city, country, weather, t, maxt, mint, humidity, pressure


def weather_pred_info(temp, time):
    city = temp['city']['name']
    country = temp['city']['country']
    for data in temp['list']:
        if compare(data['dt_txt'], time) is True:
            wt = data['weather'][0]['main']
            t = float('%.2f' % (data['main']['temp'] - 273.15))
            maxt = float('%.2f' % (data['main']['temp_max'] - 273.15))
            mint = float('%.2f' % (data['main']['temp_min'] - 273.15))
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']

    return city, country, wt, t, maxt, mint, humidity, pressure


'''
# define get_weather() in given city and country
def get_weather_cc(city, country):
    querystring = {"callback": "", "id": "2172797", "units": "\"metric\"", "mode": "JSON",
                   "q": "{},{}".format(city, country)}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "405ea20859mshe8ff965dbb40800p108b05jsna3f1ce90d9bf"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    js = response.json()
    # print(float('%.2f' % (js['main']['temp'] - 273.15)))
    # print('weather: {}\n'.format(js['weather'][0]['main']))
    print(js)
    return js
'''


# define pred_weather to find out the weather in the future
def pred_weather(location):
    import requests

    url = "https://community-open-weather-map.p.rapidapi.com/forecast"

    querystring = {"q": "{}".format(location)}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "405ea20859mshe8ff965dbb40800p108b05jsna3f1ce90d9bf"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    js = response.json()

    print(js)
    return js


# define get_weather() in given city
def get_weather(location):
    querystring = {"callback": "", "id": "2172797", "units": "\"metric\"", "mode": "JSON",
                   "q": "{}".format(location)}

    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "405ea20859mshe8ff965dbb40800p108b05jsna3f1ce90d9bf"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    js = response.json()
    # print(float('%.2f' % (js['main']['temp'] - 273.15)))
    # print('weather: {}\n'.format(js['weather'][0]['main']))
    print(js)
    return js


'''
def interpret(message):
    interpreter = train_nlu("./rasa/data/data.json", "./rasa/config_spacy.yml")
    data = interpreter.parse(message)
    if 'no' in message:
        data["intent"]["name"] = "deny"
    return data


def retreive_entities(message):
    # Interpret the message
    parse_data = interpret(message)
    # Extract the intent
    intent = parse_data["intent"]["name"]
    print(intent)
    # Extract the entities
    entities = parse_data["entities"]
    print(entities[0])
    return entities[0]
'''

# retreive_entities("tell me the weather in Beijing")
# get_weather('Wuhan')
# print(datetime.datetime.strptime('20-Nov-2002','%d-%b-%Y'))
# print(str(tomorrow) + ' 12:00:00')


# if compare('2019 - 9 - 18 12:00:00', '2019-09-18 12:00:00') is True:
# print('Yes')
