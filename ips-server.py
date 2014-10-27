import socket, select
import json

import copy, time
def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,'1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])-1
(width, height) = getTerminalSize()
colors = ['\033[95m','\033[94m','\033[92m','\033[93m','\033[91m']
ENDC = '\033[0m'

start = []
counter = -1
for y in range(height):
    start.append([])
    for x in range(width):
        start[-1].append(" ")
start[2][3]="a"
print(colors[0])

if __name__ == "__main__":
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5001
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)

    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)

    while 1:

        time.sleep(0.05)
        #print(chr(27) + "[0;0f")
        counter += 1
        start[7][7]="c"
        printer = copy.deepcopy(start)
        for x in range(len(str(counter))):
           printer[0][-x-1] = str(counter)[-x-1]
        for y in printer:
            for x in y:
                print(x,end="")
                1
            print('')

        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
        for sock in read_sockets:
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print("Client (%s, %s) connected" % addr)
            
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        try:
                            data=eval(data)
                            print(data)
                            #print (str(data["ID"])+": "+str(data["det"]))
                            #start[1][data["ID"]]=len(data["det"])
                        except:
                            print(":O", data)
                            1
                except:
                    #print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
    
    server_socket.close()
print(ENDC)
