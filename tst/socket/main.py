#
# @section License
#
# The MIT License (MIT)
# 
# Copyright (c) 2016, Erik Moqvist
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# This file is part of the Pumbaa project.
#


import select
import socket
import harness
from harness import assert_raises


def test_print():
    print(socket)


def test_tcp_client():
    client = socket.socket()
    client.connect(("192.168.1.101", 80))
    assert client.send(b'foo') == 3
    assert client.recv(3) == b'bar'
    client.close()


def test_tcp_server():
    listener = socket.socket()
    listener.bind(("192.168.1.102", 8080))
    listener.listen(5)
    listener.accept()
    listener.close()


def test_udp():
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def test_select():
    poll = select.poll()
    tcp = socket.socket()

    # Register both event channels.
    poll.register(tcp)

    # Timeout waiting for data on the socket.
    assert poll.poll(0.01) == []

    tcp.close()


def test_bad_arguments():
    # Bad socket family.
    with assert_raises(OSError):
        socket.socket(-1)

        # Bad socket type.
    with assert_raises(OSError):
        socket.socket(socket.AF_INET, -1)


def main():
    testcases = [
        (test_print, "test_print"),
        (test_tcp_client, "test_tcp_client"),
        (test_tcp_server, "test_tcp_server"),
        (test_udp, "test_udp"),
        (test_select, "test_select"),
        (test_bad_arguments, "test_bad_arguments")
    ]
    harness.run(testcases)


if __name__ == '__main__':
    main()
