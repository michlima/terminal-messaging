# 🖥️ Terminal Messaging - UDP Chatbot with AI Integration

*Terminal Messaging* is a multi-client, multi-server UDP-based chatbot system enhanced with *OpenAI ChatGPT AI*. This project allows clients to communicate seamlessly across servers, run AI-powered chatbots, and utilize terminal commands for advanced networking features.

## Contributors (Developers)
- Michael Lima (https://github.com/michlima)
-  Yusif Malikov (https://github.com/YusifMalikov)
-  Dimitri Kovzanadze (https://github.com/dimakovz)
---

## 🌐 Features

| Feature                                     | Description                                                                                                                                  |
| ------------------------------------------- | ------------------------------------------------------------------
| *OpenAI Integration*                      | Any device with the this application can run a AI client presuming they have an api-key from open-ai and implement it in the robot.py file. After writing the key the user can start the robot client and listen to to chat server he wants the AI to participate in.                      |
| *Quit Chat ⁠ !q ⁠*                          | Safely exit the chat. Sends a “left the chat” message to the server before closing the client.                                               |
| *Ping Command ⁠ /ping <ip> ⁠*               | Check if a specific IP is reachable via ICMP ping. Runs locally and does not broadcast messages to the server.                               |
| *Join Another Server ⁠ /join <server_ip> ⁠* | Switch to a different server by updating the destination IP. Server sends a “JOINED THE SERVER” notification to the clients.                     |

---

## 🛠️ Terminal Commands

| Command             | Usage               | Description                                                                |
| ------------------- | ------------------- | -------------------------------------------------------------------------- |
| ⁠ !q ⁠                | ⁠ !q ⁠                | Exit the chat safely. Sends a notification to the server.                  |
| ⁠ /ping <ip> ⁠        | ⁠ /ping 192.168.0.1 ⁠ | Ping a specific IP locally to check reachability.                          |
| ⁠ /join <server_ip> ⁠ | ⁠ /join 192.168.0.2 ⁠ | Switch to a different server and notify the new server about your arrival. |

---

## 🤖 AI Integration

Any device can run ⁠ robot.py ⁠ to handle AI responses:

•⁠  ⁠The AI acts as a chat participant (client).
•⁠  ⁠Clients can send messages to server, ai listens for code '/ai'. Once '/ai' is located the AI give it's requested input.
•⁠  ⁠AI sends message to server who distributes message to all clients connected.

---

## 📡 Demo Topology

The following diagram illustrates the network setup used in our class demo:

![ChatGPT Image Dec 16, 2025, 01\_03\_22 PM](https://github.com/user-attachments/assets/5b68f702-c6d7-409c-a2cb-fecd0b6700ca)

•⁠  ⁠*IP Assignments:* Same as class demo.
•⁠  ⁠*Network Flow:* Clients can chat, run ⁠ /ping ⁠, or switch servers with ⁠ /join ⁠. AI responses are handled by ⁠ robot.py ⁠ running on devices with key who connect AI to servers.

---

## 🚀 Getting Started

1.⁠ ⁠*Run a server:*

   ⁠ bash
   python server.py
    ⁠
2.⁠ ⁠*Start a client:*

   ⁠ bash
   python client.py
    ⁠
3.⁠ ⁠*Optional:* Start AI on the server:

   ⁠ bash
   python robot.py
    ⁠
4.⁠ ⁠*Use commands in the client:*

   * Quit: ⁠ !q ⁠
   * Ping: ⁠ /ping <ip> ⁠
   * Join server: ⁠ /join <server_ip> ⁠

THANK YOU FOR YOUR ATTENTION AND ENJOY!
