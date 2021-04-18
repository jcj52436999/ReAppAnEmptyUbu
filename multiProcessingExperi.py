#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# multiProcessingExperi.py
# Created originally in 2021 as a simplistic exercise in broad-spectrum py use
# copied from web and modified for study @author Joe Jackson 



import time
import multiprocessing


def calc_square(numbers):
    for i in numbers:
        time.sleep(3) # artificial time-delay
        print('square: ', str(i * i))


def calc_cube(numbers):
    for i in numbers:
        time.sleep(3)
        print('cube: ', str(i * i * i))


if __name__ == "__main__":
     arr = [2, 3, 8, 9]
     p1 = multiprocessing.Process(target=calc_square, args=(arr,))
     p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
     # creating two Process here p1 & p2
     p1.start()
     p2.start()
     # starting Processes here parallel by using start function.
     # p1.join()
     # this join() will wait until the calc_square() function is finished.
     # p2.join()
     # this join() will wait unit the calc_cube() function is finished.
     print("Started two processes, squares and cubes!")


