from flask import Flask, render_template, redirect, request, url_for
import os 
from pathlib import Path
import random

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pages/login.html')
def login():
  return render_template('pages/login.html')

@app.route('/pages/cadastro.html')
def cadastro():
  return render_template('pages/cadastro.html')

@app.route('/pages/sobre.html')
def sobre():
  return render_template('pages/sobre.html')

@app.route('/pages/suporte.html')
def suporte():
  return render_template('pages/suporte.html')

@app.route('/create-folder', methods=['POST'])
def create_folder():
    data = request.data.decode('UTF-8')
    allDataStored = 'datastore'
    absolutePath = Path().absolute()
    path = f'{absolutePath}/{allDataStored}/{data}'
    try: 
      os.mkdir(path)
    except OSError as error: 
      print(error)
    try:
      port = random.randrange(65535)
      os.system(f'python3 changedetection.py -d {path} -p {port}')
      print(port)
    except OSError as error:
      print(error)
      port = random.randrange(65535)
      os.system(f'python3 changedetection.py -d {path} -p {port}')
      print(port)
    return redirect(f'http://localhost:{port}')

if __name__ == '__main__':
  app.run(debug=True)
  app.static_folder = 'static'