from flask import Flask, render_template, request, redirect, session
from environs import Env
import requests

env = Env()
env.read_env() # reads from the .env file
app = Flask(__name__)
app.secret_key = env("SECRET")
base_url = "http://mcastelnoble-001-site3.ftempurl.com"
ACCESS_TOKEN = env("ACCESS_TOKEN")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

        # Authenticate with the API
        response = requests.post(f'{base_url}/Services/APICustomer/Login', headers=headers, json={
            "User": username,
            "Password": password
        })

        if response.status_code == 200:
            data = response.json()
            session['_token'] = data['Token']
            return redirect('/packages')  # Redirect to packages page
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/packages')
def packages():
    # Retrieve packages using the API with the access token
    _token = session.get('_token')
    if _token:
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        response = requests.post(f'{base_url}/Services/APICustomer/GetPackages', headers=headers, json={
            "Token": _token,
             "PackageNumber": "",
             "PackageAirwayBillNumber": "",
             "PackageStatus":""
            })
        packages = response.json()
        #import ipdb;ipdb.set_trace()
        return render_template('packages.html', packages=packages)
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
