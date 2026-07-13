import socket
import os
import time

#HIASQ 
#https://github.com/HIASQ

print("    PS4 ELF PAYLOAD SENDER v0.001     ")

RECEIVER_IP = "192.168.1.1" 
PORT = 9090 


FILE_NAME = "np-fake-signin-ps4.elf" 

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(CURRENT_DIR, FILE_NAME)

def send_elf_file(ip, port, file_path):
    if not os.path.exists(file_path):
        print(f"\n[ERROR] File not found at:\n{file_path}")
        return
        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            print(f"\nConnecting to {ip}:{port}...")
            s.connect((ip, port))
            print("Connected successfully. Sending file...")
            
            with open(file_path, 'rb') as f:
                while chunk := f.read(8192):
                    s.sendall(chunk)
                    time.sleep(0.001) 
                    
            print("File sent successfully!")
            
        except Exception as e:
            print(f"\n[ERROR] Connection failed: {e}")

if __name__ == "__main__":
    send_elf_file(RECEIVER_IP, PORT, FILE_PATH)
