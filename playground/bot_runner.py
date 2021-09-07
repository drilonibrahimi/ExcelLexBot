import boto3
import json

client = boto3.client('lex-runtime', region_name='eu-central-1')

response = client.post_text(
    botName='ScheduleAppointmentBot',
    botAlias='$LATEST',
    userId='UserOne',
    inputText='book a hotel')

print(json.dumps(response, indent=4))
