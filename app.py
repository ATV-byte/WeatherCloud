from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here
    useful_data = {}
    if request.method == 'POST':
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"q": request.form.get('q'), "lat": "0", "lon": "0", "lang": "null",
                       "units": "metric"}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "641a9d24e6msh57be48318c28698p13b739jsnbee5d827d8d9"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        print(data)
        cod = data['cod']
        if cod == 200:
            useful_data = {
                'loc': 'The weather in ' + data['name']+' is:',
                'desc': data['weather'][0]['description'],
                'real_temp': "Temperature: "+str(int(data['main']['temp']))+" Celsius",
                'felt_temp': "Felt temperature: "+str(int(data['main']['feels_like']))+" Celsius",
                'min': "Minimum temperature: "+str(int(data['main']['temp_min']))+" Celsius",
                'max': "Maximim temperature: "+str(int(data['main']['temp_max']))+" Celsius",
            }
            print(useful_data)
            return render_template("index.html", weather_data=useful_data, cod=cod)
        else:
            return render_template("index.html", cod=404)
    else:
        return render_template("index.html", cod=500)


if __name__ == '__main__':
    app.run()
