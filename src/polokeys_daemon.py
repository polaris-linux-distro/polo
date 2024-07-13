#!/usr/bin/python
import zmq
import keyboard
import pcore

def open_terminal():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5555")
    socket.send_string("open_terminal")
    message = socket.recv_string()
    print(f"Received reply: {message}")

def main():
    if pcore.ostype == "svr":
        print("running on server, so nah")
        return
    # Set up the keyboard shortcut
    keyboard.add_hotkey('ctrl+alt+t', open_terminal)

    print("Service running. Press CTRL+ALT+T to open a terminal.")
    keyboard.wait('esc')

if __name__ == '__main__':
    main()
