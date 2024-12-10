from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"


@app.route('/users')
def users():
    return jsonify({'name': 'Amauri', 'profissão': 'DEVOPS'})

if __name__ == '__main__':
    app.run(debug=True)