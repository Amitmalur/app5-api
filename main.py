import requests
from send_email import email_send

api_key = ""

topic = "tesla"

url = "https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey=xxxx&language=en"

request = requests.get(url)
content = request.json()


body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + \
            article["url"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
email_send(message=body)
