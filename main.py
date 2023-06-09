import requests
from send_email import email_send

api_key = "befd96e6cf1b4a808a4a62ac4a1d0627"

topic = "tesla"

url = "https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey=befd96e6cf1b4a808a4a62ac4a1d0627&language=en"

request = requests.get(url)
content = request.json()


body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + \
            article["url"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
email_send(message=body)
