import socket as sk

ip='192.168.1.15'
port =12345

client_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
while True:
    message = input("Enter the message you want to send [enter ""exit"" to exit]")
    byte_message = message.encode()  
    client_socket.sendto(byte_message, (ip, port))
    if message == "exit":
        break
    data, server = client_socket.recvfrom(1024)
    received_message = data.decode() 
    print(f"Received message from server: {received_message}")
    

client_socket.close()