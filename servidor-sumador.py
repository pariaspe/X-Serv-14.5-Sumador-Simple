#!/usr/bin/python3
"""
Ejercicio 14.4 Sumador Simple

Pedro Arias Pérez
p.ariaspe @ alumnos.urjc.es
SAT , Universidad Rey Juan Carlos
"""

import socket
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        request = str(recvSocket.recv(2048))
        print(request)
        print('Answering back...')

        # Building Answer
        num = 999999999
        html_answer = '<html><body><h1>Hola. <a href="/' + str(num)
        html_answer += '">Dame otra<a/></body></h1></html>'

        # Answering
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        html_answer + '\r\n', 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
