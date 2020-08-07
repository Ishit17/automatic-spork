from twilio.rest import Client

account_sid = 'Account SID'
auth_token = 'Authentication Token'
client = Client(account_sid, auth_token)

def message1():
    messages = client.messages \
        .create(
            media_url=['Image Url'],
            from_='whatsapp:Sender no',
            body="message",
            to='whatsapp:receiver no'
        )

def message2():
    messages = client.messages \
        .create(
           media_url=['Image Url'],
            from_='whatsapp:Sender no',
            body="message",
            to='whatsapp:receiver no'
        )

def message3():
    messages = client.messages \
        .create(
           media_url=['Image Url'],
            from_='whatsapp:Sender no',
            body="message",
            to='whatsapp:receiver no'
        )

def message4():
    messages = client.messages \
        .create(
           media_url=['Image Url'],
            from_='whatsapp:Sender no',
            body="message",
            to='whatsapp:receiver no'
        )