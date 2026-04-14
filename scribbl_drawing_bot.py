import socket
import pyautogui
import threading
import time

class ScribblDrawingBot:
    def __init__(self, mode='server', host='127.0.0.1', port=65432):
        self.mode = mode
        self.host = host
        self.port = port

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print('Server listening on {}:{}'.format(self.host, self.port))
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    self.process_command(data.decode('utf-8'))

    def start_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            while True:
                cmd = input('Enter drawing command: ')
                if cmd.lower() == 'exit':
                    break
                s.sendall(cmd.encode('utf-8'))

    def process_command(self, command):
        if command.startswith('move_to'):
            _, x, y = command.split()
            pyautogui.moveTo(int(x), int(y))
        elif command.startswith('draw_line'):
            _, x1, y1, x2, y2 = command.split()
            pyautogui.moveTo(int(x1), int(y1))
            pyautogui.dragTo(int(x2), int(y2), duration=0.5)
        elif command.startswith('wait'):
            _, seconds = command.split()
            time.sleep(int(seconds))
        else:
            print('Unknown command:', command)

    def run(self):
        if self.mode == 'server':
            self.start_server()
        elif self.mode == 'client':
            self.start_client()

if __name__ == '__main__':
    mode = input('Enter mode (server/client): ').strip().lower()
    bot = ScribblDrawingBot(mode=mode)
    bot.run()