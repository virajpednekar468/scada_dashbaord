from flask import Flask,render_template,jsonify,request
from flask_cors import CORS 
from module import get_level, get_flow,get_pressure,get_temperature

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/parameter')
def parameter():
    return render_template("parameter.html")

@app.route('/resistorvalue')
def resistor():
    return render_template("resistorvalue.html")

@app.route('/aboutus')
def about_us():
    return render_template("about.html")

@app.route('/instru')
def instru():
    return render_template("instru.html")

# ----process value code start ------- 

@app.route('/temp')
def temperature():
    return jsonify({'temperature': get_temperature()})

@app.route('/pressure')
def pressure():
    return jsonify({'pressure': get_pressure()})

@app.route('/Level')
def level():
    return jsonify({'level': get_level()})

@app.route('/flow')
def flow():
    return jsonify({'flow':  get_flow()})

# ------------code end------------
# --------tank code start---------- 
@app.route('/set_temperature', methods=['POST'])
def set_temperature():
    try:
        data = request.get_json()
        if not data or 'temperature' not in data:
            return jsonify({'error': 'Invalid request, temperature is required'}), 400
        
        temperature = float(data.get('temperature', 0))  # Allow decimals
        
        print(f"Received temperature: {temperature}")  # Debugging
    
        return jsonify({'temperature': temperature})  # Send back updated temperature

    except ValueError:
        return jsonify({'error': 'Invalid temperature value'}), 400  # Handle non-numeric input
    # -------------tank code end--------------

if __name__ == "__main__":
    app.run(debug=True)

