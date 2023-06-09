import requests
from send_email import email_send

api_key = "befd96e6cf1b4a808a4a62ac4a1d0627"

url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=befd96e6cf1b4a808a4a62ac4a1d0627"

request = requests.get(url)
content = request.json()


body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
email_send(message=body)
