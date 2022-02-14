from flask import Flask,render_template,request
import requests
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/current' , methods=['GET','POST'])
def current():
    if request.method == 'POST':
        name = request.form['name']
        api_url = 'http://api.weatherapi.com/v1/current.json?key=089caf54a64843419ab95848211511&q='+name
        response = requests.get(api_url)
        result = response.json()
        return render_template('current.html',name=result)
    else:
        return render_template('current.html')

@app.route('/forecast' , methods=['GET','POST'])
def forecast():
    if request.method == 'POST':
        name = request.form['name']
        api_url = 'http://api.weatherapi.com/v1/forecast.json?key=089caf54a64843419ab95848211511&q='+name+'&days=10'
        response = requests.get(api_url)
        result = response.json()
        return render_template('forecast.html',name=result)
    else:
        return render_template('forecast.html')

@app.route('/forecast/<string:city>/<string:date>' , methods=['GET','POST'])
def forecastDetails(city,date):
    api_url = 'http://api.weatherapi.com/v1/forecast.json?key=089caf54a64843419ab95848211511&q='+city+'&days=10'
    response = requests.get(api_url)
    result = response.json()
    forecastday = result["forecast"]["forecastday"]
    dataObj = {}
    for day in forecastday:
        if(day["date"] == date):
            dataObj = day
    return render_template('forecastDetails.html',name=dataObj)
    
@app.route('/search', methods=['GET','POST']) 
def search():
    if request.method == 'POST':
        city= request.form['city']
        api_url = 'http://api.weatherapi.com/v1/search.json?key=089caf54a64843419ab95848211511&q='+city
        response = requests.get(api_url)
        result = response.json()
        return render_template('search.html',name=result, city=city)
    else:
        return render_template('search.html')

if __name__ == "__main__":
     app.run(debug=True)