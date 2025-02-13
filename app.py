from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

# Konfigurasi database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ip_locations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class IPLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# API Key untuk ipinfo.io
ACCESS_TOKEN = 'f7eec03ef1f1ef'  # token yang valid

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track_ip():
    user_ip = request.form['ip_address'] if 'ip_address' in request.form else request.remote_addr
    
    # Mengirim request ke API ipinfo.io untuk mendapatkan lokasi berdasarkan IP
    url = f'https://ipinfo.io/{user_ip}/json?token={ACCESS_TOKEN}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        location = data.get('city', 'Unknown') + ", " + data.get('region', 'Unknown') + ", " + data.get('country', 'Unknown')

        # Simpan data IP dan lokasi ke dalam database
        new_ip_location = IPLocation(ip_address=user_ip, location=location)
        db.session.add(new_ip_location)
        db.session.commit()

        return render_template('result.html', ip=user_ip, location=location)
    else:
        return 'Gagal mendapatkan data lokasi.'

@app.route('/history')
def history():
    ip_locations = IPLocation.query.all()
    return render_template('history.html', ip_locations=ip_locations)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
