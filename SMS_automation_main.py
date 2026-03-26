import pandas as pd
from twilio.rest import Client

acc_SID = "Your SID number"
auth_token = "Your auth_token"

client = Client(acc_SID, auth_token)
df = pd.read_excel("data.xlsx")

for i in range(len(df)):
    name = df.loc[i, "Name"]
    designation = df.loc[i, "Designation"]
    number = str(df.loc[i, "Number"])

    number = "+91" + number
    messages = {
        'staff': "Good morning sir",
        'friend': "hey bro...how are you",
        'student': "hello..whats up?",
        'gf': "hey buddy..how are you?"
    }

    msg = messages.get(designation.lower(), "Hello!!")
    final_message = f"Dear {name}, {msg}"

    client.messages.create(
        from_='whatsapp:+14155238886',
        body=final_message,
        to=f'whatsapp:{number}'
    )

    print(f"Message sent to {name} - {number}")