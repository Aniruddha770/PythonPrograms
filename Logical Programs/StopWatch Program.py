"""
   * Author - Aniruddha Patil
   * Date - 29July2021
   * Time - 20:58
   * Title - Write a Stopwatch Program for measuring the time that elapses between
             the start and end clicks

"""
import time

class StopWatch:
    try:
        while True:
            # print("Enter 1 to Start Time:");
            start = int(input("Enter 1 to Start:"))
            startTime = time.time()
            stop = int(input("Enter 0 to Stop Time:"))
            endTime = time.time()
            timeElapsed = endTime - startTime
            print("Time elapsed from Start to Stop is: ", timeElapsed, " Sec")
    except ValueError:
        print("Invalid input ")
