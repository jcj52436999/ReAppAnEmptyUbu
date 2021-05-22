#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# multiPrcsgPoolJrnlDev.py  by  journaldev
# 
# copied from web and modified for study @author Joe Jackson 

from multiprocessing import Pool
import multiprocessing

import time
# import multiprocessing
print("Number of cpu : ", multiprocessing.cpu_count()) 

work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])


def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])


def pool_handler():
    p = Pool(2)
    p.map(work_log, work)


if __name__ == '__main__':
    pool_handler()
