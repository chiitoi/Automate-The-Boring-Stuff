import random, pprint

def get_random_weather_data():
    weather = {}
    temperature = round(random.uniform(-50, 50), 1)
    weather['temp'] = temperature
    weather['feels_like'] = round(random.uniform(temperature-10, temperature+10), 1)
    weather['humidity'] = random.randint(0,100)
    weather['pressure'] = random.randint(990, 1010)
    return weather

def get_average_temperature(weather_data):
    total = 0
    for weather_dict in weather_data:
        total += weather_dict['temp']
    return round(total / len(weather_data),1)

weather_list = []
for _ in range(100):
    weather_list.append(get_random_weather_data())

pprint.pprint(weather_list)

print(get_average_temperature(weather_list))