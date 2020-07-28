from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply
from whatsapp import message1
from whatsapp import message2
from whatsapp import message3
from whatsapp import message4

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = fetch_reply(msg, phone_no)
    if reply==str(1):
        [message1() for _ in range(5)] 
    elif reply==str(2):
        [message2() for _ in range(5)] 
    elif reply==str(3):
        [message3() for _ in range(5)] 
    elif reply==str(4):
        [message4() for _ in range(5)] 
    else:
        # Create reply
        resp = MessagingResponse()
        resp.message(reply)
        
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
