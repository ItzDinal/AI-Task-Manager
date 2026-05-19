import socket

s = socket.socket()
s.settimeout(5)
try:
    s.connect(('127.0.0.1', 8000))
    print('connected')
except Exception as exc:
    print('failed', exc)
finally:
    s.close()
