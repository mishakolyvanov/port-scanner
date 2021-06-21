import logging
import socket
import config

log = logging.getLogger()


class BadIpError(Exception):
    pass


def scan_port(ip: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(config.TIME)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            log.debug(f'Port: {port} state: open')
            return True
        else:
            log.debug(f'Port: {port} state: close')
            sock.close()
            return False
    except socket.gaierror:
        log.debug(f'Не првильный ip {ip}')
        raise BadIpError
    except Exception as e:
        log.error(f'Error on check port: {e}')
        raise
