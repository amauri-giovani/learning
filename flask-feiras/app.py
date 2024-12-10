import json
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

url = "http://127.0.0.1:8000/feiraslivres/"
# url = "https://feiraslivres.herokuapp.com/feiraslivres"
# url = "http://127.0.0.1:8000/"

@app.route("/")
def home():
    header = {"accept": "application/json"}
    response = requests.get(url)#, headers=header)
    print(response)
    dados = json.loads(response.content)
    return jsonify(dados)


if __name__ == "__main__":
    app.run(debug=True)

