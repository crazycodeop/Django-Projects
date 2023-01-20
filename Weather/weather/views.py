from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=98e0937fdb2d36311b46a4e6e82933e4').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinates': 'Longitude: ' + str(json_data['coord']['lon']) + ' Latitude: ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'K',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),    
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'data': data, 'city': city})
