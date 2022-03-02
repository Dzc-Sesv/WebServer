class HttpRequest:
    def __init__(self,sock,source):
        self.sock = sock
        self.originContent = source
        contentList = source.split('\r\n')
        self.requestLine = contentList[0]
        self.method = self.requestLine.split(" ")[0]
        self.url = self.requestLine.split(" ")[1]
    def getMethod(self):
        return self.method
    def getUrl(self):
        return self.url
