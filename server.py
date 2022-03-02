import logging
import socket
import threading
import HttpRequest
def process_connect(HttpHandleManage,sock,ip):
    total_msg = ''
    while True:
        msg = sock.recv(1024)
        if len(msg) < 1024:
            total_msg = total_msg + msg.decode()
            break
        total_msg = total_msg + msg.decode()
    if len(total_msg) > 0:
        request = HttpRequest.HttpRequest(sock,total_msg)
        HttpHandleManage.ResponseRequest(request)
class HttpServer:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.HttpHandleManage = None
    def AddHttpHandleManage(self,httphandleManage):
        self.HttpHandleManage = httphandleManage
    def run(self):
        sock = socket.socket()
        sock.bind((self.ip,self.port))
        sock.listen()
        while True:
            clientSock,clientAddr = sock.accept()
            logging.debug(clientAddr)
            t = threading.Thread(target = process_connect,args=(self.HttpHandleManage,clientSock,clientAddr))
            t.start()
