import socket
import threading
import time
import sys

# Try to import pyautogui, but make it optional for Codespaces
try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except Exception as e:
    PYAUTOGUI_AVAILABLE = False
    print(f"⚠️  PyAutoGUI not available (Codespaces environment detected)")
    print("Running in server mode to receive drawing commands.\n")

class ScribblDrawingBot:
    def __init__(self, mode='server', host='0.0.0.0', port=65432):
        self.mode = mode
        self.host = host
        self.port = port

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen()
            print(f'🎨 Server listening on {self.host}:{self.port}')
            print('Waiting for client connections...\n')
            
            try:
                while True:
                    try:
                        conn, addr = s.accept()
                        print(f'✓ Client connected: {addr}')
                        threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()
                    except KeyboardInterrupt:
                        break
            except Exception as e:
                print(f'Error: {e}')
            finally:
                print('Server stopped.')

    def handle_client(self, conn, addr):
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                command = data.decode('utf-8').strip()
                print(f'Received: {command}')
                
                if PYAUTOGUI_AVAILABLE:
                    self.process_command(command)
                else:
                    print(f'  (Command received and queued)')
                
                conn.sendall(b'OK\n')
        except Exception as e:
            print(f'Error handling client {addr}: {e}')
        finally:
            conn.close()

    def start_client(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                print(f'✓ Connected to server at {self.host}:{self.port}\n')
                print('Enter commands (type "exit" to quit):')
                print('  move_to x y')
                print('  draw_line x1 y1 x2 y2')
                print('  wait seconds\n')
                
                while True:
                    cmd = input('> ')
                    if cmd.lower() == 'exit':
                        break
                    if cmd.strip():
                        s.sendall(cmd.encode('utf-8'))
                        response = s.recv(1024)
                        print(f'  {response.decode("utf-8").strip()}')
        except ConnectionRefusedError:
            print(f'❌ Could not connect to server at {self.host}:{self.port}')
            print('Make sure the server is running first!')
        except Exception as e:
            print(f'Error: {e}')

    def process_command(self, command):
        if not PYAUTOGUI_AVAILABLE:
            return
        
        try:
            parts = command.split()
            cmd_type = parts[0].lower()
            
            if cmd_type == 'move_to':
                x, y = int(parts[1]), int(parts[2])
                pyautogui.moveTo(x, y)
                print(f'  → Moved to ({x}, {y})')
            
            elif cmd_type == 'draw_line':
                x1, y1, x2, y2 = int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])
                pyautogui.moveTo(x1, y1)
                pyautogui.dragTo(x2, y2, duration=0.5)
                print(f'  → Drew line from ({x1}, {y1}) to ({x2}, {y2})')
            
            elif cmd_type == 'wait':
                seconds = int(parts[1])
                time.sleep(seconds)
                print(f'  → Waited {seconds} second(s)')
            
            else:
                print(f'  ❌ Unknown command: {cmd_type}')
        
        except Exception as e:
            print(f'  ❌ Error processing command: {e}')

    def run(self):
        if self.mode == 'server':
            self.start_server()
        elif self.mode == 'client':
            self.start_client()
        else:
            print('Invalid mode. Choose "server" or "client".')

if __name__ == '__main__':
    print('='*50)
    print('Scribbl Drawing Bot')
    print('='*50 + '\n')
    
    mode = input('Enter mode (server/client): ').strip().lower()
    
    if mode not in ['server', 'client']:
        print('Invalid mode. Please choose "server" or "client".')
        sys.exit(1)
    
    bot = ScribblDrawingBot(mode=mode)
    bot.run()
