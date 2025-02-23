from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_migrate import Migrate

app = Flask(__name__)

# Konfigurasi database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ip_locations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # migrasi database bil

class IPLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    abuse_info = db.Column(db.Text, nullable=True)  # Tambahkan kolom ini

# API Key untuk ipinfo.io
ACCESS_TOKEN = 'f7eec03ef1f1ef'  # token yang valid

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track_ip():
    user_ip = request.form['ip_address'] if 'ip_address' in request.form else request.remote_addr
    print(f"User IP: {user_ip}")  # Debug: Cek apakah IP benar-benar diterima
    
    record_count = db.session.query(IPLocation).count() # Cek jumlah data di database

    if record_count >= 25:
        db.session.query(IPLocation).delete()
        db.session.commit()
        print("Database direset karena sudah mencapai 25 data!") # Reset database jika data sudah mencapai 25
    
    # Mengirim request ke API ipinfo.io untuk mendapatkan lokasi berdasarkan IP
    url = f'https://ipinfo.io/{user_ip}/json?token={ACCESS_TOKEN}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        city = data.get('city', 'Unknown')
        region = data.get('region', 'Unknown')
        country = data.get('country', 'Unknown')
        org = data.get('org', 'Unknown')  # ISP
        timezone = data.get('timezone', 'Unknown')
        loc = data.get('loc', 'Unknown')  # Latitude, Longitude

        # Data Abuse (jika tersedia)
        abuse_info = data.get('abuse', {})
        abuse_address = abuse_info.get('address', 'Unknown')
        abuse_country = abuse_info.get('country', 'Unknown')
        abuse_email = abuse_info.get('email', 'Unknown')
        abuse_name = abuse_info.get('name', 'Unknown')
        abuse_network = abuse_info.get('network', 'Unknown')
        abuse_phone = abuse_info.get('phone', 'Unknown')

         # Format lokasi dan abuse data dengan rapi
        location = f"{city}, {region}, {country} | Koordinat: {loc} | ISP: {org} | Zona Waktu: {timezone}"
        abuse_details = f"Nama: {abuse_name} | Alamat: {abuse_address} | Negara: {abuse_country} | Email: {abuse_email} | Jaringan: {abuse_network} | Telepon: {abuse_phone}"

        # Simpan data IP dan lokasi ke dalam database
        new_ip_location = IPLocation(ip_address=user_ip, location=location)
        db.session.add(new_ip_location)
        db.session.commit()

        return render_template('result.html', ip=user_ip, location=location)
    else:
        return render_template('error.html')

@app.route('/history')
def history():
    ip_locations = IPLocation.query.all()
    return render_template('history.html', ip_locations=ip_locations)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
