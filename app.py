from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Birim dönüşüm katsayıları
lenghtUnits = {
    'milimeter': 0.001, 'centimeter': 0.01, 'meter' : 1.0,
    'kilometer': 1000.0, 'inch': 0.0254, 'foot': 0.3048,
    'yard': 0.9144, 'mile': 1609.34
}

weightUnits = {
    'miligram': 0.001, 'gram': 1.0, 'kilogram': 1000.0,
    'ounce': 28.3495, 'pound': 453.592 
}

# --- ANA SAYFA YÖNLENDİRMESİ ---
# Kullanıcı direkt siteye girdiğinde Weight sayfasına gider
@app.route('/')
def home():
    return redirect(url_for('weight'))

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    if request.method == 'POST':
        try:
            val = float(request.form['value'])
            unit_from = request.form['from']
            unit_to = request.form['to']
            result = val * (lenghtUnits[unit_from] / lenghtUnits[unit_to])
        except (ValueError, KeyError):
            result = "Error"
    return render_template('length.html', units=lenghtUnits.keys(), result=result)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = None
    if request.method == 'POST':
        try:
            val = float(request.form['value'])
            unit_from = request.form['from']
            unit_to = request.form['to']
            result = val * (weightUnits[unit_from] / weightUnits[unit_to])
        except (ValueError, KeyError):
            result = "Error"
    return render_template('weight.html', units=weightUnits.keys(), result=result)

@app.route('/temperature', methods=['GET', 'POST'])
def temp():
    result = None
    temp_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    if request.method == 'POST':
        try:
            val = float(request.form['value'])
            f = request.form['from']
            t = request.form['to']
            
            # Celsius'a çevir
            if f == 'Fahrenheit': c = (val - 32) * 5/9
            elif f == 'Kelvin': c = val - 273.15
            else: c = val

            # Hedefe çevir
            if t == 'Fahrenheit': result = (c * 9/5) + 32
            elif t == 'Kelvin': result = c + 273.15
            else: result = c
        except ValueError:
            result = "Error"
            
    return render_template('temp.html', units=temp_units, result=result)

if __name__ == '__main__':
    app.run(debug=True)