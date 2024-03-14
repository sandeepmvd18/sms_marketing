from twilio.rest import Client

# Twilio credentials
account_sid = 'ACc8d42355377ff1c025a2ec4e99cae1fd'
auth_token = '6bd3ce9bded4f68b970a38926455edaa'
twilio_number = '+18509722162'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Message to be sent
message_body = """Dear Customer,

Discover a world of exceptional service at Sri Vijaya Motors, located at Bethamangala Rd, Kolar Gold Fields, Karnataka 563116, India. From top-notch maintenance to expert guidance, we're here to elevate your experience. Visit us today to explore our range of services and products.

- Sri Vijaya Motors"""

# List of numbers to send messages to
numbers = ['+919449668894','+919686450179','+919449749697','+919844811299']  # Add your numbers here

# Send messages
for number in numbers:
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to=number
    )

    print("Message sent to", number)
