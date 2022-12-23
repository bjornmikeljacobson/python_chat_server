import socket

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local host and port
server_socket.bind(('localhost', 8000))

# Set the socket to listen for incoming connections
server_socket.listen()

# Accept incoming connections
client_socket, client_address = server_socket.accept()

# Receive data from the client
data = client_socket.recv(1024)

# Send data back to the client
client_socket.sendall(data)

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
