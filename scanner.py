import socket


def scan_port(ip: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        print('Port:', port, 'state: open')
        sock.close()
        return True
    except:
        print('Port:', port, 'state: close')
        return False


ip = '192.168.1.155'
for i in range(135, 140):
    scan_port(ip, i)
