#!/usr/bin/python
# This script is quite simple. It simply recreates the CTRL-ALT-T functionality from Ubuntu.

import subprocess
import pcore
import zmq

def terminal():
    subprocess.Popen([pcore.terminal])

def main():
    if pcore.ostype == "svr":
        print("running on server, so nah")
        return
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5555")
    
    while True:
        message = socket.recv_string()
        if message == "open_terminal":
            terminal()
            socket.send_string("terminal_opened")

if __name__ == '__main__':
    main()
