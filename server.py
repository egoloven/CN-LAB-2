# # first of all import the socket library 
# import socket                
  
# # next create a socket object 
# s = socket.socket()          
# print("Socket successfully created")
  
# # reserve a port on your computer in our 
# # case it is 12345 but it can be anything 
# port = 12345                
  
# # Next bind to the port 
# # we have not typed any ip in the ip field 
# # instead we have inputted an empty string 
# # this makes the server listen to requests  
# # coming from other computers on the network 
# s.bind(('', port))         
# print("socket binded to %s" %(port))
  
# # put the socket into listening mode 
# s.listen(5)      
# print("socket is listening")            
  
# # a forever loop until we interrupt it or  
# # an error occurs 
# while True: 
# # Establish connection with client. 
# 	c, addr = s.accept()      
# 	print('Got connection from', addr) 
# 	# send a thank you message to the client.  
# 	temp = 'Thank you for connecting'
# 	c.send(temp.encode()) 

# 	# c.send('Write a word to translate')

# 	data = c.recv(1024)
# 	if not data:
# 		break
# 	print(data)
# 	c.send(data.upper())
# 	# Close the connection with the client 


import socket
import threading
import time


address_to_server = ('localhost', 1235)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address_to_server)



LOG = ""
USERID = ""

LOG += str(time.ctime(time.time())) + f"I connected to the server\n"

def listen_server():
	global LOG
	global USERID
	while True:
		try:
			data = client.recv(1024)
			answer = data.decode()
			if answer == "end" :
				client.close()
				print("Server stoped responding")
				LOG += str(time.ctime(time.time())) + f"Server stoped responding\n"
				break
			if "Hello user" in answer:
				USERID = answer.split(" ")[2]
			LOG += str(time.ctime(time.time())) + f"Server send me {answer}\n"
			print(str(answer))
		except OSError:
			client.close()
			print("disconected")
			break

listener = threading.Thread(target=listen_server)
listener.start()

while True:
	try:
		print(">", end="")
		n = input()
		LOG += str(time.ctime(time.time())) + f"I send {n} to server\n"
		client.send(bytes(n, encoding="UTF-8"))
		if n == "end":
			break
		time.sleep(0.1)
	except OSError:
		break

with open(f"clientlogs{USERID}.txt", "w+") as file:
			file.write(LOG)
client.close()
	