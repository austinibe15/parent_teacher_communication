from channels.generic.websocket import AsyncWebsocketConsumer  
import json  

class MessageConsumer(AsyncWebsocketConsumer):  
    async def connect(self):  
        self.room_name = 'messages'  
        self.room_group_name = 'message_%s' % self.room_name  

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)  
        await self.accept()  

    async def disconnect(self, close_code):  
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)  

    async def receive(self, text_data):  
        try:  
            text_data_json = json.loads(text_data)  
            message = text_data_json.get('message')  
            if message:  
                await self.channel_layer.group_send(  
                    self.room_group_name,  
                    {  
                        'type': 'send_message',  
                        'message': message  
                    }  
                )  
        except json.JSONDecodeError:  
            await self.send(text_data=json.dumps({'error': 'Invalid JSON received'}))  

    async def send_message(self, event):  
        message = event['message']  
        await self.send(text_data=json.dumps({'message': message}))  


class ParentConsumer(AsyncWebsocketConsumer):  
    async def connect(self):  
        self.room_name = 'parents'  
        self.room_group_name = 'parent_%s' % self.room_name  

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)  
        await self.accept()  

    async def disconnect(self, close_code):  
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)  

    async def receive(self, text_data):  
        text_data_json = json.loads(text_data)  
        message = text_data_json.get('message')  
        await self.channel_layer.group_send(  
            self.room_group_name,  
            {  
                'type': 'send_message',  
                'message': message  
            }  
        )  

    async def send_message(self, event):  
        message = event['message']  
        await self.send(text_data=json.dumps({'message': message}))  


class TeacherConsumer(AsyncWebsocketConsumer):  
    async def connect(self):  
        self.room_name = 'teachers'  
        self.room_group_name = 'teacher_%s' % self.room_name  

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)  
        await self.accept()  

    async def disconnect(self, close_code):  
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)  

    async def receive(self, text_data):  
        text_data_json = json.loads(text_data)  
        message = text_data_json.get('message')  
        await self.channel_layer.group_send(  
            self.room_group_name,  
            {  
                'type': 'send_message',  
                'message': message  
            }  
        )  

    async def send_message(self, event):  
        message = event['message']  
        await self.send(text_data=json.dumps({'message': message}))