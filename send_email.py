import smtplib
import ssl
import os


def email_send(message):
    host = "smtp.gmail.com"
    port = 465

    username = "techgeeksinit@gmail.com"
    password = "tvvqlucvcbjmxrda"

    receiver = "techgeeksinit@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)