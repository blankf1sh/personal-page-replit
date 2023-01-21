from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/input/<name>')
def input(name):
  return 'Hello'+name

@app.route('/.well-known/nostr.json')
def nostr():
  return '{"names":{"nemo":"public key goes here"}}'

app.run(host='0.0.0.0', port=81)
