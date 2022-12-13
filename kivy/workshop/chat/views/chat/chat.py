from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder
import pprint
import ast
import threading
Builder.load_file('./views/chat/chat.kv')


class Chat(Screen):

    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.username = None
        self.total_user = []

    def on_text(self, instance: TextInput, text: str):
        self.send_message(instance.text, self.ids.chat_list,
                          self.ids.chat_input)

    def on_enter(self, *args):
        self.controller.client.initial_client()
        self.username = self.controller.client.name
        threading.Thread(target=self.receive_message_thread).start()
        return super().on_enter(*args)

    def send_message(self, text: str, rv: RecycleView, instance: TextInput):
        rv.data.append({'message_text': '[color=#000000]{}[/color]'.format(text),
                       'height': 50, 'mode': 'sender'})
        self.controller.client.send(
            str({'message': text, 'username': self.username}))
        instance.text = ""

    def receive_message(self, message: str, username: str):
        received_message = '[color=#16A085]{}[/color] [color=#000000]--> {}[/color]'.format(
            username, message)
        self.ids.chat_list.data.append(
            {'message_text': received_message, 'height': 50, 'mode': 'receiver'})

    def add_new_member(self, message: str):
        new_member = '[color=#C0392B]{}[/color] [color=#000000]--> is join[/color]'.format(
            message)
        self.ids.chat_list.data.append(
            {'message_text': new_member, 'height': 50, 'mode': 'new_member'})

    def receive_message_thread(self):
        while True:
            message: dict = ast.literal_eval(self.controller.client.recv())
            if("total_user" in list(message.keys())):
                for i in message["total_user"]:
                    if (i != self.username):
                        self.add_new_member(i)
            elif("message" in list(message.keys()) and message["username"] != self.username and message["username"] not in self.total_user):
                self.total_user.append(message["username"])
                self.receive_message(message["message"], message["username"])
            print(self.total_user)
