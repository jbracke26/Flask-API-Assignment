import requests

print("Testing my Flask API server")

try:
    print("Getting a joke...")
    response = requests.get("http://127.0.0.1:8000/api/joke")
    joke_data = response.json()
    print("joke:")
    print(f"Setup: {joke_data['setup']}")
    print(f"Punchline: {joke_data['punchline']}")

    num = input("Enter a number for a fact: ")
    print("Getting number fact...")
    response = requests.get(f"http://127.0.0.1:8000/api/number?num={num}")
    number_data = response.json()
    print("number fact:")
    print(f"Number: {number_data['number']}")
    print(f"Fact: {number_data['fact']}")

except requests.exceptions.ConnectionError:
    print("server is not running")