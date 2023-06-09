import requests

api_key = "befd96e6cf1b4a808a4a62ac4a1d0627"

url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=befd96e6cf1b4a808a4a62ac4a1d0627"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
