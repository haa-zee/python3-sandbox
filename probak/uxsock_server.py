#!/usr/bin/env python3
import os, socket, sys, signal


def process_input(socket_object):
    answ = ""
    part_of_answer = socket_object.recv(512)
    # ## *** törölve *** ---!!! ez itt valamiért nem működik, nem lép ki, ha 0 hosszúságú adatot küld a kliens,
    # ## *** törölve *** és akkor sem, ha üres stringet, hiába próbálkoztam a különböző variációkkal a feltételekben.
    # Valójában arról van szó, hogy a kliensnek kell lezárnia a saját oldalán close()-zal a
    # socketet, ekkor kap a szerveroldali recv() egy nulla hosszúságú választ.
    # DE! Ha kétirányú a kommunikáció, akkor a kliensnek is ki kell olvasni a szerver által
    # küldött adatokat a socket-ről, mielőtt lezárja, különben a szerver oldalon jön egy
    # hiba (connection reset by peer vagy valami hasonló). Ha rendesen kiolvassa mindkét oldal
    # a nekik szóló üzeneteket és így zárja a kliens a socketet, akkor nincs gond.
    # Nézd meg a socket.shutdown-t is!!
    #

    while part_of_answer != b"":
        print(".  {} {}".format(len(part_of_answer), type(part_of_answer)))
        answ += part_of_answer.decode("UTF-8")
        print("x: {:02x}".format(part_of_answer[-1]))
        if part_of_answer[-1] == 10:
            print("Child - received data: {}".format(answ))
            socket_object.send(b"Good bye")
            answ = ""
        part_of_answer = socket_object.recv(512)
    socket_object.close()
    print("Konyec")
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
        pid = os.fork()

        if pid == 0:  # Child process
            srvsock.close()
            print("Child process, socket: {}".format(socket_object))
            process_input(socket_object)
            os._exit(0)

        else:  # Parent process
            socket_object.close()
            # Ez értelmetlenné teszi a fork() használatát, mivel amíg nem áll le a gyerek processz,
            # addig itt vár a szülő. Viszont ha ezt kihagyom, akkor amint leáll a gyerek, átmegy zombiba
            # alias defunct process...
            # pid, stat = os.wait()
            # print("Parent process wait pid:{}, stat:{}".format(pid,stat))

            # kivéve, ha a fork előtt lefut egy
            # signal.signal(signal.SIGCHLD, signal.SIG_IGN)
            #


if __name__ == "__main__":
    letsdoit()
    sys.exit(0)
