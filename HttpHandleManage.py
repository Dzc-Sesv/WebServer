import HttpResponse
class HttpHandleManage:
    def __init__(self):
        self.mapToHandle = {}
    def ResponseRequest(self,request):
        method = request.getMethod()
        url = request.getUrl()
        response = HttpResponse.HttpResponse(request.sock)
        if method not in self.mapToHandle.keys() or len(self.mapToHandle[method]) == 0 or url not in self.mapToHandle[method].keys():
            response_body = self.DefaultMethod(request)
            response.setResponseStatus("404")
        else:
            try:
                response_body = self.mapToHandle[method][url](request)
            except:
                response.setResponseStatus("404")
        response.setResponseBody(response_body)
        response.Response()
    def AddRoute(self,method,url,handle):
        self.mapToHandle[method] = {url:handle}
    def DefaultMethod(self,request):
        return ""