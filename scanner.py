import logging
import socket
import config

log = logging.getLogger()

def scan_port(ip: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(config.TIME)
    try:
        sock.connect((ip, port))
        log.debug(f'Port: {port} state: open')
        sock.close()
        return True
    except socket.timeout:
        log.debug(f'Port: {port} state: close')
        return False
    except Exception as e:
        log.error(f'Error on check port: {e}')