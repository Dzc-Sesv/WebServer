class HttpResponse:
    def __init__(self,sock):
        self.sock = sock
        self.responseLine = "HTTP/1.1"
        self.status = "200"
        self.responseHead = {}
        self.responseBody = ''
    def setResponseLine(self,content):
        self.responseLine = content
    def setResponseHead(self,key,value):
        self.responseHead[key] = value
    def setResponseBody(self,body):
        self.responseBody = body
    def setResponseStatus(self,status):
        self.status = status
    def Response(self):
        response = self.responseLine + " " + self.status
        response += "\r\n"
        for (key,item) in self.responseHead.items():
            response += key + ":" + item
            response += "\r\n"
        response += "\n"
        response += self.responseBody
        self.sock.send(response.encode())
        self.sock.close()
