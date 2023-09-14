import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 1773))
sock.listen(5)

trunk = ''
trunk_length = 0
while True:
    message = ''
    connection, address = sock.accept()
    message = connection.recv(260)
    if not message or len(message) < 4: # 4 = get/put + \n
        connection.close()
        continue
    start = message[:3] # get/put
    if start.decode('utf8') == 'PUT':
        trunk_length = message[3]
        if len(message) != 5 + trunk_length: # 5 = 3 + len + 1
            connection.send(bytes('1\n', encoding='utf8'))
            connection.close()
            continue
        connection.send(bytes('0\n', encoding='utf8'))
        trunk = message[4:] # message + \n
    elif start.decode('utf8') == 'GET':
        bytes_send = 0
        len_bytes_send = connection.send(bytes(str(trunk_length), encoding='utf8'))
        if len_bytes_send == 0:
            connection.close()
            continue
        while bytes_send < len(trunk):
            try:
                bytes_send_in_iter = connection.send(bytes(trunk[bytes_send:]))
                bytes_send += bytes_send_in_iter
            except:
                break
    connection.close()
