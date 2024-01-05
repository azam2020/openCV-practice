from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import json
import pytz
import requests

timezone = pytz.timezone("Asia/Kolkata")
timestamp = datetime.now(timezone).strftime("%d/%m/%Y %H:%M")
font_size = 30
font = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
bar_size_percent = 95
location = "Aligarh,in"
new_image_size = 1920, 1080
api_key = "792bb1f7570e486997ec3653e7320041"

response = json.loads(requests.get("https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key+"&units=metric").text)
weather_string = timestamp+" "
weather_string += response['name']+", "+response['sys']['country']+" - Temp:"+str(response['main']['temp'])+" dCS Perceived:"+str(response['main']['feels_like'])+"dCs -"
for weather_data in response['weather']:
	weather_string+=" "+weather_data['description']

print(weather_string)

im = Image.open("latest.jpg")
draw = ImageDraw.Draw(im)
bar_font = ImageFont.truetype(font,font_size)

size_y = round(bar_size_percent*im.size[1]/100.0)
shape = [(0,size_y),im.size]
draw.rectangle(shape,fill='#777', outline='#000')

draw.text((25,im.size[1]-45),weather_string,(255,255,255),font=bar_font)

im.thumbnail(new_image_size)
im.save('weatherwebcam.jpg',"JPEG")
