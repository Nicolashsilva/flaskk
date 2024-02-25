from flask import Flask

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, Nicolas!'

@app.route('/sobre')
def sobre_mim():
  return 'Nicolas Henrique pt3022382! Prontuário: pt3022382 instituicao : IFSP'

@app.route('/host')
def host():
  return ' 192.168.15.1'

app.run(host='0.0.0.0', port=8080)