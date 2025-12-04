import random
import socket
import threading
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Chatbot
chatbot = ChatBot('Ron Obvious')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./chatterbot-corpus-master/chatterbot_corpus/data/english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
SERVER_IP = "172.17.215.200"  # <-- replace with your server LAN IP
SERVER_PORT = 9999

# Bind client socket to a random port
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("",random.randint(8000,9000)))




def receive(): 
    print("Starting receiver")
    while True:
        try:
            print("hi")
            message, _ = client.recvfrom(1024)
            print(message.decode())
            bot_response = chatbot.get_response(f"{message}")
            client.sendto(f"Chatboy: {bot_response}".encode(), (SERVER_IP, SERVER_PORT))
        except Exception as e: 
            print("Error receiving:", e)

# Start receiver thread
t = threading.Thread(target=receive, daemon=True)
t.start()

while True:
    pass

