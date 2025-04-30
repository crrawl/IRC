import socket
import threading

class IRCClient:
    def __init__(self, host="127.0.0.1", port=6667, nickname="Guest"):
        self.host = host
        self.port = port
        self.nickname = nickname
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                if message:
                    print(message)
            except:
                print("Disconnected from server")
                self.client_socket.close()
                break

    def send_messages(self):
        while True:
            message = input()
            if message.lower() == '/quit':
                self.client_socket.close()
                break
            self.client_socket.send(f"{self.nickname}: {message}".encode("utf-8"))

    def start(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to IRC server at {self.host}:{self.port}")
            threading.Thread(target=self.receive_messages).start()
            self.send_messages()
        except Exception as e:
            print(f"Failed to connect: {e}")
            self.client_socket.close()

if __name__ == "__main__":
    nickname = input("Enter your nickname: ")
    client = IRCClient(nickname=nickname)
    client.start()