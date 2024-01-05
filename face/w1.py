from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import json
import pytz
import requests

print("Azam")
timezone = pytz.timezone("Asia/Kolkata")
timestamp = datetime.now(timezone).strftime("%d/%m/%Y %H:%M")
font_size = 30
font = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
bar_size_percent = 95
location = "Aligarh,in"
new_image_size = 1920, 1080
api_key = "792bb1f7570e486997ec3653e7320041"

response = json.loads(requests.get("https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key+"&units=metric").text)
print(type(response))
weather_string = timestamp+" "
weather_string += response['name']+", "+response['sys']['country']+" - Temp:"+str(response['main']['temp'])+" dCS Perceived:"+str(response['main']['feels_like'])+"dCs -"
for weather_data in response['weather']:
	weather_string+=" "+weather_data['description']

print(weather_string)
