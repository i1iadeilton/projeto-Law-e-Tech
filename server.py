from flask import Flask, render_template
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

@app.route('/alguma-funcao/')
def my_link():
  # executar alguma função
  return 'teste'

if __name__ == '__main__':
  app.run(debug=True)
  app.static_folder = 'static'