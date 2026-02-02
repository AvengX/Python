class User:
    def __init__(self, username):
        self.username = username

    def send_message(self, chatroom, content):
        message = Message(self.username, content)
        chatroom.add_message(message)

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"[{self.sender}]: {self.content}"
    
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.history = []

    def join_user(self, user):
        self.users.append(user)
        print(f"{user.username} joined {self.room_name}")

    def leave_user(self, user):
        if user in self.users:  
            self.users.remove(user)
            print(f"{user.username} left {self.room_name}")

    def add_message(self, message):
        self.history.append(message)

    def view_history(self):
        print(f"\n--- {self.room_name} Chat History ---")
        for msg in self.history:
            print(msg)

# Testing the Chat System
room = ChatRoom("Python Devs")
user1 = User("Ayush")
user2 = User("Rahul")

room.join_user(user1)
room.join_user(user2)

user1.send_message(room, "Hello everyone!")
user2.send_message(room, "Hi Ayush, how is the assignment going?")
user1.send_message(room, "Almost done!")

room.view_history()
room.leave_user(user2)