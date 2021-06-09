import socket

def scan_port(ip,port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.5)
  try:
     connect = sock.connect((ip,port))
     print('Port:',port,'open.')
     sock.close()
  except:
     print('Port:', port, 'close.')
     pass

ip = '192.168.1.155'
for i in range(135,140):
  scan_port(ip,i)








