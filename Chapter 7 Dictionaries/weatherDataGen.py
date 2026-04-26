import random, pprint

def get_random_weather_data():
    weather = {}
    temperature = round(random.uniform(-50, 50), 1)
    weather['temp'] = temperature
    weather['feels_like'] = round(random.uniform(temperature-10, temperature+10), 1)
    weather['humidity'] = random.randint(0,100)
    weather['pressure'] = random.randint(990, 1010)
    return weather

weather_list = []
for _ in range(100):
    weather_list.append(get_random_weather_data())

pprint.pprint(weather_list)