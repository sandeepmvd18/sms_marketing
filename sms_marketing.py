from twilio.rest import Client

account_sid = '{accountsid_no}'
auth_token = '{token_num}'
twilio_number = '+{generated_num}'

client = Client(account_sid, auth_token)

message_body = """Dear Customer,

Discover a world of exceptional service at Sri Vijaya Motors, located at Bethamangala Rd, Kolar Gold Fields, Karnataka 563116, India. From top-notch maintenance to expert guidance, we're here to elevate your experience. Visit us today to explore our range of services and products.

- Sri Vijaya Motors"""

numbers = ['number of our choice']  # Add your numbers here

for number in numbers:
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to=number
    )

    print("Message sent to", number)
