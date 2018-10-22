#!/usr/bin/env python3
import os, socket, sys, signal


def process_input(socket_object):
    answ = ""
    part_of_answer = socket_object.recv(4096)
    while part_of_answer:
        answ += part_of_answer.decode("UTF-8")
        part_of_answer = socket_object.recv(4096)
    print("Child - received data: {}".format(answ))
    socket_object.close()
    return


def letsdoit():
    fname, fext = os.path.splitext(os.path.basename(__file__))
    SOCKET_FILE = "/tmp/" + fname + ".sock"
    if os.path.exists(SOCKET_FILE):
        try:
            os.remove(SOCKET_FILE)
        except IOError as err:
            print("I/O Error: {}".format(err))
            sys.exit(1)

    srvsock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    srvsock.bind(SOCKET_FILE)
    srvsock.listen(0)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        socket_object, address_info = srvsock.accept()
        subp = os.fork()
        if subp < 0:
            print("fork hiba")
            sys.exit(1)

        if subp == 0:  # Child process
            srvsock.close()
            print("Child process, socket: {}".format(socket_object))
            process_input(socket_object)
            os._exit(0)

        else:  # Parent process
            socket_object.close()
            # Ez értelmetlenné teszi a fork() használatát, mivel amíg nem áll le a gyerek processz,
            # addig itt vár a szülő. Viszont ha ezt kihagyom, akkor amint leáll a gyerek, átmegy zombiba
            # alias defunct process...
            #pid, stat = os.wait()
            #print("Parent process wait pid:{}, stat:{}".format(pid,stat))

            # kivéve, ha a fork előtt lefut egy
            # signal.signal(signal.SIGCHLD, signal.SIG_IGN)
            #

if __name__ == "__main__":
    letsdoit()
    sys.exit(0)
