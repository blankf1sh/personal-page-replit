from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input/<name>')
def input(name):
  return 'Hello'+name

@app.route('/.well-known/nostr.json')
def nostr():
  return '{"names":{"nemo":"public key goes here"}}'

def buttonFunction():
  return 'My name is nemo'

app.run(host='0.0.0.0', port=81)
