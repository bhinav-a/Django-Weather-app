from django.shortcuts import render
import datetime
import requests

def home(request):
    # Get the city from form submission or default to 'nagpur'
    if request.method == "POST" and 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'nagpur'

    # API request
    url = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {
        'q': city,
        'appid': 'f158feb9e46b8fe3fec4092caa808caa',
        'units': 'metric'
    }

    # ✅ This is the correct way to make an external API call
    response = requests.get(url, params=PARAMS)
    data = response.json()  # parse JSON from API response

    try:
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
    except (KeyError, IndexError):
        description = "Not found"
        icon = ""
        temp = "N/A"

    day = datetime.date.today()
    return render(request, 'index.html', {
        'day': day,
        'description': description,
        'icon': icon,
        'temp': temp,
        'city': city
    })