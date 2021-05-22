#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# multiPrcsgCCrouzet.py  by  christophercrouzet
# 
# copied from web and modified for study @author Joe Jackson 


import logging
import multiprocessing

# import multiprocessing
print("Number of cpu : ", multiprocessing.cpu_count()) 


_LOGGER = multiprocessing.log_to_stderr()
_LOGGER.setLevel(logging.DEBUG)


_USE_QUEUE = True
_ITERATIONS_MAX = 100


class State(object):
    def __init__(self):
        self.number = 0
        self.letter = ''
        self.seq = []

    def __str__(self):
        return ("State(number=%d, letter=%s, seq=%s, "
                % (self.number, self.letter, self.seq))


def main():
    if _USE_QUEUE:
        queue = multiprocessing.Queue()
        args = (queue, queue)
    else:
        pipe = multiprocessing.Pipe(duplex=False)
        args = (pipe[1], pipe[0])

    processes = (
        multiprocessing.Process(
            target=_producer,
            name='producer',
            args=(args[0],)
        ),
        multiprocessing.Process(
            target=_consumer,
            name='consumer',
            args=(args[1],)
        )
    )

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    _LOGGER.debug("exiting main")


def _producer(conn):
    try:
        state = State()
        iteration = 0
        while iteration < _ITERATIONS_MAX:
            _set_initial_state(state)
            _send(conn, state)
            # When using queues, this call might modify the state before it is
            # actually sent to the consumer process. This is because data
            # is pushed through queues asynchronously in a separate thread.
            # This issue doesn't apply to pipes since the push operation is
            # synchronous, meaning that the sending process is blocked until
            # the data is fully sent.
            # On the other hand, pipes could hang if too much data is pushed
            # while no other process is consuming the data, requiring both
            # processes to respectively send and receive the data at the same
            # time.
            _modify_state(state)
            iteration += 1
    finally:
        _send(conn, 'END')
        conn.close()


def _consumer(conn):
    try:
        data = None
        while True:
            state = _receive(conn)
            if state == 'END':
                break

            # The 'initial' state is expected to be printed out.
            _LOGGER.debug(state)
    finally:
        conn.close()


def _set_initial_state(state):
    state.number = 1
    state.letter = 'a'
    state.seq = ['initial']


def _modify_state(state):
    state.number = 9
    state.letter = 'z'
    state.seq = ['modified']


def _send(conn, data):
    if _USE_QUEUE :
        conn.put(data, block=True)
    else:
        conn.send(data)


def _receive(conn):
    if _USE_QUEUE :
        return conn.get()
    else:
        return conn.recv()


if __name__ == '__main__':
    main()
