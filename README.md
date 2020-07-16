# TCP-py
Simple TCP networking tools written in Python 2

### client_tcp.py
TCP client that sends and receives data

*Note: Modify target host to send data to before using*

### server_tcp.py
Simple TCP server

### proxy_tcp.py
Standard TCP proxy, acts as intermediary between client and destination server

**Usage**: ./proxy_tcp.py [localhost] [localport] [remote host] [remoteport] [receive_first]

**Example**: ./proxy_tcp.py 127.0.0.1 9000 10.10.10.1 9000 True
