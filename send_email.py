import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    with open('sec.txt', 'r') as file:
        password = file.readline()

    username = "joesidious@gmail.com"

    receiver = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
