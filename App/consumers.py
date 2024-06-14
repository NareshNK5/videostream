# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ControlConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.channel_layer.group_add(
#             'control_group',
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             'control_group',
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         command = text_data_json['command']
#         await self.channel_layer.group_send(
#             'control_group',
#             {
#                 'type': 'control_message',
#                 'command': command
#             }
#         )

#     async def control_message(self, event):
#         command = event['command']
#         await self.send(text_data=json.dumps({
#             'command': command
#         }))


from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class demo(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("connect")
        await self.accept()
    
    async def disconnect(self , close_code):
        print("disconnect",close_code)
    
    async def receive(self,text_date):
        text_data_json = json.loads(text_date)
        msg = text_data_json["message"]
        sender = text_data_json["sender"]
        print(msg,sender)
        
        await self.send(text_data=json.dump({
            'message':msg,
            'sender':sender
        }))