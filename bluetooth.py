import socket
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./chatterbot-corpus-master/chatterbot_corpus/data/english/")



server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("64:6e:e0:ee:2a:45" , 4))
server.listen(1)
client, addr = server.accept()





try:
    while True:
        message = input("Enter message: ")
        client.send(message.encode ("utf-8"))
        data = client.recv(1024)
        if not data: 
            break
    print(f"Message: {data.decode('utf-8')}")

except OSError as e:
    pass



# chatBot
while True:
    message = input("Enter message:")

    respose = chatbot.get_response(f"{message}")
    print(respose)

