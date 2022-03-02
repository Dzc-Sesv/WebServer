import server
import HttpHandleManage
def fun(request):
    return "hello world"
if __name__ == "__main__":
    httphandleManage = HttpHandleManage.HttpHandleManage()
    httphandleManage.AddRoute("GET",'/index',fun)
    server = server.HttpServer("127.0.0.1",12345)
    server.AddHttpHandleManage(httphandleManage)
    server.run()