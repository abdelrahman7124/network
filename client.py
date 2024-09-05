import socket as sk

ip='192.168.1.15'
port =12345
addr = (ip,port)
packet_num = 0

client_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

while True:
    print(f"packet number {packet_num}")
    message = input("Enter the message you want to send [enter ""exit"" to exit]")
    sent_message = str(packet_num) + ":" + message
    byte = str(sent_message).encode()
    
    client_socket.sendto(byte,addr)
    if message.lower() == "exit":
        break
    data, server = client_socket.recvfrom(1024)
    received_message = data.decode() 
    
    if received_message.lower() == f"{packet_num}":
        packet_num += 1
        print("sent message to server succesfully")
    elif received_message.lower() == "-2" :
        while received_message.lower() == "-2":
            print ("connection lost trying again")
            client_socket.sendto(byte,addr)
            data, server = client_socket.recvfrom(1024)
            received_message = data.decode()
        print("sent message to server succesfully")
        packet_num += 1
    else:
        print("couldn't send message")
    

client_socket.close()

