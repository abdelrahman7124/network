import socket as sk
host = sk.gethostbyname(sk.gethostname())
port = 12345

server_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
server_socket.bind((host, port))
    
print(f"Server started on {host}:{port}, waiting for messages...")
    
while True:
    data, addr = server_socket.recvfrom(1024) 
    received_message = data.decode() 
    print(f"Received message: {received_message} from {addr}")
    if received_message == "exit":
        break
    response = "Message received"
    byte_response = response.encode() 
    server_socket.sendto(byte_response, addr)
    
server_socket.close()