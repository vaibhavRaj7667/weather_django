from django.shortcuts import render,redirect
import requests
# views.py
from .forms import CityForm

def get_weather(request):
    api_key = "ddf124349f6ce8059b3501c5c5c1992b"
    weather = temp = wind = error = None

    if request.method =='POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']

            weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

            if weather_info.json()['cod']=='404':
                error = 'no city found'
            else:
                weather = weather_info.json()['weather'][0]['main']
                wind = weather_info.json()['wind']['speed']
                temp = round(weather_info.json()['main']['temp'])

            return render(request,'home.html',{'city':city,'weather':weather,'wind':wind,'error':error,'temp':temp,'form':form})
        
    else:
        form = CityForm()

    return render(request,'home.html',{'form':form})