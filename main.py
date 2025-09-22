from flask import Flask, request, jsonify
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to my Flask API server!</h1>"


@app.route("/fact")
def fact():
    username = request.args.get("username", "Friend")
    fact_type = request.args.get("type", "joke")

    if fact_type == "joke":
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        data = response.json()
        content = f"{data['setup']} ... {data['punchline']}"

    elif fact_type == "number":
        url = "http://numbersapi.com/random/trivia"
        response = requests.get(url)
        content = response.text

    html_content = f"<h1>Hello {username}!</h1><p>{content}</p><a href='/'>Back</a>"
    return html_content


@app.route("/jokes")
def jokes():
    count = request.args.get("count", "2")

    try:
        count = int(count)
    except ValueError:
        count = 2

    html_content = f"<h1>{count} Random Jokes</h1>"

    for i in range(count):
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        data = response.json()
        joke = f"{data['setup']} ... {data['punchline']}"
        html_content += f"<p>{i + 1}. {joke}</p>"

    html_content += "<a href='/'>Home</a>"
    return html_content


@app.route("/number")
def number():
    num = request.args.get("num", "42")

    url = f"http://numbersapi.com/{num}/trivia"
    response = requests.get(url)
    fact = response.text

    html_content = f"<h1>Number Fact</h1><p>{fact}</p><a href='/'>Back</a>"
    return html_content



@app.route("/api/joke")
def api_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)


@app.route("/api/number")
def api_number():
    num = request.args.get("num", "42")
    url = f"http://numbersapi.com/{num}/trivia"
    response = requests.get(url)
    return jsonify({"number": num, "fact": response.text})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
