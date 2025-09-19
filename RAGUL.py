from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    
    <head>
        <title>Ragul-25014743</title>
    </head>    
        <body >
         <center>
           <h1> Device specifications -25014743</h1>
     
        <hr size="10" color="black">
            <table border="5" cellspacing="10" cellpadding="10" >
                <tr >
                    <td bgcolor="red">devicename </td>
                    <td bgcolor="red">Proccessor</td>
                    <td bgcolor="red">ram</td>
                </tr>

                <tr>
                    <td>DESKTOP-KI9BIF3</td>
                    <td>AMD Ryzen 5 5600H with Radeon Graphics </td>
                    <td>8.00 GB (7.34 GB usable)</td>
                </tr>
            </table> 
               </center>
            <hr size="10" color="black">      
        </body>
    
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()