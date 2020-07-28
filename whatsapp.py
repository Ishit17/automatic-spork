from twilio.rest import Client

account_sid = 'AC61f36e448db9703e243dd0df556eecd4'
auth_token = '809519f76e6bab678d35bb5adb67c533'
client = Client(account_sid, auth_token)

def message1():
    messages = client.messages \
        .create(
            media_url=['https://staticimg.titan.co.in/Tanishq/Catalog/511556CAUAA00_1.jpg',
                        'https://staticimg.titan.co.in/Tanishq/Catalog/511556CASAA00_1.jpg',
                        'https://staticimg.titan.co.in/Tanishq/Catalog/511556CAOAA00_1.jpg',
                        'https://staticimg.titan.co.in/Tanishq/Catalog/513017CDPAA00_1.jpg',
                        'https://staticimg.titan.co.in/Tanishq/Catalog/513017CRNAA00_1.jpg'],
            from_='whatsapp:+14155238886',
            body="10gm Fox Chain",
            to='whatsapp:+919167410417'
        )

def message2():
    messages = client.messages \
        .create(
            media_url=['https://staticimg.titan.co.in/Tanishq/Catalog/511517YEVAAP4_1.jpg',
                      'https://staticimg.titan.co.in/Tanishq/Catalog/511029YHVAA00_1.jpg',
                      'https://staticimg.titan.co.in/Tanishq/Catalog/512018YWCAA00_1.jpg',
                      'https://staticimg.titan.co.in/Tanishq/Catalog/511250YHPAA00_1.jpg',
                      'https://staticimg.titan.co.in/Tanishq/Catalog/511250YHSAA00_1.jpg'],
            from_='whatsapp:+14155238886',
            body="50gm Linear Mangalsutra",
            to='whatsapp:+919167410417'
        )

def message3():
    messages = client.messages \
        .create(
            media_url=['https://staticimg.titan.co.in/Tanishq/Catalog/512515JHEABAP3_1.jpg',
                      'https://staticimg.titan.co.in/Tanishq/Catalog/512515JHFABAP3_1.jpg',
                      'https://staticimg.titan.co.in/Tanishq/Catalog/511418JTSABA00_1.jpg',
                      'https://staticimg.titan.co.in/Tanishq/Catalog/511418JTTABA00_1.jpg',
                      'https://staticimg.titan.co.in/Tanishq/Catalog/511518JCZABA00_1.jpg'],
            from_='whatsapp:+14155238886',
            body="10gm 3 layer Jhumka",
            to='whatsapp:+919167410417'
        )

def message4():
    messages = client.messages \
        .create(
            media_url=['https://staticimg.titan.co.in/Tanishq/Catalog/5138170EZABA00_1.jpg',
                       'https://staticimg.titan.co.in/Tanishq/Catalog/5125152OBABA00_1.jpg',
                       'https://staticimg.titan.co.in/Tanishq/Catalog/5124112HKABA00_1.jpg',
                       'https://staticimg.titan.co.in/Tanishq/Catalog/5123112YOABA00_1.jpg',
                       'https://staticimg.titan.co.in/Tanishq/Catalog/5121132VMABA00_1.jpg'],
            from_='whatsapp:+14155238886',
            body="50gm virasat",
            to='whatsapp:+919167410417'
        )