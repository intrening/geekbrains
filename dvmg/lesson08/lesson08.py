import json
from yandex_geocoder import Client
from geopy import distance
import folium
from flask import Flask

def min_distance(bar):
  return bar['distance']

def get_bar_list(place_current):
  bar_list = []
  with open("data.json", "r", encoding='CP1251') as file:
    bars_data = json.load(file)
  
  for bar in bars_data:
    new_bar = {
      'title': bar['Name'],
      'latitude': bar['geoData']['coordinates'][0],
      'longitude': bar['geoData']['coordinates'][1],
      'distance': distance.distance(place_current, (bar['geoData']['coordinates'][1],bar['geoData']['coordinates'][0])).km
    }
    bar_list.append(new_bar)

  return sorted(bar_list, key=min_distance)

def hello_world():
  with open('index.html') as file:
    return file.read()

def publish_site():
  app = Flask(__name__)
  app.add_url_rule('/', 'hello', hello_world)
  app.run('0.0.0.0')

def make_map(place_current, bar_list, max_bars = 5):
  bar_map = folium.Map(location=place_current, zoom_start=15)
  folium.Marker(place_current, popup='<i>Вы здесь</i>').add_to(bar_map)
  
  for bar in bar_list[:max_bars]:
    folium.Marker([bar['longitude'], bar['latitude']], icon=folium.Icon(color='green'), popup=bar['title']).add_to(bar_map)
  
  bar_map.save('index.html')


def main():
  inp = input('Введите адрес для поиска: ')
  place_current = [float(Client.coordinates(inp)[1]),float(Client.coordinates(inp)[0])]
  bar_list = get_bar_list(place_current)
  make_map (place_current, bar_list)
  publish_site()

if __name__ == '__main__':
  main()