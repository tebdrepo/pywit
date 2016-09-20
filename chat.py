from wit import Wit

def send(request, response):
    print('Sending to user...', response['text'])
def my_action(request):
    print('Received from user...', request['text'])

actions = {
    'send': send,
    'my_action': my_action,
}

client = Wit(access_token='HRJQ463G7R25U43RRXMVIFXKQNQ5XZK7', actions=actions)

my_action
send
