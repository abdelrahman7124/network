import socket as sk
import random

host = sk.gethostbyname(sk.gethostname())
port = 12345

packet_num = 0

server_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
server_socket.bind((host, port))
    
    
while True:
    data, addr = server_socket.recvfrom(1024) 
    message = data.decode()
    received_packet_num , received_message = message.split(":")
    if received_message.lower() == "exit":
        print ("Client disconnected")
        break  
    if received_packet_num == str(packet_num):
        if random.random() > 0.5 : 
            byte = f"{packet_num}".encode()
            server_socket.sendto(byte,addr)
            packet_num +=1
            print(f"Received {received_message} from {addr}")
        else :
            server_socket.sendto("-2".encode(),addr)
            print ("Message interrupted due to connection drop trying again")
            
    else :
        server_socket.sendto("-1".encode(),addr)
        print ("Message interrupted due to package loss")
    
server_socket.close()