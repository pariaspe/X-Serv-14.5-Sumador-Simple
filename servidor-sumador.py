#!/usr/bin/python3
"""
Ejercicio 14.4 Sumador Simple

Pedro Arias Pérez
p.ariaspe @ alumnos.urjc.es
SAT , Universidad Rey Juan Carlos
"""

import socket
import calculadora

def analize(request):
    resource = request.split()[1]
    print(resource)
    _, num1, operacion, num2 = resource.split('/')
    return num1, operacion, num2

def compute(num1, operacion, num2):
    op = num1 + " " + operacion + " " + num2 + " = "
    op += str(calculadora.operations[operacion](int(num1), int(num2)))
    return op

def build_answer(op):
    html_answer = '<html><body><h1>Bienvenido a la calculadora web.</h1>'
    html_answer += '<p>La operacion a realizar es:\r\t' + op
    html_answer += '</p></body>'

    answer = "HTTP/1.1 200 OK\r\n\r\n" + html_answer + '\r\n'
    return answer

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('0.0.0.0', 1234))

mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        request = str(recvSocket.recv(1024), 'utf-8')
        print(request)
<<<<<<< HEAD

        num1, operacion, num2 = analize(request)
        print('Answering back...')

        # Building Answer
        try:
            op = compute(num1, operacion, num2)
        except KeyError:
            op = "Operacion no permitida(" + operacion + ")"
        except ZeroDivisionError:
            op = "No se puede dividir entre zero."
        except:
            op = "Error"

        answer = build_answer(op)
=======
        resource = request.split()[1]
        print(resource)
        param = resource.split('/')
        if len(param) != calculadora.NUM_ARGS:
            html_answer = '<html><body><h1>Bienvenido a la calculadora web.</h1>'
            html_answer += '<p>Usage error</p></body>'
        else:
            _, num1, operacion, num2 = resource.split('/')
            print('Answering back...')

            # Building Answer
            try:
                op = num1 + " " + operacion + " " + num2 + " = "
                op += str(calculadora.operations[operacion](int(num1), int(num2)))
            except KeyError:
                op = "Operacion no permitida(" + operacion + ")"
            except ZeroDivisionError:
                op = "No se puede dividir entre zero."
            except:
                op = "Error"

            html_answer = '<html><body><h1>Bienvenido a la calculadora web.</h1>'
            html_answer += '<p>La operacion a realizar es:\r\t' + op
            html_answer += '</p></body>'

>>>>>>> c7ea541790880b38aa6c2e05b86d60f051adb5fe
        # Answering
        recvSocket.send(bytes(answer, 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
