#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# multiProcGlblVar.py
# Created originally in 2021 as a simplistic exercise in broad-spectrum py use
# copied from web and modified for study @author Joe Jackson 




import multiprocessing

results = []   #Creating a Global Variable

def calc_square(numbers):
   global results
   for i in numbers:
      print('square: ', str(i*i))
      results.append(i*i)
      print('witnin a result: '+str(results))



if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target = calc_square,args=(arr,))
    # creating one Process here p1

    p1.start()
    # starting Processes here parallel by using start function.

    p1.join()    

    # this join() will wait until the calc_square() function is    finished.


    print('result : '+str(results))
    #this print didn't work here we have to print it within the process    

    print("Successed!")

