from math import pi,tan
import time
def decorator(func):
    def MAIN_decorator():
      now=time.perf_counter()
      func()
      NOw0=time.perf_counter()
      print("Time_left =",NOw0-now,"s\nStart_time =",now,"s\nEnd_time =",NOw0,end=" s\n")
    return MAIN_decorator
def main():
    s=float(input("S="))
    n=int(input("N="))
    out=ns**2/(4*tan(pi/n))
    print(out)
main=decorator(main)
main()
