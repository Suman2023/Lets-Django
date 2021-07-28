import json
from django.contrib.auth import get_user_model
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message, Room

User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    # converted the received object from database to json compatible
    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'author': message.author.username,
            'content': message.content,
            'timeStamp': str(message.timeStamp),
            # 'group_admin': message.group__group_admin.username,
            # 'group_name': message.group__group_name
        }

    #getting messsages from database
    def fetch_messages(self, data):
        messages = Message.last_10_messages(
            data['room_name'],
            data['group_admin'],
        )

        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    # save to db when someone sends a message
    def new_message(self, data):
        author = data['from']
        group_admin_username = data['group_admin']
        author_user = User.objects.filter(username=author)[0]
        group_name = data['room_name']
        group_admin = User.objects.filter(username=group_admin_username)[0]

        group = Room.objects.filter(group_name=group_name)[0]
        message = Message.objects.create(
            group=group,
            author=author_user,
            content=data['message'],
        )
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',  #call this when u receive
                'message': message,  #this is the event
            })

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
